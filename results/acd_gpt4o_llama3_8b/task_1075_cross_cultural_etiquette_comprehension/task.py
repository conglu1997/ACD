class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are invited to a traditional Japanese tea ceremony. Describe the appropriate behavior and customs that you should follow during the ceremony."},
            "2": {"scenario": "You are attending a business meeting in Saudi Arabia. Generate a culturally-appropriate greeting and introduction for the meeting."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Interpret the following social scenario in its specific cultural context and explain the appropriate behavior or generate a culturally-appropriate response:\n\n{scenario}\n\nEnsure that your response is accurate, culturally sensitive, and follows the social norms of the given context. Avoid adding any unnecessary information that is not relevant to the scenario.\n\nYour submission should include the following:\n1. A clear and concise explanation of the appropriate behavior or response.\n2. Relevant cultural norms or customs that apply.\n3. An example of how to behave or respond appropriately.\n\nSubmit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately address the given scenario.",
            "The response should include a clear explanation of appropriate behavior or response.",
            "The response should reference relevant cultural norms or customs.",
            "The response should provide an example of appropriate behavior or response.",
            "The response should be culturally sensitive and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
