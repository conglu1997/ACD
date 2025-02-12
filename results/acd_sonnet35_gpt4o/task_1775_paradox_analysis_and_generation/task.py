import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        paradoxes = [
            {
                "name": "The Liar's Paradox",
                "statement": "This statement is false."
            },
            {
                "name": "Russell's Paradox",
                "statement": "Consider the set of all sets that do not contain themselves. Does this set contain itself?"
            },
            {
                "name": "The Ship of Theseus",
                "statement": "If every part of a ship is replaced over time, is it still the same ship?"
            }
        ]
        return {str(i+1): paradox for i, paradox in enumerate(random.sample(paradoxes, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following paradox and then create a new, related paradox:

{t['name']}: {t['statement']}

Your response should include the following:

1. Paradox Analysis (200-250 words):
   a) Explain the logical structure of the paradox.
   b) Identify the key concepts or assumptions that lead to the paradoxical situation.
   c) Discuss any potential resolutions or interpretations of the paradox.

2. Related Concepts (100-150 words):
   a) Identify at least two related philosophical or logical concepts.
   b) Briefly explain how these concepts connect to the given paradox.

3. New Paradox Generation (200-250 words):
   a) Create a new paradox that uses similar logical principles or concepts.
   b) Clearly state your new paradox.
   c) Explain how it relates to or builds upon the original paradox.
   d) Discuss the logical structure of your new paradox.

4. Implications and Applications (150-200 words):
   a) Discuss potential implications of your new paradox for philosophy, logic, or cognitive science.
   b) Propose a practical application or thought experiment based on your paradox.

Ensure your response demonstrates a deep understanding of logical reasoning and creative problem-solving. Use clear and concise language, and structure your response with appropriate headings for each section.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the given paradox",
            "The analysis of the paradox is logically sound and well-explained",
            "The new paradox is original, well-formulated, and relates to the given paradox",
            "The implications and applications of the new paradox are insightful and well-reasoned",
            "The response is well-structured and adheres to the word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
