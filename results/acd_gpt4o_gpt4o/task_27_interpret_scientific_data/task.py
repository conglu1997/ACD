class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "Time (s), Velocity (m/s)\n0, 0\n1, 3\n2, 5\n3, 6\n4, 9\n5, 12", "question": "Based on the data, describe the type of motion and calculate the average acceleration."},
            "2": {"data": "Concentration (M), Rate of reaction (M/s)\n0.1, 0.01\n0.2, 0.04\n0.3, 0.09\n0.4, 0.16\n0.5, 0.25", "question": "Determine the order of the reaction with respect to the concentration of the reactant and provide the rate law."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given scientific data and draw a conclusion based on it.

Data:
{t['data']}

Question: {t['question']}

Provide a clear and concise conclusion based on the interpretation of the data. Your response should include any necessary calculations and be scientifically accurate and logically reasoned. Format your answer as follows:

- Conclusion: [Your conclusion]
- Calculations: [Any relevant calculations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The conclusion should be scientifically accurate.", "The conclusion should logically follow from the data.", "The response should include relevant calculations.", "The response should be clear and concise."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
