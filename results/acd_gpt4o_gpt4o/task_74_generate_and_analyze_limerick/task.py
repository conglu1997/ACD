class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a limerick about a cat who loves to dance."},
            "2": {"prompt": "Write a limerick about a scientist who makes a funny mistake."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Your task is to generate a limerick based on the following prompt: " + t["prompt"] + " Ensure your limerick follows the traditional structure: five lines with an AABBA rhyme scheme and a humorous or whimsical theme. Provide your limerick in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The limerick should have five lines.",
            "The rhyme scheme should follow AABBA.",
            "The limerick should have a humorous or whimsical theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
