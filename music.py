# File: E:\musicalmathtutor\music.py

from elevenlabs.client import ElevenLabs
from elevenlabs import save
import os

def generate_voiceover(text, filename, api_key):
    """Generates an MP3 voiceover from text using ElevenLabs."""
    try:
        print(f"Generating voiceover for: '{text[:30]}...'")
        
        client = ElevenLabs(api_key=api_key)
        
        # CORRECTED LINE: The `generate` method is now part of `text_to_speech`
        audio = client.text_to_speech.generate(
            text=text,
            voice="Rachel",  # You can choose different voices
            model="eleven_multilingual_v2"
        )
        save(audio, filename)
        print(f"Successfully saved voiceover to {filename}")
        return filename
    except Exception as e:
        print(f"Error generating voiceover: {e}")
        return None