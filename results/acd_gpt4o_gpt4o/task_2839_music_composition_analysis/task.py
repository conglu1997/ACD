class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "compose", "theme": "tranquility", "constraints": "must be in a classical style, include a minimum of 16 bars, and use a 4/4 time signature."},
            "2": {"task": "analyze", "music": "C-D-E-F-G-A-B-C"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "compose":
            return f"Your task is to compose a piece of music based on the given theme and constraints.\n\nTheme: {t['theme']}\nConstraints: {t['constraints']}\n\nSubmit your composition in plain text format, using standard musical notation (e.g., C-D-E-F-G)."
        elif t["task"] == "analyze":
            return f"Your task is to analyze the given piece of music.\n\nMusic: {t['music']}\n\nYour analysis should include: 1. The musical structure, 2. The key elements used (such as melody, harmony, rhythm), and 3. The overall mood or feel of the piece. Provide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "compose":
            criteria = [
                "The composition should adhere to the given theme.",
                "The composition should follow the specified constraints.",
                "The composition should be coherent and musically valid.",
                "The composition should be at least 16 bars long."
            ]
        elif t["task"] == "analyze":
            criteria = [
                "The analysis should correctly identify the musical structure.",
                "The analysis should accurately describe the key elements used.",
                "The analysis should provide a clear interpretation of the mood or feel of the piece."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
