class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "A programmer walks into a bar and asks for a drink that will fix all her bugs.", "task_type": "interpretation"},
            "2": {"context": "Create a joke that involves a chicken, a road, and a surprising twist.", "task_type": "generation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpretation":
            return """Your task is to explain why the following joke is funny:

{0}

Ensure that your explanation is clear, accurate, and captures the essence of the humor. Provide your response in plain text format.""".format(t["context"])
        elif t["task_type"] == "generation":
            return """Your task is to generate a joke based on the following context:

{0}

Ensure that your joke is original, funny, and fits the given context. Provide your response in plain text format.""".format(t["context"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should accurately convey why the joke is funny." if t["task_type"] == "interpretation" else "The generated joke should be original, funny, and fit the given context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
