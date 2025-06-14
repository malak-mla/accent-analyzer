# English Accent Analyzer

Professional tool for evaluating spoken English proficiency by analyzing accent characteristics and speech clarity.

## Features
- Supports any public video URL (YouTube, Loom, direct links)
- Speech-to-text transcription with confidence scoring
- Accent classification (American, British, Australian, Canadian)
- Confidence scoring (0-100%)
- Detailed analysis reports

## Installation

```bash
# Clone repository
git clone https://github.com/<your-username>/accent-analyzer.git
cd accent-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Run Streamlit App
```bash
streamlit run app.py
```

### Test Sample URLs
1. American English: 
   ```
   https://download.samplelib.com/mp4/sample-5s.mp4
   ```
2. British English: 
   ```
   https://www.youtube.com/watch?v=8UQzCQ4I7X0
   ```
3. Australian English: 
   ```
   https://www.youtube.com/watch?v=5g0Evw3GXfM
   ```

### Test with Your Own Video
1. Upload to a cloud service (Google Drive, Dropbox)
2. Get a shareable link (make sure it's publicly accessible)
3. Paste the link in the app

## Architecture
```
core/
  downloader.py      # Video downloading
  audio_processor.py # Audio extraction
  transcriber.py     # Speech-to-text
  scorer.py          # Accent scoring
app.py               # Streamlit UI
```

## Testing
```bash
pytest tests/
```

## Deployment
1. Create Streamlit account at [share.streamlit.io](https://share.streamlit.io/)
2. Connect your GitHub repository
3. Set main file to `app.py`
4. Deploy!

## Technical Approach
1. **Video Download**: 
   - Direct video links downloaded via requests
   - Platform links (YouTube/Loom) handled with yt-dlp
   
2. **Audio Processing**:
   - Converted to 16kHz mono WAV
   - Limited to 5 minutes for processing efficiency
   
3. **Speech Recognition**:
   - OpenAI Whisper model for transcription
   - Confidence score calculated from word-level probabilities
   - Language detection based on transcription confidence
   
4. **Accent Scoring**:
   - Wav2Vec2 model fine-tuned for accent classification
   - Confidence normalized to 0-100% scale
   - Threshold-based scoring for clear classification
```

## How to Use in VS Code:

1. **Create Project Structure:**
   ```bash
   mkdir accent-analyzer
   cd accent-analyzer
   mkdir core tests
   touch app.py requirements.txt README.md .gitignore
   touch core/__init__.py core/downloader.py core/audio_processor.py
   touch core/transcriber.py core/scorer.py core/config.py
   touch tests/test_downloader.py tests/test_scorer.py
   ```

2. **Copy the code** for each file as shown above

3. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Test Locally:**
   ```bash
   streamlit run app.py
   ```

5. **Run Tests:**
   ```bash
   pytest tests/
   ```

6. **Initialize Git:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

7. **Create GitHub Repository:**
   - Go to GitHub and create new repository
   - Follow instructions to push existing repository

8. **Deploy to Streamlit:**
   - Connect your GitHub account at share.streamlit.io
   - Select repository and app.py file
   - Deploy

## Key Features:

1. **Modular Architecture**:
   - Clear separation of concerns
   - Reusable components
   - Easy testing

2. **Robust Processing**:
   - Handles any public video URL
   - Supports multiple video formats
   - Automatic format conversion

3. **Accurate Scoring**:
   - Whisper ASR for transcription
   - Wav2Vec2 for accent classification
   - Normalized confidence scoring

4. **Professional UI**:
   - Step-by-step progress
   - Audio preview
   - Detailed confidence visualization
   - Transcript display

5. **Test Coverage**:
   - Unit tests for critical components
   - Sample test cases
   - Easy to extend

This solution provides a professional, maintainable, and accurate system for evaluating English accents from video URLs, with a clear focus on hiring assessment needs.