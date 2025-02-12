class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "It is the year 1492, and Christopher Columbus has just discovered the New World. Hypothesize how this event might influence the political landscape of Europe in the following decades."},
            "2": {"context": "In 1969, humans first landed on the moon. Hypothesize the potential long-term effects this achievement might have on global politics and technological advancement."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given historical context:

Historical Context: {t['context']}

Generate a plausible historical hypothesis about the given event or context. Your hypothesis should include:
1. A clear statement of the hypothesis.
2. A logical explanation of why this hypothesis is plausible.
3. Potential evidence or reasoning that supports this hypothesis.

Ensure that your hypothesis is well-reasoned, coherent, and demonstrates a deep understanding of historical principles. Submit your response as a plain text string with clearly labeled sections for 'Hypothesis', 'Explanation', and 'Evidence'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear statement of the hypothesis.", "The response should include a logical explanation of why this hypothesis is plausible.", "The response should include potential evidence or reasoning that supports the hypothesis.", "The hypothesis should be well-reasoned, coherent, and demonstrate a deep understanding of historical principles."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
