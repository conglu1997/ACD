class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "analogy": "Hand is to glove as foot is to _____."
            },
            "2": {
                "analogy": "Bird is to nest as bee is to _____."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following analogy by filling in the blank with the most appropriate word:

{t['analogy']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
