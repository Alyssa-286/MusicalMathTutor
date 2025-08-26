# Musical Math Tutor

This project creates engaging math lesson videos by combining AI-generated scripts with Manim animations and voiceovers.

---

### ## How to Run

Execute the main script from your terminal and follow the prompts:

`python main.py`

The script will ask for a math concept and then generate the final video as `final_lesson.mp4`.

---

### ## Setup Instructions

**1. Clone the repository:**
`git clone <your-repo-url>`
`cd <repo-name>`

**2. Create and activate a virtual environment:**
`python -m venv venv`
`source venv/bin/activate` _(On Windows use `venv\Scripts\activate`)_

**3. Install dependencies:**
`pip install -r requirements.txt`

**4. Set up environment variables:**

- Create a file named `.env` in the root directory.
- Add your API keys in `KEY=VALUE` format:
  `    OPENAI_API_KEY="your_openai_key"
   ELEVENLABS_API_KEY="your_elevenlabs_key"
 `
  **5. Install FFmpeg:**
  This project requires FFmpeg for video processing. Please [install it](https://ffmpeg.org/download.html) and ensure it's in your system's PATH.
