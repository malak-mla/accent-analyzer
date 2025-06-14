from transformers import pipeline
from .config import ACCENT_MAP

class AccentScorer:
    def __init__(self):
        self.model = pipeline(
            "audio-classification", 
            model="taln-ls/accent-classification-english"
        )
    
    def score_accent(self, audio_path: str) -> dict:
        """Score English accents with confidence"""
        results = self.model(audio_path)
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        
        # Get top result
        top_result = sorted_results[0]
        label = top_result['label']
        
        # Map to human-readable label
        accent_info = ACCENT_MAP.get(label, {"label": "Unknown", "threshold": 0.5})
        
        # Calculate confidence score
        confidence = self._calculate_confidence(top_result['score'], accent_info['threshold'])
        
        return {
            "accent": accent_info['label'],
            "confidence": confidence,
            "all_scores": [
                {"accent": ACCENT_MAP.get(r['label'], {"label": r['label']})["label"], 
                 "score": r['score']}
                for r in sorted_results
            ]
        }
    
    def _calculate_confidence(self, score: float, threshold: float) -> float:
        """Calculate normalized confidence score (0-100%)"""
        if score >= threshold:
            return min(100, 70 + 30 * ((score - threshold) / (1.0 - threshold)))
        else:
            return max(0, 70 * (score / threshold))