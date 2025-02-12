class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"puzzle": "What comes next in the sequence: [🔺, 🔺🔺, 🔺🔺🔺, 🔻, 🔻🔻, 🔻🔻🔻, 🔺, 🔺🔺, ?]"},
            "2": {"puzzle": "Complete the pattern: [⚫, ⚫⚫, ⚫⚫⚫, ⚫⚫⚫⚫, ⚫⚫⚫⚫⚫, ?]"}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following visual-spatial puzzle by identifying the pattern and providing the next item in the sequence:

Puzzle: {t['puzzle']}

Provide your answer in plain text format as the next item in the sequence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly identify the next item in the sequence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
