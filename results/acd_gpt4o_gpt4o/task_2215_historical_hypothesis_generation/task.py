class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event_context": "The sudden decline of the Mayan civilization around the 9th century."},
            "2": {"event_context": "The disappearance of the Roanoke Colony in the late 16th century."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a plausible hypothesis for the following historical event based on the provided context:

Historical Event: {t['event_context']}

Your hypothesis should be creative, coherent, and plausible based on historical knowledge. Provide your response in the following format:

Hypothesis: [Your hypothesis]

Example:
Historical Event: The sudden decline of the Mayan civilization around the 9th century.
Hypothesis: [Example hypothesis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The hypothesis should be creative and coherent.", "The hypothesis should be plausible based on historical knowledge."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
