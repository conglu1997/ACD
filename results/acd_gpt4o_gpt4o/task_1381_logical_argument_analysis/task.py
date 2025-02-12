class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"argument": "If we don't ban all cars, the world will end due to climate change. We must ban all cars to save the planet."},
            "2": {"argument": "Everyone says that the new policy is a failure, so it must be true."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify any logical fallacies in the following argument and explain why they are fallacies. Additionally, reconstruct the argument in a logically sound manner. Provide a detailed explanation for both the identification and reconstruction.

Argument:
{t['argument']}

Ensure your response is comprehensive, accurate, and demonstrates a clear understanding of logical fallacies and sound argumentation. Your response should include:
1. Identification of each logical fallacy present in the argument.
2. Explanation of why each identified fallacy is problematic.
3. Reconstruction of the argument in a logically sound manner.

Provide your response in the following format:

Identification of Fallacies:
[Your identification of fallacies]

Explanation:
[Your explanation of why each fallacy is problematic]

Reconstructed Argument:
[Your logically sound argument]

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should identify logical fallacies in the argument.",
            "The explanation should clarify why each identified fallacy is problematic.",
            "The argument should be reconstructed in a logically sound manner."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
