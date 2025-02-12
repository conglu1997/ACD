class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'coordinates': '48.8588443,2.2943506'},  # Eiffel Tower, Paris, France
            '2': {'coordinates': '40.689247,-74.044502'},   # Statue of Liberty, New York, USA
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed description of the location based on the provided coordinates.

Coordinates: {t['coordinates']}

Your description should include:
1. The name of the location (if known).
2. Notable historical, cultural, or geographical features.
3. Any relevant facts that would help someone understand the significance of the location.
4. Ensure the description is coherent, informative, and contextually accurate.

Provide your description in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The description should include the name of the location if known.',
            'The description should mention notable historical, cultural, or geographical features.',
            'The description should include relevant facts to understand the significance of the location.',
            'The description should be coherent, informative, and contextually accurate.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
