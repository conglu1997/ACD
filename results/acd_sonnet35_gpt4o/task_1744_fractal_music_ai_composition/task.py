import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            "Baroque",
            "Classical",
            "Romantic",
            "Impressionist",
            "Jazz",
            "Minimalist"
        ]
        fractal_types = [
            "Mandelbrot set",
            "Julia set",
            "Sierpinski triangle",
            "Koch snowflake",
            "Lyapunov fractal"
        ]
        return {
            "1": {"style": random.choice(musical_styles), "fractal": random.choice(fractal_types)},
            "2": {"style": random.choice(musical_styles), "fractal": random.choice(fractal_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and generate music based on fractal mathematics, then use it to compose a piece in the {t['style']} style using principles from the {t['fractal']}. Your response should include:

1. AI System Design (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system incorporates fractal mathematics into music analysis and generation.
   c) Detail how your system learns and applies the characteristics of the specified musical style.
   d) Discuss any novel approaches or technologies your system employs.

2. Fractal Music Analysis (250-300 words):
   a) Explain how the {t['fractal']} can be applied to music composition.
   b) Describe the mathematical principles your system uses to translate fractal patterns into musical elements (e.g., melody, harmony, rhythm).
   c) Discuss how your system balances mathematical precision with musical aesthetics.

3. Style Adaptation (200-250 words):
   a) Outline how your AI system identifies and incorporates key features of the {t['style']} style.
   b) Explain any challenges in combining fractal-based composition with this particular style.
   c) Describe how your system ensures the generated music remains recognizably within the specified style.

4. Composition Process (250-300 words):
   a) Provide a step-by-step explanation of how your AI system would compose a piece using the {t['fractal']} and in the {t['style']} style.
   b) Include at least one specific musical example (you can describe it in words, no need for actual notation).
   c) Explain how your system handles aspects like musical form, development, and coherence.

5. Evaluation and Refinement (200-250 words):
   a) Propose methods for evaluating the quality and style-appropriateness of the AI-generated compositions.
   b) Discuss how your system could learn and improve from feedback.
   c) Suggest potential applications of your AI system in music education, composition, or music theory research.

Ensure your response demonstrates a deep understanding of music theory, fractal mathematics, and artificial intelligence. Use appropriate terminology from all fields and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and musical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, fractal mathematics, and artificial intelligence.",
            "The AI system design is comprehensive, innovative, and plausibly integrates fractal mathematics with music generation.",
            "The explanation of how the specified fractal type is applied to music composition is clear and mathematically sound.",
            "The approach to adapting the fractal-based composition to the given musical style is well-reasoned and demonstrates knowledge of the style's characteristics.",
            "The composition process is explained in detail and includes a specific, plausible musical example described in words.",
            "The proposed evaluation methods and potential applications are thoughtful and relevant.",
            "The response follows the specified format with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
