class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "# # #\n# . #\n# # #"},
            "2": {"description": "Generate a 5x5 grid where each cell in the border is '#' and each inner cell is '.'"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "pattern" in t:
            return f"""Your task is to interpret the following visual pattern and describe it in plain text:

{t["pattern"]}

Provide a detailed description of the visual pattern, including the arrangement of symbols and any identifiable structures or symmetries. Describe each row separately and mention any alternating sequences explicitly."""
        elif "description" in t:
            return f"""Your task is to generate a visual pattern based on the following description:

{t["description"]}

Ensure that the visual pattern is accurate and adheres to the given description. Provide the pattern in a standard format, with each row separated by a newline character (\n)."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "pattern" in t:
            criteria = [
                "The response should describe the arrangement of symbols in each row.",
                "The response should identify any structures or symmetries.",
                "The response should mention any alternating sequences explicitly.",
            ]
        elif "description" in t:
            criteria = [
                "The generated visual pattern should match the given description.",
                "Each row should be separated by a newline character (\n).",
                "The pattern should have '#' in all border cells and '.' in all inner cells.",
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
