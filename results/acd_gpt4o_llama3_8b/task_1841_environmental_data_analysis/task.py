class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Year, CO2 Emissions (Million Metric Tons), Global Temperature Anomaly (°C)\n2000, 25000, 0.42\n2005, 27000, 0.48\n2010, 30000, 0.54\n2015, 32000, 0.67\n2020, 34000, 0.72\n2025, 36000, 0.76\n2030, 38000, 0.80\n2035, 40000, 0.85",
                "question": "Analyze the data and discuss the relationship between CO2 emissions and global temperature anomalies."
            },
            "2": {
                "data": "Year, Deforestation Rate (Hectares/year), Species Extinction Rate (Species/year)\n2000, 100000, 20\n2005, 95000, 22\n2010, 90000, 25\n2015, 85000, 27\n2020, 80000, 30\n2025, 75000, 32\n2030, 70000, 35\n2035, 65000, 38",
                "question": "Analyze the data and discuss the impact of deforestation on species extinction rates."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given environmental data and draw conclusions based on the dataset. Your analysis should include:
1. A clear explanation of the trends observed in the data.
2. A discussion on the relationship between the variables provided.
3. Any potential implications or inferences that can be drawn from the data.

Dataset:
{t['data']}

Question: {t['question']}

Submit your response as a plain text string in paragraph format, clearly addressing each of the points mentioned above. Ensure your response is well-structured, detailed, and comprehensive."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should accurately describe the trends observed in the data.",
            "The discussion should clearly explain the relationship between the variables provided.",
            "The inferences and implications drawn from the data should be logical and scientifically sound.",
            "The response should be coherent, well-structured, detailed, and comprehensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
