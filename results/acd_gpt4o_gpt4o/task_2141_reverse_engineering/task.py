class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "output": "The encoded message is: 72 101 108 108 111",
                "hint": "The encoding method is ASCII values of characters."
            },
            "2": {
                "output": "The resulting sequence is: 1, 1, 2, 3, 5, 8, 13",
                "hint": "This is a famous mathematical sequence."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to reverse engineer the given output to deduce the original input or process that produced it.\n\nOutput: {t['output']}\nHint: {t['hint']}\n\nProvide a clear explanation of your deduction process and the original input or process. Your response should be formatted as follows:\n\nOriginal Input/Process: [Your answer]\nExplanation: [Your explanation]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The original input or process should be correctly deduced based on the given output and hint.",
            "The explanation should be clear and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
