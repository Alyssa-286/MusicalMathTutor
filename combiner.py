import subprocess

# This is the function you posted
def combine_video_and_audio(video_path, audio_path, output_path):
    """Combines a video file and an audio file into one output video."""
    print(f"Combining video '{video_path}' and audio '{audio_path}'...")
    command = [
        'ffmpeg',
        '-y',
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-shortest',
        output_path
    ]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Successfully created final video: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print("Error during FFmpeg execution:")
        print(e.stderr)
        return None

if __name__ == "__main__":
    # Use the full path to your video file.
    # Note how single backslashes \ are changed to double backslashes \\
    video_file = r"E:\\musicalmathtutor\\media\\videos\\musical_math_lesson\\720p30\\MusicalMathLesson.mp4"
    
    # Make sure this audio file is in the same folder as your script (E:\musicalmathtutor)
    audio_file = "explanation_voiceover.mp3" 
    
    output_file = "final_lesson_with_audio.mp4"
    
    # Now, this function knows exactly where to find the video
    combine_video_and_audio(video_file, audio_file, output_file)