class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraint": "Write a short story (200-300 words) where every sentence starts with the next letter of the alphabet, starting from 'A'."},
            "2": {"constraint": "Write a short story (200-300 words) without using the letter 'e'."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a creative short story based on the following constraint:

{t["constraint"]}

Ensure your story is coherent, engaging, and adheres strictly to the given constraint. Provide your response in plain text format. The story should be between 200 and 300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["constraint"].startswith("Write a short story where every sentence starts with the next letter of the alphabet"):
            criteria = [
                "The story should have every sentence starting with the next letter of the alphabet, starting from 'A'.",
                "The story should be between 200 and 300 words.",
                "The story should be coherent and engaging."
            ]
        elif t["constraint"].startswith("Write a short story without using the letter 'e'"):
            criteria = [
                "The story should not contain the letter 'e'.",
                "The story should be between 200 and 300 words.",
                "The story should be coherent and engaging."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
