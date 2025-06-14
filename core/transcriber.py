from transformers import pipeline
from .config import SAMPLE_RATE, LANGUAGE_THRESHOLD

class Transcriber:
    def __init__(self):
        self.model = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-tiny.en",
            chunk_length_s=30
        )
    
    def transcribe(self, audio_path: str) -> dict:
        """Transcribe audio and return text with confidence"""
        result = self.model(
            audio_path,
            return_timestamps=True,
            generate_kwargs={"language": "english"}
        )
        
        # Calculate overall confidence
        segments = result.get('chunks', [])
        if not segments:
            return {"text": "", "confidence": 0.0, "is_english": False}
        
        # Calculate average confidence
        confidences = [seg['confidence'] for seg in segments if 'confidence' in seg]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
        
        return {
            "text": result["text"],
            "confidence": avg_confidence,
            "is_english": avg_confidence >= LANGUAGE_THRESHOLD
        }