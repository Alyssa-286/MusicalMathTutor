# File: combiner.py

import subprocess
import os

def combine_video_and_audio(video_path, audio_path, output_path):
    """
    Combines a video file and an audio file into one output video using FFmpeg.

    Args:
        video_path (str): Path to the input video file (silent).
        audio_path (str): Path to the input audio file (voiceover).
        output_path (str): Path to save the final combined video.

    Returns:
        str: The output path if successful, None otherwise.
    """
    print(f"🎵 Combining video '{video_path}' and audio '{audio_path}'...")

    # Ensure the input files exist before proceeding
    if not os.path.exists(video_path):
        print(f"❌ Error: Video file not found at {video_path}")
        return None
    if not os.path.exists(audio_path):
        print(f"❌ Error: Audio file not found at {audio_path}")
        return None

    # FFmpeg command to merge video and audio
    command = [
        'ffmpeg',
        '-y',  # Overwrite output file if it exists
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',      # Copy the video stream without re-encoding (it's faster)
        '-c:a', 'aac',       # Re-encode audio to AAC, a standard format
        '-shortest',         # Finish encoding when the shortest input stream ends
        output_path
    ]
    
    try:
        # Run the command
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✅ Successfully created final video: {output_path}")
        return output_path
        
    except subprocess.CalledProcessError as e:
        # This catches errors from FFmpeg itself
        print("❌ Error during FFmpeg execution:")
        print(f"FFmpeg stderr: {e.stderr}")
        return None
        
    except FileNotFoundError:
        # This catches the error if FFmpeg is not installed or not in the system's PATH
        print("❌ Error: 'ffmpeg' command not found.")
        print("Please ensure FFmpeg is installed and accessible from your terminal.")
        return None