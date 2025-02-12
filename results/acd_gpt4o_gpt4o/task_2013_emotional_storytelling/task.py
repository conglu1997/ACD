class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"emotion": "happiness", "prompt": "Write a short story about a surprise birthday party where everything goes perfectly."},
            "2": {"emotion": "fear", "prompt": "Write a short story about someone getting lost in a dark forest and encountering strange noises."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a short story that evokes a sense of {t['emotion']} based on the following prompt:

Prompt: {t['prompt']}

Your story should be engaging, well-structured, and clearly evoke the specified emotion. Ensure your narrative is coherent and emotionally resonant. The story should be between 200 and 300 words. Provide your story in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The story should evoke a sense of {t['emotion']}.", "The narrative should be engaging and well-structured.", "The story should be coherent and emotionally resonant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
