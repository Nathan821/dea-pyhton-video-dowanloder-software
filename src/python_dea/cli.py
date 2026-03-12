#!/usr/bin/env python
import argparse
import os
import sys
from pathlib import Path

import yt_dlp

def download_video(url, output=None):
    if output is None:
        output = "downloads/%(title)s.%(ext)s"
    
    os.makedirs("downloads", exist_ok=True)
    
    ydl_opts = {
        'format': 'best[height<=1080]/best',  # Best <=1080p
        'outtmpl': output,
        'progress_hooks': [progress_hook],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '?')
        speed = d.get('_speed_str', '?')
        eta = d.get('_eta_str', '?')
        print(f"Progress: {percent} | Speed: {speed} | ETA: {eta}")
    elif d['status'] == 'finished':
        print(f"Downloaded: {d['filename']}")

def main():
    parser = argparse.ArgumentParser(description="Python DEA Video Downloader CLI")
    parser.add_argument("--url", "-u", required=True, help="Video/playlist URL")
    parser.add_argument("--output", "-o", default=None, help="Output template")
    
    args = parser.parse_args()
    try:
        download_video(args.url, args.output)
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

