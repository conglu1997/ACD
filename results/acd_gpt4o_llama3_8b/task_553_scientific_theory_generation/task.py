class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"observations": "In an isolated ecosystem, a species of plant has been observed to grow significantly faster when exposed to a particular type of fungus. Hypothesize a scientific theory explaining this phenomenon."},
            "2": {"observations": "During a series of experiments, it was noted that a metal alloy exhibits increased conductivity when subjected to a magnetic field. Hypothesize a scientific theory explaining this behavior."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given observations or experimental data:

Observations: {t['observations']}

Generate a plausible scientific theory that explains the given observations. Your theory should include:
1. A clear statement of the theory.
2. A logical explanation of why this theory is plausible.
3. Potential evidence or reasoning that supports this theory.

Ensure that your theory is well-reasoned, coherent, and demonstrates a deep understanding of scientific principles. Submit your response as a plain text string with clearly labeled sections for 'Theory', 'Explanation', and 'Evidence'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear statement of the theory.", "The response should include a logical explanation of why this theory is plausible.", "The response should include potential evidence or reasoning that supports the theory.", "The theory should be well-reasoned, coherent, and demonstrate a deep understanding of scientific principles.", "The scientific concepts used should be relevant and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
