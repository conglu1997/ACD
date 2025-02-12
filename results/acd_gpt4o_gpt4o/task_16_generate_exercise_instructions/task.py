class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "exercise": "push-up"
            },
            "2": {
                "exercise": "squat"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        exercise = t["exercise"]
        return f"""Your task is to generate detailed instructions for performing the following exercise: {exercise}.

The instructions should include the following components:
1. Starting position
2. Step-by-step guide on how to perform the exercise
3. Common mistakes to avoid
4. Tips for beginners

Ensure that the instructions are clear, concise, and easy to follow. Provide your instructions in plain text format, with each component clearly labeled."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should correctly describe the starting position.",
            "The step-by-step guide should be accurate and easy to follow.",
            "The common mistakes section should mention at least two mistakes.",
            "The tips for beginners should provide helpful advice.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
