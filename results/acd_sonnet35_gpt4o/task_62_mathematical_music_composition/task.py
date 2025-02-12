import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "Fibonacci sequence",
            "Golden ratio",
            "Prime numbers",
            "Fractals"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "form"
        ]
        return {
            "1": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a short musical piece that incorporates the mathematical concept of {t['math_concept']} into its {t['musical_element']}. Your response should include:

1. A brief explanation of the chosen mathematical concept and how it relates to music (2-3 sentences)
2. A detailed description of your musical composition, explaining how you've incorporated the mathematical concept into the specified musical element (4-5 sentences)
3. An analysis of how this mathematical approach affects the overall structure and sound of the piece (3-4 sentences)
4. One potential challenge a performer might face when playing this piece, and a suggested solution (2-3 sentences)
5. A creative title for your composition that reflects both its mathematical and musical aspects

Ensure your composition is musically coherent while clearly demonstrating the application of the mathematical concept. Organize your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must explain the {t['math_concept']} concept and its relation to music.",
            f"The composition must incorporate the {t['math_concept']} into its {t['musical_element']}.",
            "The response must include a detailed description of the composition and its structure.",
            "The response must analyze how the mathematical approach affects the piece.",
            "The response must identify a potential performance challenge and suggest a solution.",
            "The composition must have a creative title reflecting both mathematical and musical aspects.",
            "The response must be organized with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
