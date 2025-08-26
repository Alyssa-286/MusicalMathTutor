from manim import *
import json

# Placeholder data from your AI script
SAMPLE_DATA = {
    "narrator_script": "The Pythagorean Theorem states that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.",
    "lyrics": "A squared plus B squared, equals C squared! It's a right triangle fact, so it's never abstract!",
    "manim_commands": [
        "show_triangle",
        "label_sides",
        "show_formula"
    ]
}

class MusicalMathLesson(Scene):
    def construct(self):
        # Load the content
        script_data = SAMPLE_DATA
        
        # 1. Animate the narrator script
        # Set a fixed width to ensure it fits, and position it at the top
        narration_text = MarkupText(script_data['narrator_script']).set_width(config.frame_width - 1).to_edge(UP)
        self.play(Write(narration_text))
        self.wait(2)
        
        # 2. Animate based on AI commands, with careful placement
        if "show_triangle" in script_data['manim_commands']:
            triangle = Polygon(
                [0, 0, 0],
                [3, 0, 0],
                [0, 2.5, 0],
                color=BLUE
            ).to_edge(LEFT, buff=1) # Position the triangle to the left with a buffer
            self.play(Create(triangle))
            self.wait(1)
        
        if "label_sides" in script_data['manim_commands']:
            # Position the labels relative to the triangle
            a = Tex("a").next_to(triangle, RIGHT, buff=0.2)
            b = Tex("b").next_to(triangle, UP, buff=0.2)
            c = Tex("c").next_to(triangle, UR, buff=0.2)
            
            # Combine them into a VGroup for easier animation
            labels = VGroup(a, b, c)
            self.play(Write(labels))
            self.wait(1)
        
        if "show_formula" in script_data['manim_commands']:
            # Position the formula below the triangle, with sufficient space
            formula = MathTex("a^2 + b^2 = c^2").next_to(triangle, DOWN, buff=1)
            self.play(Write(formula))
            self.wait(2)
            
        # 3. Animate the song lyrics
        lyrics_text = Text(script_data['lyrics']).set_width(config.frame_width - 1).to_edge(DOWN)
        self.play(FadeOut(formula), FadeIn(lyrics_text))
        self.wait(3)
        
        # 4. Clean up
        self.play(FadeOut(VGroup(narration_text, triangle, labels, lyrics_text)))
        self.wait(1)