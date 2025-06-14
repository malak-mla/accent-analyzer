import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from .config import SUPPORTED_FORMATS, SAMPLE_RATE, MAX_DURATION

def extract_audio(video_path: str, temp_dir: str) -> str:
    """Extract audio from video and convert to 16kHz WAV"""
    audio_path = os.path.join(temp_dir, "audio.wav")
    
    # Check duration
    duration = _get_duration(video_path)
    if duration > MAX_DURATION:
        raise ValueError(f"Video too long ({duration}s > {MAX_DURATION}s max)")
    
    # Use moviepy for supported formats
    if any(video_path.lower().endswith(ext) for ext in SUPPORTED_FORMATS):
        clip = VideoFileClip(video_path)
        clip.audio.write_audiofile(audio_path, fps=SAMPLE_RATE, verbose=False)
        return audio_path
    
    # Fallback to pydub
    audio = AudioSegment.from_file(video_path)
    audio = audio.set_frame_rate(SAMPLE_RATE).set_channels(1)
    audio.export(audio_path, format="wav")
    return audio_path

def _get_duration(video_path: str) -> float:
    """Get video duration in seconds"""
    try:
        clip = VideoFileClip(video_path)
        return clip.duration
    except:
        audio = AudioSegment.from_file(video_path)
        return len(audio) / 1000.0