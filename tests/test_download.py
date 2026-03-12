import pytest
import yt_dlp
import os

def test_yt_dlp_import():
    assert yt_dlp is not None

def test_download_dir():
    # Smoke test: create dir
    os.makedirs("downloads", exist_ok=True)
    assert os.path.exists("downloads")

