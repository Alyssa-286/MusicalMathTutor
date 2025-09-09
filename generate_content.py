import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_math_lesson(concept, grade_level="middle school"):
    """
    Generate comprehensive math lesson content for various concepts
    """
    
    prompt = f"""
    Create a comprehensive math lesson for the concept: "{concept}" at {grade_level} level.
    
    Return a JSON object with the following structure:
    {{
        "title": "Engaging title for the lesson",
        "concept": "{concept}",
        "grade_level": "{grade_level}",
        "narrator_script": "A clear, engaging explanation of the concept (2-3 minutes worth of content)",
        "lyrics": "A catchy song/rap about the concept that helps remember key points",
        "key_points": ["point1", "point2", "point3"],
        "examples": [
            {{"problem": "example problem", "solution": "step by step solution", "visual_cue": "description for animation"}},
            {{"problem": "another example", "solution": "step by step solution", "visual_cue": "description for animation"}}
        ],
        "manim_commands": [
            "Create title animation",
            "Show definition with key terms highlighted",
            "Animate first example with step-by-step breakdown",
            "Display formula or key concept visually",
            "Animate second example",
            "Show summary with key points",
            "End with practice problems"
        ],
        "difficulty": "beginner/intermediate/advanced",
        "duration_minutes": 3,
        "practice_problems": [
            {{"question": "practice question 1", "answer": "answer with explanation"}},
            {{"question": "practice question 2", "answer": "answer with explanation"}}
        ]
    }}
    
    Make sure the content is:
    - Age-appropriate for {grade_level}
    - Engaging and fun
    - Mathematically accurate
    - Includes real-world applications
    - Has memorable elements (rhymes, patterns, etc.)
    
    IMPORTANT: Return ONLY the JSON object, no other text.
    """
    
    try:
        response = model.generate_content(prompt)
        
        # Clean the response to ensure it's valid JSON
        content = response.text.strip()
        if content.startswith('```json'):
            content = content[7:-3]
        elif content.startswith('```'):
            content = content[3:-3]
        
        # Validate JSON
        lesson_data = json.loads(content)
        return json.dumps(lesson_data, indent=2)
        
    except Exception as e:
        print(f"Error generating lesson with Gemini: {e}")
        # Return fallback content
        fallback = {
            "title": f"Introduction to {concept}",
            "concept": concept,
            "grade_level": grade_level,
            "narrator_script": f"Today we're learning about {concept}. This is an important mathematical concept that helps us solve many real-world problems.",
            "lyrics": f"🎵 {concept}, {concept}, let's learn it today! Mathematical thinking in a fun, engaging way! 🎵",
            "key_points": [f"Understanding {concept}", "Key properties", "Real-world applications"],
            "examples": [
                {"problem": f"Basic {concept} example", "solution": "Step by step solution", "visual_cue": "Show problem visually"}
            ],
            "manim_commands": ["Create title", "Show definition", "Animate example", "Summary"],
            "difficulty": "beginner",
            "duration_minutes": 2,
            "practice_problems": [
                {"question": f"Practice with {concept}", "answer": "Sample answer"}
            ]
        }
        return json.dumps(fallback, indent=2)

def get_math_concepts_by_category():
    """
    Return a dictionary of math concepts organized by category and grade level
    """
    concepts = {
        "Elementary": {
            "Arithmetic": ["Addition", "Subtraction", "Multiplication", "Division", "Fractions", "Decimals"],
            "Geometry": ["Shapes", "Perimeter", "Area", "Symmetry"],
            "Measurement": ["Time", "Money", "Length", "Weight", "Volume"]
        },
        "Middle School": {
            "Algebra": ["Linear Equations", "Inequalities", "Exponents", "Polynomials", "Factoring"],
            "Geometry": ["Triangles", "Circles", "Pythagorean Theorem", "Surface Area", "Volume"],
            "Statistics": ["Mean, Median, Mode", "Probability", "Data Analysis", "Graphs and Charts"],
            "Number Theory": ["Prime Numbers", "Greatest Common Factor", "Least Common Multiple", "Ratios", "Proportions"]
        },
        "High School": {
            "Algebra II": ["Quadratic Equations", "Logarithms", "Complex Numbers", "Sequences and Series"],
            "Geometry": ["Trigonometry", "Coordinate Geometry", "Transformations", "Proofs"],
            "Calculus": ["Limits", "Derivatives", "Integrals", "Applications of Calculus"],
            "Statistics": ["Standard Deviation", "Normal Distribution", "Hypothesis Testing", "Correlation"]
        }
    }
    return concepts

def list_available_concepts():
    """
    Display all available math concepts organized by category
    """
    concepts = get_math_concepts_by_category()
    print("\n=== Available Math Concepts ===")
    for grade, categories in concepts.items():
        print(f"\n{grade}:")
        for category, concept_list in categories.items():
            print(f"  {category}: {', '.join(concept_list)}")
    
    # Flatten all concepts for easy selection
    all_concepts = []
    for grade, categories in concepts.items():
        for category, concept_list in categories.items():
            all_concepts.extend(concept_list)
    
    return all_concepts

def suggest_related_concepts(concept):
    """
    Suggest related math concepts based on the input
    """
    concept_relationships = {
        "Addition": ["Subtraction", "Multiplication", "Fractions"],
        "Algebra": ["Linear Equations", "Quadratic Equations", "Polynomials"],
        "Geometry": ["Area", "Perimeter", "Volume", "Pythagorean Theorem"],
        "Calculus": ["Limits", "Derivatives", "Integrals"],
        "Statistics": ["Probability", "Mean, Median, Mode", "Standard Deviation"]
    }
    
    suggestions = []
    for key, related in concept_relationships.items():
        if key.lower() in concept.lower() or concept.lower() in key.lower():
            suggestions.extend(related)
    
    return suggestions[:3]  # Return top 3 suggestions

if __name__ == "__main__":
    # Test the function
    test_concept = "Quadratic Equations"
    result = generate_math_lesson(test_concept)
    print(f"Generated lesson for: {test_concept}")
    print(result)