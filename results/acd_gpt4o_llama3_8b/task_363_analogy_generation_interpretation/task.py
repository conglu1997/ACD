class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "concept_pair": ["sun", "moon"]},
            "2": {"task_type": "interpretation", "analogy": "Reading a book is like traveling to another world."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generation":
            return f"""Generate an analogy based on the following pair of concepts: '{t["concept_pair"][0]}' and '{t["concept_pair"][1]}'. The analogy should clearly illustrate a relationship similar to the one between the given concepts. Submit your analogy as a plain text string in the format: '[Concept1] is to [Concept2] as [Your analogy]'.

Example:
If the given concepts were 'cat' and 'mouse', a possible analogy could be 'Cat is to mouse as predator is to prey'."""
        elif t["task_type"] == "interpretation":
            return f"""Interpret the following analogy: '{t["analogy"]}'. Provide a clear and concise explanation of the relationship between the two parts of the analogy. Your explanation should help the reader understand why this analogy is appropriate. Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["task_type"] == "generation":
            criteria = ["The analogy should clearly illustrate a relationship similar to the one between the given concepts.", "The analogy should be in the format '[Concept1] is to [Concept2] as [Your analogy]'."]
        elif t["task_type"] == "interpretation":
            criteria = ["The explanation should clarify the relationship between the two parts of the analogy."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
