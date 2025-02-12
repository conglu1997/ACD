class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"musical_notation": "C4 D4 E4 F4 G4"},
            "2": {"musical_notation": "G3 A3 B3 C4 D4 E4 F#4 G4"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given musical notation and generate a corresponding textual description of the musical piece. Here is the musical notation: '{t["musical_notation"]}'. Provide your response in the following format:

1. Musical Notation: [the provided musical notation]
2. Interpretation: [your detailed textual description of the musical piece]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly interpret the given musical notation.",
            "The submission should provide a detailed textual description of the musical piece.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
