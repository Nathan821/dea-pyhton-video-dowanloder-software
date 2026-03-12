# Python DEA - Video Downloader

![Python DEA](https://via.placeholder.com/800x400?text=Python+DEA)

**Python Downloader Extraordinaire Awesome (DEA)**: Open-source CLI & GUI video downloader supporting YouTube, TikTok, Instagram, and 1000+ sites via yt-dlp.

## Features
- CLI: `dea --url https://youtube.com/watch?v=...`
- GUI: Simple Tkinter app with URL input, progress, download.
- Best quality auto-download (video+audio).
- Playlists support.
- Cross-platform (Windows/Linux/macOS).

## Installation
1. Clone/Download repo.
2. `python -m venv .venv`
3. `.venv\\Scripts\\activate` (Windows) or `source .venv/bin/activate`
4. `pip install -e .`
5. Install ffmpeg: https://ffmpeg.org/download.html (recommended for merging).

## CLI Usage
```
dea --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --output "downloads/%(title)s.%(ext)s"
dea --playlist "https://youtube.com/playlist?list=..."
```

## GUI Usage
```
python -m python_dea.gui
```
Enter URL, click Download.

## Dependencies
- yt-dlp (pip)
- tkinter (Python stdlib)
- ffmpeg (optional, external)

## Testing
`pip install -r requirements.txt -e .[test] && pytest`

## Contributing
Fork, PR to main. Issues welcome.

## License
MIT

