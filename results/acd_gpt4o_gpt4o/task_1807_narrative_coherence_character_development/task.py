class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A young detective in a small town discovers a mysterious artifact that changes their life."},
            "2": {"prompt": "A retired astronaut encounters a strange signal from space, leading to an unexpected adventure."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a short story based on the following prompt:

Prompt: {t['prompt']}

Ensure that your story has a coherent narrative structure, well-developed characters, and an engaging plot. Your story should be original and creative. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should follow a coherent narrative structure.", "The characters should be well-developed and consistent.", "The plot should be engaging and original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
