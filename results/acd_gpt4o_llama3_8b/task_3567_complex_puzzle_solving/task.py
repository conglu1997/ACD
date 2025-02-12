class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "123->234, 345->456, 567->678, 789->?"},
            "2": {"puzzle": "AB1->BC2, CD3->DE4, EF5->FG6, GH7->?"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following puzzle based on the given patterns and rules. Identify the missing sequence or element.

Puzzle: {t["puzzle"]}

Provide your answer as a plain text string in the following format:

Answer: [Your answer here]

Example:
For the puzzle '123->234, 345->456, 567->678, 789->?', a suitable answer could be '890'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answer should logically follow the given pattern.",
            "The answer should be a valid solution to the puzzle.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
