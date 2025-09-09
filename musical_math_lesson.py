# File: musical_math_lesson.py

from manim import (
    Scene, VGroup, Text, Paragraph, Star, Dot,
    UP, DOWN, LEFT, ORIGIN, PI,
    Write, FadeIn, FadeOut, DrawBorderThenFill, LaggedStart, GrowFromCenter, Rotate,
    # --- CORRECTED COLORS ---
    # Replaced non-existent colors with valid Manim shades like GREEN_B
    GREEN, GREEN_B, YELLOW, BLUE, BLUE_B, ORANGE, PURPLE, PURPLE_B, RED, WHITE,
    config
)
import json
import numpy as np
import random

try:
    with open('lesson_content.json', 'r') as f:
        script_data = json.load(f)
except FileNotFoundError:
    print("Error: lesson_content.json not found. Please run main.py first.")
    script_data = {
        "title": "Math Lesson", "concept": "Error", "narrator_script": "Error.",
        "lyrics": "Error.", "key_points": [], "examples": [], "difficulty": "beginner"
    }

class MusicalMathLesson(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"
        difficulty = script_data.get('difficulty', 'beginner')
        
        # --- CORRECTED COLOR ASSIGNMENTS ---
        if difficulty == 'beginner':
            primary_color, secondary_color, accent_color = GREEN, GREEN_B, YELLOW
        elif difficulty == 'intermediate':
            primary_color, secondary_color, accent_color = BLUE, BLUE_B, ORANGE
        else:
            primary_color, secondary_color, accent_color = PURPLE, PURPLE_B, RED
        
        self.create_title_animation(primary_color, accent_color)
        self.introduce_concept(primary_color)
        self.display_key_points(primary_color)
        self.animate_examples(primary_color, secondary_color)
        self.musical_section(accent_color)
        self.create_summary(primary_color)
        self.create_end_screen(primary_color, accent_color)

    def create_title_animation(self, primary_color, accent_color):
        title = Text(script_data['title'], font_size=60, color=primary_color).to_edge(UP, buff=1)
        subtitle = Text(f"Learning: {script_data['concept']}", font_size=32, color=accent_color).next_to(title, DOWN)
        self.play(DrawBorderThenFill(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)
        self.play(FadeOut(title, shift=UP), FadeOut(subtitle, shift=UP))

    def introduce_concept(self, primary_color):
        title = Text("What are we learning?", font_size=40, color=primary_color).to_edge(UP, buff=1)
        narrator_text = script_data['narrator_script']
        intro_text = '. '.join(narrator_text.split('.')[:2]) + '.'
        explanation = Paragraph(intro_text, font_size=24, color=WHITE, width=config.frame_width - 2, alignment="center").next_to(title, DOWN, buff=1)
        self.play(Write(title))
        self.play(FadeIn(explanation, shift=UP))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(explanation))

    def display_key_points(self, primary_color):
        key_points = script_data.get('key_points', [])
        if not key_points: return
        title = Text("Key Points", font_size=48, color=primary_color).to_edge(UP, buff=1)
        self.play(Write(title))
        bullets = VGroup()
        for i, point in enumerate(key_points[:4]):
            bullet_text = Text(f"• {point}", font_size=28, color=WHITE)
            if i == 0:
                bullet_text.next_to(title, DOWN, buff=1.5)
            else:
                bullet_text.next_to(bullets[-1], DOWN, buff=0.5)
            bullets.add(bullet_text)

        for bullet in bullets:
            self.play(FadeIn(bullet, shift=LEFT))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(bullets))

    def animate_examples(self, primary_color, secondary_color):
        for i, example in enumerate(script_data.get('examples', [])[:2]):
            self.animate_single_example(example, primary_color, secondary_color, i + 1)

    def animate_single_example(self, example, primary_color, secondary_color, num):
        title = Text(f"Example {num}", font_size=40, color=primary_color).to_edge(UP, buff=0.5)
        problem = Text(example['problem'], font_size=32, color=WHITE).next_to(title, DOWN, buff=1)
        self.play(Write(title), FadeIn(problem, shift=UP))
        self.wait(1)
        solution_group = VGroup()
        for i, line in enumerate(example['solution'].split('\n')[:3]):
            if line.strip():
                step = Text(line.strip(), font_size=24, color=secondary_color)
                if i == 0:
                    step.next_to(problem, DOWN, buff=1)
                else:
                    step.next_to(solution_group[-1], DOWN, buff=0.3)
                solution_group.add(step)
        for step in solution_group: self.play(Write(step))
        checkmark = Text("✓", font_size=48, color=GREEN).next_to(solution_group, DOWN, buff=0.5)
        self.play(GrowFromCenter(checkmark))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(problem), FadeOut(solution_group), FadeOut(checkmark))

    def musical_section(self, accent_color):
        lyrics = script_data.get('lyrics', '')
        if not lyrics: return
        notes = VGroup(*[Text(s, font_size=40, color=accent_color).move_to([2.5 * np.cos(i*PI/4), 1.5 * np.sin(i*PI/4), 0]) for i, s in enumerate(["♪", "♫", "♬", "♩"]*2)])
        lyrics_text = Paragraph(lyrics[:200], font_size=28, color=WHITE, width=config.frame_width-2, alignment="center")
        self.play(LaggedStart(*[FadeIn(n) for n in notes], lag_ratio=0.2))
        self.play(FadeIn(lyrics_text, shift=UP))
        self.play(Rotate(notes, angle=2*PI, run_time=3))
        self.wait(1)
        self.play(FadeOut(notes), FadeOut(lyrics_text))

    def create_summary(self, primary_color):
        title = Text("What we learned:", font_size=40, color=primary_color).to_edge(UP, buff=1)
        items = VGroup()
        for i, point in enumerate(script_data.get('key_points', [])[:3]):
            item = Text(f"{i+1}. {point}", font_size=28, color=WHITE)
            if i == 0:
                item.next_to(title, DOWN, buff=1)
            else:
                item.next_to(items[-1], DOWN, buff=0.5)
            items.add(item)
        self.play(Write(title))
        self.play(LaggedStart(*[FadeIn(item, shift=LEFT) for item in items], lag_ratio=0.3))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(items))

    def create_end_screen(self, primary_color, accent_color):
        thank_you = Text("Great Job!", font_size=60, color=primary_color)
        keep_learning = Text("Keep exploring mathematics!", font_size=32, color=accent_color).next_to(thank_you, DOWN)
        self.play(DrawBorderThenFill(thank_you))
        self.play(FadeIn(keep_learning, shift=UP))
        self.wait(2)