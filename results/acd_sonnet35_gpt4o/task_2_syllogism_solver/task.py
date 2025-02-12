import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        syllogisms = [
            {
                'premise1': 'All mammals are warm-blooded',
                'premise2': 'All dogs are mammals',
                'valid_conclusion': 'All dogs are warm-blooded'
            },
            {
                'premise1': 'No reptiles are warm-blooded',
                'premise2': 'All snakes are reptiles',
                'valid_conclusion': 'No snakes are warm-blooded'
            }
        ]
        return {str(i+1): syllogism for i, syllogism in enumerate(syllogisms)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following syllogism:

Premise 1: {t['premise1']}
Premise 2: {t['premise2']}

Based on these premises, determine the valid conclusion, if any. If there is no valid conclusion, state 'No valid conclusion'. Provide your answer in the following format:

Conclusion: [Your conclusion here]

Explain your reasoning briefly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conclusion should be logically equivalent to '{t['valid_conclusion']}'.",
            "The response should include a clear statement of the conclusion.",
            "The explanation should demonstrate understanding of the logical relationship between the premises and the conclusion."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
