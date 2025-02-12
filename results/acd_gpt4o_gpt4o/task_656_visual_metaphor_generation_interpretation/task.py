class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "freedom", "task_type": "generation"},
            "2": {"visual_metaphor": "A bird flying out of an open cage", "task_type": "interpretation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generation":
            return """Your task is to create a visual metaphor for the following concept:

{0}

Describe your visual metaphor in detail, ensuring it effectively conveys the concept. Provide your response in plain text format.""".format(t["concept"])
        elif t["task_type"] == "interpretation":
            return """Your task is to interpret the following visual metaphor:

{0}

Explain the meaning and the underlying concept it represents. Provide your response in plain text format.""".format(t["visual_metaphor"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should effectively convey the target concept through a well-crafted visual metaphor." if t["task_type"] == "generation" else "The interpretation should accurately explain the underlying concept represented by the visual metaphor."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
