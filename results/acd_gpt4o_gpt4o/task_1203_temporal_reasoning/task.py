class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": ["Alice wakes up", "Alice eats breakfast", "Alice goes to work", "Alice attends a meeting", "Alice goes to lunch", "Alice finishes her work", "Alice comes home", "Alice goes to bed"], "task": "What does Alice do after she attends a meeting?"},
            "2": {"sequence": ["The sun rises", "The morning begins", "People go to work", "The afternoon begins", "People have lunch", "The evening begins", "The sun sets", "The night begins", "People go to sleep"], "task": "What happens after the evening begins?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given sequence of events and determine the correct ordering or predict the next event in the sequence. Provide your response in the following format:

Response: [Your answer]

Sequence: {', '.join(t['sequence'])}
Task: {t['task']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify the next event in the sequence or answer the task question accurately.",
            "The response should be in the format 'Response: [Your answer]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
