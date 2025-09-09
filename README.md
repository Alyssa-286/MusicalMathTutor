# 🎵 Musical Math Teacher

An AI-powered educational tool that creates engaging math lesson videos by combining Gemini AI-generated scripts, Manim animations, and ElevenLabs voiceovers.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **🧠 AI-Generated Lessons**: Uses Google's Gemini AI to create comprehensive math lessons
- **🎬 Dynamic Animations**: Manim-powered visual animations that adapt to different concepts
- **🎤 Voice Narration**: ElevenLabs text-to-speech for engaging audio
- **📚 Multi-Level Support**: Elementary, Middle School, and High School concepts
- **🎯 Vast Concept Coverage**: 50+ math concepts across different categories
- **🎵 Musical Elements**: Catchy songs and rhymes to help memorization
- **📊 Batch Processing**: Generate multiple lessons at once

## 📋 Supported Math Concepts

### Elementary Level

- **Arithmetic**: Addition, Subtraction, Multiplication, Division, Fractions, Decimals
- **Geometry**: Shapes, Perimeter, Area, Symmetry
- **Measurement**: Time, Money, Length, Weight, Volume

### Middle School Level

- **Algebra**: Linear Equations, Inequalities, Exponents, Polynomials, Factoring
- **Geometry**: Triangles, Circles, Pythagorean Theorem, Surface Area, Volume
- **Statistics**: Mean/Median/Mode, Probability, Data Analysis, Graphs
- **Number Theory**: Prime Numbers, GCF, LCM, Ratios, Proportions

### High School Level

- **Algebra II**: Quadratic Equations, Logarithms, Complex Numbers, Sequences
- **Advanced Geometry**: Trigonometry, Coordinate Geometry, Transformations, Proofs
- **Calculus**: Limits, Derivatives, Integrals, Applications
- **Statistics**: Standard Deviation, Normal Distribution, Hypothesis Testing

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed
2. **FFmpeg** installed and in PATH ([Download here](https://ffmpeg.org/download.html))
3. **Git** installed

### Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd musical-math-teacher
```

2. **Create virtual environment**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up API keys**

Create a `.env` file in the project root:

```bash
cp .env.template .env
```

Edit `.env` and add your API keys:

```
GEMINI_API_KEY=your_gemini_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

### 5. Verify Your Setup (Recommended)

Run the setup test script to ensure all dependencies and API keys are correctly configured:

````bash
python test_setup.py

**Getting API Keys:**

- **Gemini AI**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **ElevenLabs**: Visit [ElevenLabs](https://elevenlabs.io/app/speech-synthesis)

### 🎯 Usage

Run the main script:

```bash
python main.py
````

The interactive menu will guide you through:

1. **Browse Concepts**: Choose from 50+ predefined math concepts
2. **Custom Concept**: Enter any math topic you want
3. **Batch Generation**: Create multiple lessons at once
4. **Exit**: Close the application

### Example Usage

```bash
$ python main.py

🎵 MUSICAL MATH TEACHER 🎵
==================================================

Choose an option:
1. Browse available concepts
2. Enter a custom concept
3. Generate lessons for multiple concepts
4. Exit

Enter your choice (1-4): 1

=== Available Math Concepts ===

Elementary:
  Arithmetic: Addition, Subtraction, Multiplication, Division, Fractions, Decimals
  Geometry: Shapes, Perimeter, Area, Symmetry
  ...

Enter a concept name or part of it:
Search: quadratic

Found 1 matching concepts:
1. Quadratic Equations

🎯 Generating lesson for: 'Quadratic Equations'
--------------------------------------------------
📝 Step 1: Generating lesson content with Gemini AI...
✅ Content saved to lesson_content_quadratic_equations.json
...
🎉 SUCCESS! Final video created: final_lesson_quadratic_equations.mp4
```

## 📁 Project Structure

```
musical-math-teacher/
├── main.py                    # Main application entry point
├── generate_content.py        # Gemini AI content generation
├── music.py                  # ElevenLabs voice generation
├── combiner.py              # FFmpeg video/audio combining
├── musical_math_lesson.py   # Manim animation scenes
├── requirements.txt         # Python dependencies
├── .env.template           # Environment variables template
├── README.md              # This file
├── media/                 # Generated videos (created by Manim)
├── lesson_content_*.json  # Generated lesson data
├── voiceover_*.mp3       # Generated audio files
└── final_lesson_*.mp4    # Final output videos
```

## 🔧 Configuration Options

### Video Quality Settings

In `main.py`, you can adjust video quality:

- `-ql`: Low quality (480p, fast rendering)
- `-qm`: Medium quality (720p, moderate rendering)
- `-qh`: High quality (1080p, slow rendering)

### Voice Settings

In `music.py`, you can change:

- **Voice**: "Rachel", "Daniel", "Bella", etc.
- **Model**: "eleven_multilingual_v2", "eleven_monolingual_v1"

### Animation Themes

The Manim scenes automatically adjust colors based on difficulty:

- **Beginner**: Green theme
- **Intermediate**: Blue theme
- **Advanced**: Purple theme

## 🐛 Troubleshooting

### Common Issues

1. **FFmpeg not found**

   ```
   ❌ FFmpeg not found. Please install FFmpeg and add it to PATH
   ```

   **Solution**: Install FFmpeg from [official website](https://ffmpeg.org/download.html)

2. **Manim not found**

   ```
   ❌ Manim not found. Please install with: pip install manim
   ```

   **Solution**: Run `pip install manim` in your virtual environment

3. **API Key errors**

   ```
   ❌ GEMINI_API_KEY not found in .env file
   ```

   **Solution**: Check your `.env` file has the correct API keys

4. **Video rendering fails**
   - Check if you have enough disk space
   - Try using `-ql` (low quality) for faster rendering
   - Ensure no other process is using the output files

### Performance Tips

- Use **low quality** (`-ql`) for testing and development
- Generate **high quality** (`-qh`) only for final videos
- Close other applications to free up memory during rendering
- Consider generating videos in batches during off-peak hours

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Manim Community** for the amazing animation library
- **Google AI** for Gemini API
- **ElevenLabs** for voice synthesis
- **OpenAI** for inspiration from educational AI tools

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all dependencies are correctly installed
3. Verify your API keys are valid
4. Open an issue on GitHub with:
   - Error messages
   - Your OS and Python version
   - Steps to reproduce the issue

---

**Happy Learning! 🎓✨**
