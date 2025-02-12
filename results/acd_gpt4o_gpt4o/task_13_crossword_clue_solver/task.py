class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clue": "A place where you might find books (6 letters)",
                "answer_length": 6
            },
            "2": {
                "clue": "A festive occasion (5 letters)",
                "answer_length": 5
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        clue = t["clue"]
        answer_length = t["answer_length"]
        instructions = f"""Your task is to solve the following crossword clue and provide the correct word.

Clue: {clue}

The answer should be {answer_length} letters long. Provide your answer as a single word in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The answer must be {t['answer_length']} letters long.",
            "The answer must correctly solve the given clue."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
