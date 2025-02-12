class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A significant event in the early 20th century where a major global conflict began, involving many countries and leading to widespread destruction."},
            "2": {"description": "An event in the 18th century where a series of meetings and discussions led to the drafting of a fundamental document for a new nation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        return f"""Identify the historical event based on the following description and provide a detailed explanation of its significance:

Description: {description}

Your response should include the name of the event and a thorough explanation covering the key aspects and impact of the event. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly identify the historical event.", "The explanation should be detailed and cover the key aspects and impact of the event."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
