# Configuration constants
SUPPORTED_FORMATS = ['.mp4', '.mov', '.webm', '.mkv', '.avi']
MAX_DURATION = 300  # 5 minutes maximum processing
SAMPLE_RATE = 16000
LANGUAGE_THRESHOLD = 0.85  # Minimum confidence for English detection
ACCENT_MAP = {
    'us': {'label': 'American 🇺🇸', 'threshold': 0.7},
    'england': {'label': 'British 🇬🇧', 'threshold': 0.7},
    'australia': {'label': 'Australian 🇦🇺', 'threshold': 0.7},
    'canada': {'label': 'Canadian 🇨🇦', 'threshold': 0.7},
    'neutral': {'label': 'Neutral English', 'threshold': 0.6}
}