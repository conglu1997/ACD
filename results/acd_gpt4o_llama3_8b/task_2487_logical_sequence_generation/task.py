class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sequence": [3, 9, 27, 81],
                "rule": "Each number is three times the previous one."
            },
            "2": {
                "sequence": [2, 5, 10, 17, 26],
                "rule": "The difference between consecutive numbers increases by 2 each time."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "You will be given a logical sequence and a rule that defines the pattern of the sequence. Your task is to continue the sequence by generating the next three elements that follow the given rule."
        instructions += f"\nSequence: {t['sequence']}"
        instructions += f"\nRule: {t['rule']}"
        instructions += "\nSubmit your response as a plain text string containing only the next three elements, separated by commas."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should contain the correct next three elements of the sequence, based on the given rule.",
            "The elements should be separated by commas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
