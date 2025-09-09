# File: main.py

import os
import json
import subprocess
import sys
from dotenv import load_dotenv

# Import our custom functions
from generate_content import generate_math_lesson, list_available_concepts, suggest_related_concepts
from music import generate_voiceover
from combiner import combine_video_and_audio

# Load API keys from .env file
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("Checking dependencies...")
    
    # Check API keys
    if not ELEVENLABS_API_KEY:
        print("❌ ELEVENLABS_API_KEY not found in .env file")
        return False
    if not GEMINI_API_KEY:
        print("❌ GEMINI_API_KEY not found in .env file")
        return False
    
    # Check FFmpeg
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✅ FFmpeg is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ FFmpeg not found. Please install FFmpeg and add it to PATH")
        return False
    
    # Check Manim
    try:
        subprocess.run(['manim', '--version'], capture_output=True, check=True)
        print("✅ Manim is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Manim not found. Please install with: pip install manim")
        return False
    
    print("✅ All dependencies are ready!")
    return True

def get_user_choice():
    """Interactive menu for choosing math concepts"""
    print("\n" + "="*50)
    print("🎵 MUSICAL MATH TEACHER 🎵")
    print("="*50)
    
    print("\nChoose an option:")
    print("1. Browse available concepts")
    print("2. Enter a custom concept")
    print("3. Generate lessons for multiple concepts")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    return choice

def browse_concepts():
    """Let user browse and select from available concepts"""
    concepts = list_available_concepts()
    
    print(f"\nTotal concepts available: {len(concepts)}")
    print("\nEnter a concept name or part of it:")
    
    user_input = input("Search: ").strip()
    
    # Find matching concepts
    matches = [c for c in concepts if user_input.lower() in c.lower()]
    
    if matches:
        print(f"\nFound {len(matches)} matching concepts:")
        for i, concept in enumerate(matches, 1):
            print(f"{i}. {concept}")
        
        if len(matches) == 1:
            return matches[0]
        else:
            try:
                choice = int(input(f"\nSelect a concept (1-{len(matches)}): ")) - 1
                return matches[choice]
            except (ValueError, IndexError):
                print("Invalid selection. Using first match.")
                return matches[0]
    else:
        print("No exact matches found. Using your input as custom concept.")
        return user_input

def generate_single_lesson(concept, grade_level="middle school"):
    """Generate a single lesson"""
    print(f"\n🎯 Generating lesson for: '{concept}'")
    print("-" * 50)
    
    # Step 1: Generate Content
    print("📝 Step 1: Generating lesson content with Gemini AI...")
    try:
        lesson_json_str = generate_math_lesson(concept, grade_level)
        lesson_data = json.loads(lesson_json_str)
        
        # Save content
        content_filepath = f"lesson_content_{concept.replace(' ', '_').lower()}.json"
        with open(content_filepath, 'w') as f:
            json.dump(lesson_data, f, indent=4)
        print(f"✅ Content saved to {content_filepath}")
        
        # Show lesson preview
        print(f"\n📋 Lesson Preview:")
        print(f"Title: {lesson_data.get('title', 'N/A')}")
        print(f"Duration: {lesson_data.get('duration_minutes', 'N/A')} minutes")
        print(f"Difficulty: {lesson_data.get('difficulty', 'N/A')}")
        print(f"Key Points: {', '.join(lesson_data.get('key_points', []))}")
        
    except Exception as e:
        print(f"❌ Error generating content: {e}")
        return None
    
    # Step 2: Generate Voiceover
    print("\n🎤 Step 2: Generating voiceover...")
    narrator_script = lesson_data.get("narrator_script", "No script available.")
    voiceover_filepath = f"voiceover_{concept.replace(' ', '_').lower()}.mp3"
    
    if generate_voiceover(narrator_script, voiceover_filepath, ELEVENLABS_API_KEY):
        print(f"✅ Voiceover saved to {voiceover_filepath}")
    else:
        print("❌ Failed to generate voiceover")
        return None
    
    # Step 3: Render Manim Animation
    print("\n🎬 Step 3: Rendering Manim animation...")
    print("This may take a few minutes...")
    
    try:
        # Update the lesson content file for Manim to read
        with open('lesson_content.json', 'w') as f:
            json.dump(lesson_data, f, indent=4)
        
        manim_command = [
            "manim",
            "-ql",  # Low quality for faster rendering
            "musical_math_lesson.py",
            "MusicalMathLesson"
        ]
        
        result = subprocess.run(manim_command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Animation rendered successfully")
        else:
            print(f"❌ Manim rendering failed: {result.stderr}")
            return None
            
    except Exception as e:
        print(f"❌ Error during animation rendering: {e}")
        return None
    
    # Step 4: Find the rendered video
    video_paths = [
        os.path.join("media", "videos", "musical_math_lesson", "480p15", "MusicalMathLesson.mp4"),
        os.path.join("media", "videos", "musical_math_lesson", "720p30", "MusicalMathLesson.mp4"),
    ]
    
    silent_video_path = None
    for path in video_paths:
        if os.path.exists(path):
            silent_video_path = path
            break
    
    if not silent_video_path:
        print("❌ Could not find rendered video file")
        return None
    
    # Step 5: Combine Video and Audio
    print("\n🎵 Step 5: Combining video and audio...")
    output_video_path = f"final_lesson_{concept.replace(' ', '_').lower()}.mp4"
    
    if combine_video_and_audio(silent_video_path, voiceover_filepath, output_video_path):
        print(f"🎉 SUCCESS! Final video created: {output_video_path}")
        
        # Show lesson summary
        print(f"\n📊 Lesson Summary:")
        print(f"Concept: {concept}")
        print(f"Grade Level: {grade_level}")
        print(f"Video File: {output_video_path}")
        print(f"Duration: ~{lesson_data.get('duration_minutes', 3)} minutes")
        
        # Suggest related concepts
        related = suggest_related_concepts(concept)
        if related:
            print(f"💡 You might also like: {', '.join(related)}")
        
        return output_video_path
    else:
        print("❌ Failed to combine video and audio")
        return None

def generate_multiple_lessons():
    """Generate lessons for multiple concepts"""
    concepts = input("Enter math concepts separated by commas: ").strip().split(',')
    concepts = [c.strip() for c in concepts if c.strip()]
    
    if not concepts:
        print("No concepts provided.")
        return
    
    grade_level = input("Enter grade level (elementary/middle school/high school) [middle school]: ").strip() or "middle school"
    
    print(f"\n🎯 Generating {len(concepts)} lessons...")
    
    successful = []
    failed = []
    
    for i, concept in enumerate(concepts, 1):
        print(f"\n{'='*20} Lesson {i}/{len(concepts)} {'='*20}")
        result = generate_single_lesson(concept, grade_level)
        
        if result:
            successful.append(concept)
        else:
            failed.append(concept)
    
    # Summary
    print(f"\n🎉 BATCH COMPLETE!")
    print(f"✅ Successful: {len(successful)} lessons")
    print(f"❌ Failed: {len(failed)} lessons")
    
    if successful:
        print(f"\nSuccessfully created lessons for:")
        for concept in successful:
            print(f"  • {concept}")
    
    if failed:
        print(f"\nFailed to create lessons for:")
        for concept in failed:
            print(f"  • {concept}")

def main():
    """Main function with enhanced user interaction"""
    print("🚀 Starting Musical Math Teacher...")
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Please fix the above issues before continuing.")
        sys.exit(1)
    
    while True:
        choice = get_user_choice()
        
        if choice == '1':
            # Browse concepts
            concept = browse_concepts()
            grade_level = input("Enter grade level (elementary/middle school/high school) [middle school]: ").strip() or "middle school"
            generate_single_lesson(concept, grade_level)
            
        elif choice == '2':
            # Custom concept
            concept = input("Enter your math concept: ").strip()
            if concept:
                grade_level = input("Enter grade level (elementary/middle school/high school) [middle school]: ").strip() or "middle school"
                generate_single_lesson(concept, grade_level)
            
        elif choice == '3':
            # Multiple concepts
            generate_multiple_lessons()
            
        elif choice == '4':
            print("👋 Thanks for using Musical Math Teacher!")
            break
            
        else:
            print("Invalid choice. Please try again.")
        
        # Ask if user wants to continue
        if choice in ['1', '2', '3']:
            continue_choice = input("\n🔄 Would you like to create another lesson? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("👋 Thanks for using Musical Math Teacher!")
                break

if __name__ == "__main__":
    main()