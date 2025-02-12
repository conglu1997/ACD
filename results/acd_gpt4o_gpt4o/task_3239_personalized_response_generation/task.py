class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"user_profile": "A 25-year-old software engineer who enjoys hiking and reading science fiction.", "context": "The user asks for book recommendations.", "objective": "Provide a response that includes book recommendations tailored to the user's interests."},
            "2": {"user_profile": "A 40-year-old parent of two children interested in healthy cooking and family activities.", "context": "The user asks for weekend activity suggestions.", "objective": "Provide a response that includes activity suggestions suitable for the user's family."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to generate a response tailored to the following user profile and context: \nUser Profile: '{t['user_profile']}'\nContext: '{t['context']}'\nObjective: '{t['objective']}'. Ensure that your response is personalized and relevant to the user's interests and situation. Provide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
