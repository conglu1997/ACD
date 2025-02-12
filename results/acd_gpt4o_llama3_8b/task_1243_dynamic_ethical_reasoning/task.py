class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a rescue worker with a limited amount of time and resources to save people trapped in a collapsing building. You can either save a group of elderly people or a young child who is a prodigy and expected to make significant contributions to society in the future. Both groups are in equally critical condition.",
                "ethical_principle": "Utilitarianism"
            },
            "2": {
                "scenario": "You are a judge presiding over a case where a person stole food to feed their starving family. The law mandates a strict punishment for theft, but the person's actions were driven by desperation to save their family from hunger.",
                "ethical_principle": "Deontology"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario and ethical principle:

Scenario:
{t['scenario']}

Ethical Principle: {t['ethical_principle']}

Your task is to:
1. Explain the ethical principle provided.
2. Evaluate the dilemma using the provided ethical principle.
3. Make a decision and justify it based on the ethical principle.
4. Consider and address potential counterarguments to your decision.

Submit your response as a plain text string in the following format:
- Explanation of Ethical Principle: [Your explanation here]
- Evaluation of Dilemma: [Your evaluation here]
- Decision and Justification: [Your decision and justification here]
- Counterarguments: [Your counterarguments here]

Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of the ethical principle and the scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately explain the ethical principle.",
            "The response should evaluate the dilemma using the provided ethical principle.",
            "The response should make a decision and justify it based on the ethical principle.",
            "The response should consider and address potential counterarguments.",
            "The response should be well-structured, coherent, and demonstrate a deep understanding of the ethical principle and the scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
