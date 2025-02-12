from typing import Dict

class TaskFamily:
    @staticmethod
    def get_tasks() -> Dict[str, Dict]:
        return {
            "1": {
                "puzzle_type": "completion",
                "pattern_sequence": [[1, 2, 3], [2, 3, 4], [3, 4, None]],
                "answer": [4, 5, 6]
            },
            "2": {
                "puzzle_type": "generation",
                "pattern_sequence": [[1, 1, 2], [2, 3, 5], [3, 6, 9]],
                "next_sequence": [4, None, None]
            }
        }

    @staticmethod
    def get_instructions(t: Dict) -> str:
        if t['puzzle_type'] == 'completion':
            return f"""You are provided with a sequence of geometric patterns. Your task is to determine the missing element in the sequence based on the given patterns. Provide your answer as a sequence of numbers.

Pattern Sequence: {t['pattern_sequence']}

Submit your response as a plain text string in the following format:

Answer: [your sequence here]
"""
        elif t['puzzle_type'] == 'generation':
            return f"""You are provided with a sequence of geometric patterns. Your task is to generate the next pattern in the sequence based on the given patterns. Provide your answer as a sequence of numbers.

Pattern Sequence: {t['pattern_sequence']}

Submit your response as a plain text string in the following format:

Next Sequence: [your generated sequence here]
"""

    @staticmethod
    def score(t: Dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle_type'] == 'completion':
            validation_criteria = [
                f"The answer should be {t['answer']}.",
                "The sequence should logically follow the given patterns."
            ]
        elif t['puzzle_type'] == 'generation':
            validation_criteria = [
                "The next sequence should logically follow the given patterns.",
                "The generated sequence should be coherent and consistent with the previous patterns."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
