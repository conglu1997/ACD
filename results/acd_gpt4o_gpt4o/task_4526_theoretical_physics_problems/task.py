class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Derive the Schwarzschild radius for a non-rotating black hole and explain its significance in the context of general relativity."},
            "2": {"problem": "Using the principles of quantum mechanics, explain how the Heisenberg Uncertainty Principle imposes limits on the precision of simultaneous measurements of position and momentum."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following theoretical physics problem and provide a detailed explanation of your solution. Ensure that your explanation is clear, coherent, and demonstrates a deep understanding of the underlying physical concepts. Include any necessary mathematical derivations and logical reasoning.

Problem: {t['problem']}

Your explanation should be between 300 and 600 words long. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should demonstrate a deep understanding of the underlying physical concepts.",
            "The mathematical derivations should be correct and logically sound.",
            "The response should be between 300 and 600 words long.",
            "The explanation should be clear and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
