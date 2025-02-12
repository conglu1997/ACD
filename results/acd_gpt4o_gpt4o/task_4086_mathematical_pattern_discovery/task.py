class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": [2, 4, 8, 16, 32]},
            "2": {"sequence": [1, 1, 2, 6, 24]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and articulate the pattern in the following sequence:

{t['sequence']}

Your response should include:
1. A clear identification of the pattern.
2. An explanation of how the pattern is derived.
3. A prediction of the next two elements in the sequence.

Ensure that your explanation is detailed, logically sound, and does not contain any errors. Provide your response in plain text format in the following structure:

- Pattern Identification: [Your identification of the pattern]
- Explanation: [Your detailed explanation]
- Next Elements: [Your prediction of the next two elements]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly identify the pattern in the sequence.",
            "The response should include a logical and detailed explanation of how the pattern is derived.",
            "The response should correctly predict the next two elements in the sequence based on the identified pattern."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
