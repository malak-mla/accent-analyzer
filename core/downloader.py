import requests
import os
import validators
from .config import SUPPORTED_FORMATS

def download_video(url: str, temp_dir: str) -> str:
    """Download video from any public URL"""
    if not validators.url(url):
        raise ValueError("Invalid URL format")
    
    # Check if direct video link
    if any(url.lower().endswith(ext) for ext in SUPPORTED_FORMATS):
        return _download_direct(url, temp_dir)
    
    # Try as generic video
    return _download_generic(url, temp_dir)

def _download_direct(url: str, temp_dir: str) -> str:
    """Download direct video file"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, stream=True, timeout=30)
    response.raise_for_status()
    
    # Get filename from URL or content-disposition
    filename = url.split('/')[-1].split('?')[0]
    if 'content-disposition' in response.headers:
        content = response.headers['content-disposition']
        filename = content.split('filename=')[1].strip('"')
    
    video_path = os.path.join(temp_dir, filename)
    
    with open(video_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
    
    return video_path

def _download_generic(url: str, temp_dir: str) -> str:
    """Download video using yt-dlp for supported platforms"""
    try:
        import yt_dlp
    except ImportError:
        raise RuntimeError("yt-dlp required for non-direct URLs")
    
    ydl_opts = {
        'outtmpl': os.path.join(temp_dir, 'video.%(ext)s'),
        'quiet': True,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)