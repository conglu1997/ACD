class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Create a fictional world including the following elements: a unique geography, a distinct culture, and a pivotal historical event."},
            "2": {"prompt": "Expand upon the following fictional world description by adding details about its political structure and key figures: 'The land of Eldoria is a vast kingdom with lush forests and towering mountains. The inhabitants are known for their intricate craftsmanship and deep respect for nature. Long ago, a great war shaped the history of Eldoria, leaving behind ancient ruins and legends of heroic deeds.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['prompt']}

Ensure that your response is coherent, detailed, and maintains internal consistency within the fictional world. Submit your answer in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be coherent and detailed.",
            "The response should maintain internal consistency within the fictional world.",
            "The response should expand on the given elements appropriately.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0