class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dialect": "Scottish", "sentence": "I am going to the store to buy some groceries."},
            "2": {"dialect": "Southern American English", "sentence": "He is working hard on the farm.", "direction": "to_standard"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dialect = t["dialect"]
        sentence = t["sentence"]
        direction = t.get("direction", "to_dialect")
        if direction == "to_standard":
            return f"Translate the following {dialect} dialect sentence into standard English: '{sentence}'"
        else:
            return f"Translate the following sentence into {dialect} dialect: '{sentence}'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translation should accurately reflect the given dialect.", "The translated sentence should preserve the original meaning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
