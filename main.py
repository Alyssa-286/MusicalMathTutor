# File: main.py

import os
import json
import subprocess
from dotenv import load_dotenv

# Import our custom functions
from generate_content import generate_math_lesson
from music import generate_voiceover
from combiner import combine_video_and_audio

# Load API keys from .env file
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def main():
    # --- Step 1: Get User Input & Generate Content ---
    math_concept = input("Enter the math concept you want to create a video for: ")
    print(f"Generating lesson content for '{math_concept}'...")
    
    # Get the structured lesson data from the AI
    lesson_json_str = generate_math_lesson(math_concept)
    lesson_data = json.loads(lesson_json_str)

    # Save the content to a file so Manim can read it
    content_filepath = "lesson_content.json"
    with open(content_filepath, 'w') as f:
        json.dump(lesson_data, f, indent=4)
    print(f"Lesson content saved to {content_filepath}")

    # --- Step 2: Generate Voiceover ---
    narrator_script = lesson_data.get("narrator_script", "No script found.")
    voiceover_filepath = "voiceover.mp3"
    generate_voiceover(narrator_script, voiceover_filepath, ELEVENLABS_API_KEY)

    # --- Step 3: Render the Manim Animation (Silent Video) ---
    print("Rendering the Manim animation... This may take a moment.")
    manim_command = [
        "manim",
        "-ql", # ql for low quality, use -qh for high quality
        "musical_math_lesson.py",
        "MusicalMathLesson"
    ]
    subprocess.run(manim_command, check=True)
    
    # Manim saves videos in a specific folder structure
    silent_video_path = os.path.join("media", "videos", "musical_math_lesson", "480p15", "MusicalMathLesson.mp4")

    # --- Step 4: Combine Video and Audio ---
    output_video_path = "final_lesson.mp4"
    combine_video_and_audio(silent_video_path, voiceover_filepath, output_video_path)

if __name__ == "__main__":
    main()