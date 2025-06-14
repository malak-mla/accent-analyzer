# 🌍 English Accent Analyzer

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/<your-username>/accent-analyzer/app.py)

Professional tool for evaluating spoken English proficiency by analyzing accent characteristics.

## Features
- Supports any public video URL (YouTube, Loom, direct links)
- Accent classification (American, British, Australian, Canadian)
- Confidence scoring (0-100%)
- Speech transcription with English confidence
- Detailed analysis reports

## How to Test
1. Click the "Open in Streamlit" badge above
2. Paste a public video URL
3. Click "Analyze Accent"
4. View results in 30-60 seconds

## Sample Test URLs
- American English: https://download.samplelib.com/mp4/sample-5s.mp4
- British English: https://www.youtube.com/watch?v=8UQzCQ4I7X0
- Australian English: https://www.youtube.com/watch?v=5g0Evw3GXfM

## Technical Details
- Speech Recognition: OpenAI Whisper
- Accent Classification: Wav2Vec2 model
- Video Processing: MoviePy + PyDub
- Hosting: Streamlit Community Cloud

[Report Issues](https://github.com/<your-username>/accent-analyzer/issues)