class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"key": "C Major", "tempo": "120 BPM", "structure": "AABB"},
            "2": {"key": "G Minor", "tempo": "90 BPM", "structure": "ABAB"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a short piece of music based on the following guidelines:

Key: {t['key']}
Tempo: {t['tempo']}
Structure: {t['structure']}

Your composition should be at least 16 bars long and follow the given structure. Submit your composition as a plain text string in the following format:

Composition: [Your music composition in standard musical notation, e.g., ABC notation]

Note: Ensure your composition is clearly formatted and adheres strictly to the given key, tempo, and structure."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should adhere to the given key.",
            "The tempo should be consistent with the specified BPM.",
            "The structure should follow the specified format (e.g., AABB or ABAB).",
            "The composition should be at least 16 bars long.",
            "The musical notation should be clear and correctly formatted."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
