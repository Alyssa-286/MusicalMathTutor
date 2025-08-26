import openai

client = openai.OpenAI(api_key="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")

def generate_math_lesson(concept):
    prompt = f"""
    You are a musical math teacher. Your task is to create a lesson for the concept of '{concept}'.
    Provide the following in a structured JSON format:
    1. "narrator_script": A clear, concise explanation of the concept.
    2. "lyrics": Song lyrics that make the concept easy to remember.
    3. "manim_commands": A list of visual cues or Manim commands to animate the script and lyrics.

    Example for 'Pythagorean Theorem':
    "narrator_script": "The Pythagorean Theorem is a fundamental rule in geometry. It states that in a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. We write this as $a^2 + b^2 = c^2$."
    ...
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    # Parse and return the JSON response
    return response.choices[0].message.content