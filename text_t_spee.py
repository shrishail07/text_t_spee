import streamlit as st
from gtts import gTTS
import os

# Set up page configuration
st.set_page_config(page_title="Text to Speech Converter", page_icon="🔊", layout="centered")

# Title and description
st.title("🔊 Text to Speech Converter")
st.write("Convert your written text into an audio file instantly and download it as an MP3.")

st.markdown("---")

# User Input
text_input = st.text_area(
    "Enter the text you want to convert:",
    placeholder="Type something here...",
    height=150
)

# Optional settings
language = st.selectbox(
    "Select Language Accent",
    options=["en", "es", "fr", "de", "it"],
    format_func=lambda x: {"en": "English", "es": "Spanish", "fr": "French", "de": "German", "it": "Italian"}[x]
)

st.markdown("---")

# Convert Button
if st.button("Convert to Speech", type="primary"):
    if text_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Generating audio... Please wait."):
            try:
                # Initialize gTTS with the text and language
                tts = gTTS(text=text_input, lang=language, slow=False)
                
                # Define filename
                filename = "speech.mp3"
                
                # Save the audio file locally (File Handling)
                tts.save(filename)
                
                # Success message
                st.success("Conversion successful!")
                
                # Streamlit audio player
                with open(filename, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    
                    # Play the audio inside the app
                    st.audio(audio_bytes, format="audio/mp3")
                    
                    # Download button for MP3
                    st.download_button(
                        label="📥 Download MP3",
                        data=audio_bytes,
                        file_name="converted_speech.mp3",
                        mime="audio/mp3"
                    )
                
                # Clean up the file after reading it into memory
                if os.path.exists(filename):
                    os.remove(filename)
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
