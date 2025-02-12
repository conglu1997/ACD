class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "love"},
            "2": {"concept": "time"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t['concept']
        return f"""Generate a metaphor based on the following concept: '{concept}'. Then, explain the meaning of the metaphor. Ensure that the metaphor is creative, original, and clearly related to the given concept. Your explanation should demonstrate a clear understanding of both the metaphor and the concept.

Submit your response as a plain text string in the following format:
'Metaphor: [Your metaphor] Explanation: [Your explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The metaphor should be creative and original.",
            "The metaphor should clearly relate to the given concept.",
            "The explanation should demonstrate a clear understanding of both the metaphor and the concept.",
            "The metaphor should demonstrate a level of sophistication and depth."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
