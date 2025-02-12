class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"paradox": "The Barber Paradox: In a town, there is a barber who shaves all those, and only those, who do not shave themselves. Does the barber shave himself?"},
            "2": {"paradox": "The Liar Paradox: Consider the statement 'This statement is false.' Is the statement true or false?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain and resolve the given mathematical paradox.

Paradox: {t['paradox']}

Instructions:
1. Provide a detailed explanation of the paradox, including its background and significance.
2. Attempt to resolve the paradox logically, presenting any steps or reasoning used in your resolution.
3. Ensure that your explanation is coherent, logical, and demonstrates a deep understanding of the paradox.

Your response should be structured as follows:
Explanation: [Your detailed explanation]
Resolution: [Your logical resolution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should clearly describe the paradox, including its background and significance.", "The resolution should logically address the paradox, demonstrating a deep understanding of the problem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
