import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "language": "Arabic",
                "feature": "root-pattern morphology",
                "math_field": "linear algebra"
            },
            {
                "language": "Mandarin Chinese",
                "feature": "tonal system",
                "math_field": "complex analysis"
            }
        ]
        return {
            "1": random.choice(languages),
            "2": random.choice(languages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel mathematical notation system based on the linguistic principles of {t['language']}, specifically its {t['feature']}. Then, use this notation to solve a complex problem in {t['math_field']}. Follow these steps:

1. Linguistic Analysis (150-200 words):
   Briefly explain the key features of {t['language']}'s {t['feature']} and how it structures information.

2. Notation System Design (200-250 words):
   a) Describe your mathematical notation system, explaining how it incorporates the linguistic feature.
   b) Provide examples of how basic mathematical operations are represented in your system.
   c) Explain how your system handles complex mathematical concepts specific to {t['math_field']}.

3. Problem Solving (250-300 words):
   a) State a complex problem in {t['math_field']} using standard mathematical notation.
   b) Solve this problem step-by-step using your new notation system. Format your solution as follows:
      Step 1: [Your notation] (Explanation)
      Step 2: [Your notation] (Explanation)
      ...
   c) Explain each step of your solution, highlighting how the linguistic-based notation provides insights or advantages.

4. Comparative Analysis (150-200 words):
   Compare your notation system to standard mathematical notation, discussing potential advantages and limitations for problem-solving in {t['math_field']}.

5. Potential Applications (100-150 words):
   Propose two potential applications of your linguistic-based mathematical notation system in scientific or technological domains.

Ensure your response demonstrates a deep understanding of both the linguistic principles and the mathematical concepts involved. Be creative in your approach while maintaining mathematical rigor and logical consistency."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The mathematical notation system clearly incorporates the specified linguistic feature.",
            "The solution to the complex mathematical problem is correct and well-explained using the new notation.",
            "The comparative analysis demonstrates a deep understanding of both standard and new notation systems.",
            "The response shows creativity and interdisciplinary knowledge application."
        ]
        # The eval_with_llm_judge function uses GPT-4 to evaluate the submission based on the instructions and criteria
        # It returns True if the submission meets the criteria, False otherwise
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
