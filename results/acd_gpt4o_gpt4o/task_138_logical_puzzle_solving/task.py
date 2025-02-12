class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "You have three boxes, one labeled 'Apples', one labeled 'Oranges', and one labeled 'Mixed'. Each box is incorrectly labeled. You can only take out one fruit from one box to determine the correct labels. How would you do it?"
            },
            "2": {
                "puzzle": "You are in a room with two doors. One door leads to freedom, and the other door leads to a deadly trap. There are two guards, one in front of each door. One guard always tells the truth, and the other always lies. You can ask one guard one question to determine which door leads to freedom. What do you ask?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Solve the following logical puzzle: {t['puzzle']}\n"
            "Provide your solution in plain text format, clearly explaining your reasoning and steps."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
