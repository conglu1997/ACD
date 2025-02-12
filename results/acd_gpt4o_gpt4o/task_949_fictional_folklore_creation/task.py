class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"culture": "Japanese", "elements": ["mountain", "spirit", "cherry blossom"]},
            "2": {"culture": "Norse", "elements": ["sea", "giant", "storm"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        elements = ', '.join(t['elements'])
        return f"""Your task is to create a piece of fictional folklore or mythology based on the given cultural elements. The culture for this task is '{t['culture']}'. The elements you must incorporate are: {elements}. Ensure that your folklore is:
1. Coherent and engaging.
2. Culturally relevant.
3. Incorporates all given cultural elements.

Provide your response in plain text format, structured as follows:

1. Title: [Your folklore title]
2. Folklore: [Your folklore story]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should incorporate all given cultural elements.",
            "The folklore should be coherent and engaging.",
            "The folklore should be culturally relevant.",
            "The folklore should follow the response structure provided in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
