class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"elements": ["a time-traveling detective", "a hidden ancient artifact", "a futuristic city"]},
            "2": {"elements": ["a talking animal", "a mysterious forest", "a magical portal"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a coherent and engaging short story based on the following elements:

Elements: {', '.join(t['elements'])}

Ensure your story integrates all the given elements in a meaningful way, maintains a consistent narrative, and is engaging for the reader. Your response should be in plain text format and be between 500 to 1000 words. Format your response as follows:

Story: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be between 500 to 1000 words.",
            "The story should integrate all the given elements in a meaningful way.",
            "The story should maintain a consistent and coherent narrative.",
            "The story should be engaging for the reader."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
