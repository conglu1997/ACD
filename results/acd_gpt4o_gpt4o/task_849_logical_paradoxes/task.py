class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"paradox": "This statement is false.", "task": "Explain why this statement is a paradox and discuss its implications."},
            "2": {"criteria": "Create a logical paradox involving a scenario where a time traveler meets their past self.", "task": "Generate a detailed description of the paradox and explain why it is logically inconsistent."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "paradox" in t:
            instructions = f"""Your task is to interpret the following logical paradox:

Paradox: {t["paradox"]}

Explain why this statement is a paradox and discuss its implications. Ensure your explanation is clear and logical. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to generate a logical paradox based on the following criteria:

Criteria: {t["criteria"]}

Generate a detailed description of the paradox and explain why it is logically inconsistent. Ensure your paradox is coherent and well-structured. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation or generated paradox should be clear and logically consistent.",
            "The response should demonstrate an understanding of logical paradoxes.",
            "For the generation task, the paradox should be original and meet the given criteria.",
            "The response should be provided in plain text format as specified in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
