class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "mathematical_concept": "Fibonacci sequence",
                "musical_element": "rhythm"
            },
            "2": {
                "mathematical_concept": "fractal geometry",
                "musical_element": "harmony"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a novel musical system based on the mathematical concept of {t['mathematical_concept']}, focusing on the musical element of {t['musical_element']}. Then, compose and evaluate a short piece using this system. Your response should include the following sections:

1. System Design (200-250 words):
   a) Explain how you will apply {t['mathematical_concept']} to {t['musical_element']} in your musical system.
   b) Describe the key components and rules of your system.
   c) Discuss how this system differs from traditional Western music theory.

2. Composition (150-200 words):
   a) Compose a short musical piece (or section of a piece) using your system.
   b) Provide a notated representation of your composition (use ASCII or Unicode characters if needed).
   c) Explain how your composition demonstrates the principles of your system.

3. Analysis (200-250 words):
   a) Analyze the potential emotional or perceptual effects of music created with your system.
   b) Compare and contrast these effects with those typically associated with traditional Western music.
   c) Discuss any challenges or limitations you foresee in composing or performing music with this system.

4. Interdisciplinary Connections (150-200 words):
   a) Explain how your musical system might relate to or inspire developments in another field (e.g., visual arts, architecture, computer science).
   b) Propose an experiment or study that could further explore the cognitive or emotional impacts of music created with your system.

Ensure your response demonstrates a deep understanding of both {t['mathematical_concept']} and music theory, while showcasing creativity in system design and composition. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and creative application of the given mathematical concept to the specified musical element.",
            "The musical system design is coherent, innovative, and well-explained.",
            "The composition effectively demonstrates the principles of the created musical system.",
            "The analysis shows insightful consideration of the emotional and perceptual effects of the new musical system.",
            "The interdisciplinary connections are thoughtful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
