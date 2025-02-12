class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sequence": ["⬜", "⬛", "⬜", "⬛", "⬜", "?"],
                "options": ["⬛", "⬜", "▲", "■"]
            },
            "2": {
                "sequence": ["▲", "▲", "△", "▲", "▲", "?"],
                "options": ["△", "▲", "■", "○"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the missing element in the following sequence of shapes or symbols by determining the underlying pattern. Choose the correct option from the given list.

Sequence: {t['sequence']}

Options: {t['options']}

Submit your response as a plain text string in the format:

Answer: [Your Answer]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answers = {
            "1": "⬛",
            "2": "△"
        }
        task_id = [k for k, v in TaskFamily.get_tasks().items() if v == t][0]
        criteria = [f"The answer should be {correct_answers[task_id]}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
