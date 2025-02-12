class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are an American businessperson meeting a Japanese client for the first time. The meeting is in Tokyo. The Japanese client values punctuality and formal greetings."},
            "2": {"scenario": "You are a British tourist visiting a traditional market in Morocco. You want to buy a handmade rug. The market is known for its bargaining culture."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Respond to the following cross-cultural scenario in a manner that is culturally appropriate and sensitive. Your response should demonstrate an understanding of the cultural context and norms. Ensure your response is clear, respectful, and takes into account any cultural nuances.

Scenario: {t['scenario']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate an understanding of the cultural context.",
            "The response should be respectful and culturally sensitive.",
            "The response should be clear and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
