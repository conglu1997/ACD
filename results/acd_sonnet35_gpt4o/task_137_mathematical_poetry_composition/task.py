import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "math_concept": "Fibonacci sequence",
                "poetic_form": "Haiku sequence",
                "theme": "Growth in nature"
            },
            {
                "math_concept": "Prime numbers",
                "poetic_form": "Sonnet",
                "theme": "Solitude and uniqueness"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a poem that incorporates the mathematical concept of {t['math_concept']} and follows the structure of a {t['poetic_form']}. The theme of your poem should be {t['theme']}.

Your task:

1. Create a poem that adheres to the following rules:
   a) The poem must be in the form of a {t['poetic_form']}.
   b) The content must relate to the theme of {t['theme']}.
   c) The poem must incorporate the mathematical concept of {t['math_concept']} in both its structure and content.

2. Explain how your poem incorporates the mathematical concept (2-3 sentences).

3. Analyze how the mathematical structure enhances or interacts with the poetic theme (2-3 sentences).

Ensure your poem is creative, mathematically accurate, and poetically sound. The explanation and analysis should demonstrate a clear understanding of both the mathematical concept and poetic techniques."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The poem adheres to the structure of a {t['poetic_form']}.",
            f"The poem incorporates the mathematical concept of {t['math_concept']} in both structure and content.",
            f"The poem's theme relates to {t['theme']}.",
            "The explanation clearly describes how the mathematical concept is incorporated into the poem.",
            "The analysis demonstrates how the mathematical structure enhances or interacts with the poetic theme.",
            "The poem is creative and poetically sound while maintaining mathematical accuracy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
