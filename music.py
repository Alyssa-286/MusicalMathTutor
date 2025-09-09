# File: music.py

import os
from elevenlabs.client import ElevenLabs
from elevenlabs import save

def generate_voiceover(text, filename, api_key):
    """
    Generates an MP3 voiceover from text using the ElevenLabs API.
    This version uses the correct client.generate() method.
    """
    if not api_key:
        print("❌ Error: ElevenLabs API key is not set.")
        return None
        
    try:
        print(f"🎤 Generating voiceover for: '{text[:40]}...'")
        
        # 1. Initialize the main ElevenLabs client
        client = ElevenLabs(api_key=api_key)
        
        # 2. Call the .generate() method DIRECTLY on the client object.
        # This is the correct syntax.
        audio = client.generate(
            text=text,
            voice="Rachel",
            model="eleven_multilingual_v2"
        )
        
        # 3. Save the generated audio to the specified file
        save(audio, filename)
        
        print(f"✅ Successfully saved voiceover to {filename}")
        return filename
        
    except Exception as e:
        print(f"❌ Error during voiceover generation: {e}")
        return None