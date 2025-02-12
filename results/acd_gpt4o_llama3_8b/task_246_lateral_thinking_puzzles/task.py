class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "A man is found dead in a desert. He is wearing only his underwear, and there are no footprints around him. There is an unopened package next to him. How did he die?"},
            "2": {"puzzle": "A man walks into a bar and asks the bartender for a glass of water. The bartender pulls out a gun and points it at him. The man says 'Thank you' and leaves. What happened?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following lateral thinking puzzle: {t['puzzle']}\nSubmit your answer as a short, logical, and coherent explanation."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should provide a logical and coherent explanation that solves the puzzle.", "The explanation should not be vague or overly broad."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
