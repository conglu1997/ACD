class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are in charge of organizing a large outdoor music festival. The weather forecast predicts heavy rain on the day of the event."
            },
            "2": {
                "scenario": "You are the manager of a tech startup facing a sudden drop in market demand for your main product."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Evaluate the following hypothetical scenario, predict potential outcomes, and propose a viable plan or solution. Your response should include:
1. A clear identification of the key issues and challenges.
2. A prediction of potential outcomes based on the given scenario.
3. A detailed plan or solution to address the situation, including any necessary steps and considerations.

Please submit your response in three distinct sections: Identification of Issues, Prediction of Outcomes, and Plan/Solution.

Scenario: {t['scenario']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should clearly identify the key issues and challenges.",
            "The response should include a prediction of potential outcomes based on the scenario.",
            "The response should propose a detailed and viable plan or solution to address the situation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
