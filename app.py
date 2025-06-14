import streamlit as st
import tempfile
import os
import time
from core.downloader import download_video
from core.audio_processor import extract_audio
from core.transcriber import Transcriber
from core.scorer import AccentScorer

# Initialize models (cached)
@st.cache_resource
def load_transcriber():
    return Transcriber()

@st.cache_resource
def load_scorer():
    return AccentScorer()

def show_results(transcript, accent_result, audio_path):
    """Display analysis results"""
    with st.container():
        st.success("✅ Analysis Complete!")
        st.audio(audio_path, format="audio/wav")
        
        # Language confidence
        lang_status = "🟢 English" if transcript['is_english'] else "🔴 Non-English"
        st.subheader(f"Language: {lang_status} (Confidence: {transcript['confidence']*100:.1f}%)")
        
        # Accent results
        st.subheader(f"Accent: {accent_result['accent']}")
        st.metric("Accent Confidence", f"{accent_result['confidence']:.1f}%")
        
        # Confidence visualization
        with st.expander("Detailed Confidence Scores"):
            for score in accent_result['all_scores']:
                st.progress(score['score'], text=f"{score['accent']}: {score['score']*100:.1f}%")
        
        # Transcript
        with st.expander("View Transcript"):
            st.caption(f"Overall Confidence: {transcript['confidence']*100:.1f}%")
            st.write(transcript['text'])
        
        # Interpretation
        with st.expander("Interpretation Guide"):
            st.markdown("""
            - **85-100%**: Strong accent characteristics
            - **70-85%**: Clear accent features
            - **60-70%**: Moderate accent features
            - **<60%**: Weak or mixed accent characteristics
            """)
            st.markdown(f"""
            **Analysis Summary**:  
            The speaker demonstrates {'strong' if accent_result['confidence'] > 85 else 'clear' if accent_result['confidence'] > 70 else 'moderate'} 
            characteristics of a {accent_result['accent']} accent, with an English language confidence of 
            {transcript['confidence']*100:.1f}%.
            """)

# Streamlit UI
st.set_page_config(page_title="🌍 Accent Analyzer", layout="wide")
st.title("🌍 English Accent Analyzer")
st.markdown("""
**Analyze spoken English proficiency**  
*Upload a video URL to evaluate accent and speaking clarity*
""")

# Input section
url = st.text_input("Enter video URL:", 
                   placeholder="https://example.com/video.mp4 or YouTube/Loom link")

if st.button("Analyze Accent", type="primary", use_container_width=True):
    if not url:
        st.warning("Please enter a video URL")
        st.stop()
    
    # Setup processing
    progress_bar = st.progress(0)
    status = st.empty()
    results_placeholder = st.empty()
    
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Step 1: Download
            status.subheader("Step 1: Downloading video...")
            video_path = download_video(url, temp_dir)
            progress_bar.progress(20)
            
            # Step 2: Extract audio
            status.subheader("Step 2: Extracting audio...")
            audio_path = extract_audio(video_path, temp_dir)
            progress_bar.progress(40)
            
            # Step 3: Transcribe
            status.subheader("Step 3: Transcribing speech...")
            transcriber = load_transcriber()
            transcript = transcriber.transcribe(audio_path)
            progress_bar.progress(60)
            
            # Step 4: Score accent
            status.subheader("Step 4: Analyzing accent...")
            scorer = load_scorer()
            accent_result = scorer.score_accent(audio_path)
            progress_bar.progress(100)
            
            # Display results
            show_results(transcript, accent_result, audio_path)
    
    except Exception as e:
        status.error(f"❌ Processing error: {str(e)}")
        progress_bar.empty()

# Footer
st.markdown("---")
st.caption("Accent Analysis System v1.0 | Uses Whisper and Wav2Vec2 AI models")