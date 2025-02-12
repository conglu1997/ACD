class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "Time (s), Temperature (C)\n0, 20\n1, 23\n2, 27\n3, 32\n4, 38\n5, 45", "context": "The data represents the temperature change of a substance over time when heated."},
            "2": {"data": "Concentration (M), Absorbance\n0.1, 0.2\n0.2, 0.4\n0.3, 0.6\n0.4, 0.8\n0.5, 1.0", "context": "The data represents the absorbance of a solution at different concentrations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        data = t["data"]
        context = t["context"]
        return f"""Interpret the following experimental data and generate a plausible scientific hypothesis or conclusion based on that data:\n\nData:\n{data}\n\nContext:\n{context}\n\nProvide your response in the following format:\n\nHypothesis/Conclusion: [Your hypothesis or conclusion]\nExplanation: [A detailed explanation of how you arrived at your hypothesis or conclusion based on the data]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The hypothesis or conclusion should be scientifically plausible.", "The explanation should be logical and based on the data provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
