class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "length": 26,
                "theme": "a day in the life of a detective"
            },
            "2": {
                "length": 26,
                "theme": "an unexpected journey"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        length = t["length"]
        theme = t["theme"]
        instructions = f"""Your task is to write a short story consisting of {length} sentences. Each sentence should start with a sequential letter of the alphabet, beginning with 'A' and ending with 'Z'. The story should adhere to the following theme: {theme}.

Ensure that the story is coherent, creative, and follows the alphabetical constraint throughout. Provide your story in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Each sentence must start with the correct sequential letter of the alphabet.",
            "The story must adhere to the given theme.",
            "The story must be coherent and creative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
