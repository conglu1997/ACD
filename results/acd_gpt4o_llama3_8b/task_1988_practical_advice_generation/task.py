class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A friend is considering quitting their stable job to pursue a passion for painting full-time. They are unsure about their financial stability and the risks involved. What practical advice would you give them?"},
            "2": {"scenario": "You have been invited to a wedding, but you have a conflicting work commitment on the same day. You value both the personal relationship and your professional responsibilities. What practical advice would you give on how to handle this situation?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t['scenario']
        return f"Provide practical advice based on the following scenario: {scenario}. Ensure that your advice is coherent, empathetic, and takes into consideration the various factors involved. Submit your advice as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The advice should be practical and actionable.",
            "The advice should demonstrate empathy and understanding of the scenario.",
            "The advice should consider multiple factors relevant to the situation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
