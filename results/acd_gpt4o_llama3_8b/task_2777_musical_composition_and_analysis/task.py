class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "joyful", "constraints": "Use a major scale and include at least one modulation."},
            "2": {"theme": "melancholic", "constraints": "Use a minor scale and include a counter-melody."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a musical composition based on the following theme and constraints: Theme: '{t['theme']}'. Constraints: {t['constraints']}. The composition should be at least 16 bars long and written in plain text notation (e.g., C-D-E-F-G-A-B for a simple scale). Include a brief explanation of how you adhered to the theme and constraints. Submit your response in the following format: Composition: [Your composition in plain text notation] Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The composition should adhere to the given theme and constraints.", "The composition should be at least 16 bars long.", "The composition should be written in plain text notation (e.g., C-D-E-F-G-A-B).", "The explanation should describe how the theme and constraints were met."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
