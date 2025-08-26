# File: musical_math_lesson.py

from manim import *
import json

# REMOVE the old SAMPLE_DATA

# Load the dynamically generated content from the JSON file
try:
    with open('lesson_content.json', 'r') as f:
        script_data = json.load(f)
except FileNotFoundError:
    print("Error: lesson_content.json not found. Please run main.py first.")
    # Use fallback data so the script doesn't crash if run directly
    script_data = {
        "narrator_script": "Error: Could not load content.",
        "lyrics": "",
        "manim_commands": []
    }

class MusicalMathLesson(Scene):
    def construct(self):
        # The rest of your construct method remains EXACTLY THE SAME!
        # It will now use the loaded `script_data`.
        
        # 1. Animate the narrator script
        narration_text = MarkupText(script_data['narrator_script']).set_width(config.frame_width - 1).to_edge(UP)
        self.play(Write(narration_text))
        # ... and so on ...