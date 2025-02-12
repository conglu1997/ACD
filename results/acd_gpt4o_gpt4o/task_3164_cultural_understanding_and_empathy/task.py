class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A colleague from Japan is visiting your office in the United States for the first time. They seem uncomfortable during a team meeting where people are being very direct. How would you address this situation in a culturally sensitive manner?"},
            "2": {"scenario": "You are organizing a multicultural event at your workplace. Employees from different cultural backgrounds will be participating, including some from countries where certain dietary restrictions are common. Provide a set of guidelines to ensure that the event is inclusive and respectful of all cultures."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to respond to the following scenario in a culturally sensitive and empathetic manner:

Scenario: {t['scenario']}

Ensure your response demonstrates an understanding of cultural norms and values, and provides a thoughtful, respectful, and effective solution or advice. Provide your response in plain text format and ensure it is concise and to the point."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate an understanding of cultural norms and values.",
            "The response should be thoughtful, respectful, and effective in addressing the situation.",
            "The response should be clear, logical, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
