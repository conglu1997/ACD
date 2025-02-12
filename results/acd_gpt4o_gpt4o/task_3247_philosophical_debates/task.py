class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Debate the merits and drawbacks of utilitarianism as a moral theory. Include counterarguments and rebuttals."},
            "2": {
                "prompt": "Discuss whether free will or determinism provides a more accurate account of human behavior. Consider various philosophical positions in your response."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in a philosophical debate based on the following prompt:

Prompt:
{t['prompt']}

Construct a coherent and well-reasoned argument that includes multiple perspectives, counterarguments, and rebuttals. Your response should demonstrate a deep understanding of the philosophical concepts involved and be persuasive in its reasoning. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should construct a coherent and well-reasoned argument.",
                   "The response should include multiple perspectives, counterarguments, and rebuttals.",
                   "The response should demonstrate a deep understanding of the philosophical concepts involved.",
                   "The response should be persuasive in its reasoning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
