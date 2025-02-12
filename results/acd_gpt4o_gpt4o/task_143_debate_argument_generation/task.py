class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "generate", "topic": "Should homework be banned in schools?"},
            "2": {"task": "respond", "topic": "Should homework be banned in schools?", "argument": "Homework should be banned because it adds unnecessary stress to students and takes away their free time for extracurricular activities and family interactions."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "generate":
            return f"Your task is to generate a coherent and persuasive argument for the following debate topic: '{t['topic']}'. Ensure your argument is well-structured, uses logical reasoning, and is persuasive. Provide your argument in plain text format."
        elif t["task"] == "respond":
            return f"Your task is to respond to the following argument on the debate topic: '{t['topic']}'. The argument is: '{t['argument']}'. Ensure your response is coherent, uses logical reasoning, and effectively counters the given argument. Provide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "generate":
            criteria = [
                "The argument should be coherent and well-structured.",
                "The argument should use logical reasoning.",
                "The argument should be persuasive."
            ]
        elif t["task"] == "respond":
            criteria = [
                "The response should be coherent and well-structured.",
                "The response should use logical reasoning.",
                "The response should effectively counter the given argument."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
