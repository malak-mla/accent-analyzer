import pytest
import numpy as np
from core.scorer import AccentScorer
from core.config import ACCENT_MAP

@pytest.fixture
def scorer():
    return AccentScorer()

def test_score_accent(scorer, sample_audio_path):
    result = scorer.score_accent(sample_audio_path)
    assert 'accent' in result
    assert 'confidence' in result
    assert isinstance(result['confidence'], float)
    assert 0 <= result['confidence'] <= 100
    
    # Check all accents are in the map
    for score in result['all_scores']:
        assert score['accent'] in ACCENT_MAP.values() or score['accent'] in ACCENT_MAP.keys()

def test_confidence_calculation(scorer):
    # Test threshold edge cases
    assert scorer._calculate_confidence(0.8, 0.7) > 70
    assert scorer._calculate_confidence(0.6, 0.7) < 70
    assert scorer._calculate_confidence(1.0, 0.7) == 100
    assert scorer._calculate_confidence(0.0, 0.7) == 0