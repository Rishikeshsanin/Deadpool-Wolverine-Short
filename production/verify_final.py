#!/usr/bin/env python3
"""Validate the REAL rendered MP4. This does not prove artistic quality; listen and visually inspect too."""
import json
import math
import pathlib
import subprocess
import sys

def run(*args):
    return subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout

def verify(path):
    path = pathlib.Path(path)
    if not path.is_file() or path.stat().st_size < 500_000:
        raise RuntimeError(f"No substantial rendered MP4 at {path}")
    data = json.loads(run("ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)))
    videos = [s for s in data["streams"] if s.get("codec_type") == "video"]
    audios = [s for s in data["streams"] if s.get("codec_type") == "audio"]
    if len(videos) != 1 or not audios:
        raise RuntimeError("Expected one video stream and an audio stream")
    video = videos[0]
    num, den = map(int, video.get("avg_frame_rate", "0/1").split("/"))
    fps = num / den if den else 0
    seconds = float(data["format"]["duration"])
    checks = {
        "h264": video.get("codec_name") == "h264",
        "1080x1920": (video.get("width"), video.get("height")) == (1080, 1920),
        "30fps": math.isclose(fps, 30.0, abs_tol=0.1),
        "28_to_35_seconds": 28 <= seconds <= 35,
        "aac_audio": any(s.get("codec_name") == "aac" for s in audios),
    }
    subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "null", "-"], check=True)
    print(json.dumps({"path": str(path), "seconds": seconds, "fps": fps, "size_bytes": path.stat().st_size, "checks": checks}, indent=2))
    return all(checks.values())

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python production/verify_final.py deliverables/deadpool_wolverine_nuke_1080x1920.mp4")
        sys.exit(0 if verify(sys.argv[1]) else 1)
    except (RuntimeError, ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        sys.exit(1)