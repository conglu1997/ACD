class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "love", "length": "4 lines", "melody_structure": "AABA"},
            "2": {"theme": "nature", "length": "4 lines", "melody_structure": "ABAB"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Compose an original simple song based on the following requirements:\n"
            f"Theme: {t['theme']}\n"
            f"Length: {t['length']}\n"
            f"Melody Structure: {t['melody_structure']}\n\n"
            "Provide both the lyrics and a simple notation for the melody. The notation should use letters (A-G) to represent musical notes, and you can indicate the rhythm with spaces or dashes. For example, a simple melody could be 'A B C - A B C - D E F G'. Ensure the melody follows the given structure, and the lyrics adhere to the provided theme. Additionally, include a brief justification explaining how the melody follows the given structure."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The lyrics should adhere to the provided theme.",
            "The melody should follow the given structure (e.g., AABA or ABAB).",
            "The notation should be clear and understandable.",
            "The lyrics and melody must be original.",
            "The melody notation should use letters A-G and indicate rhythm clearly.",
            "The submission should include a brief justification explaining how the melody follows the given structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0