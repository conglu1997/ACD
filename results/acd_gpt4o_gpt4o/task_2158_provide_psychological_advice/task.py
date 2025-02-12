class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A teenager is feeling overwhelmed by schoolwork and peer pressure. They are struggling to balance their academic responsibilities with their social life and are experiencing high levels of stress."},
            "2": {"scenario": "An adult is going through a tough breakup and is finding it difficult to cope with the emotional pain. They feel lonely and are unsure how to move on from the relationship."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide psychological advice or support based on the following scenario. Ensure that your advice is empathetic, supportive, and appropriate for the situation described.

Scenario: {t['scenario']}

Please submit your response in plain text format."
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The advice should be empathetic and supportive.",
            "The advice should be appropriate for the given scenario.",
            "The response should be in plain text format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
