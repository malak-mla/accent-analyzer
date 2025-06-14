import pytest
import os
from core.downloader import download_video
from core.config import SUPPORTED_FORMATS

@pytest.mark.parametrize("url", [
    "https://download.samplelib.com/mp4/sample-5s.mp4",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
])
def test_download_video(url, tmp_path):
    video_path = download_video(url, str(tmp_path))
    assert os.path.exists(video_path)
    assert os.path.getsize(video_path) > 10000  # At least 10KB

def test_invalid_url():
    with pytest.raises(ValueError):
        download_video("not-a-url", "/tmp")