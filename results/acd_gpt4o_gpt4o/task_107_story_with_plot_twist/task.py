class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a detective who solves a crime, but the twist is that the detective is actually the criminal."},
            "2": {"prompt": "Write a short story about a seemingly normal day at the office, but the twist is that everyone in the office is a robot."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a short story based on the given prompt. Make sure to incorporate the specific plot twist provided in the prompt.

Prompt: {t['prompt']}

The story should be coherent, engaging, and effectively integrate the plot twist. Ensure that the twist is surprising yet fits naturally within the narrative. Provide your story in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and engaging.",
            "The plot twist should be effectively integrated and surprising.",
            "The twist should fit naturally within the narrative.",
            "The story should be written in clear and grammatically correct language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
