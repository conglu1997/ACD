class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"profile": "User: John, Age: 30, Interests: fitness, cooking, technology", "scenario": "John is looking for a new hobby to try on weekends."},
            "2": {"profile": "User: Emma, Age: 35, Interests: yoga, painting, entrepreneurship", "scenario": "Emma is looking for ways to balance her work and personal life."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate personalized advice or recommendations based on the given user profile and scenario.

User Profile: {t['profile']}
Scenario: {t['scenario']}

Provide your response in plain text format with the following structure:

Advice: [Your personalized advice or recommendation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The advice should be personalized based on the user profile.", "The advice should be relevant to the scenario.", "The advice should be practical and actionable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
