class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'phenomenon': 'Time travel is possible but only in one direction.'},
            '2': {'phenomenon': 'Plants can communicate with each other through an unknown energy field.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        phenomenon = t['phenomenon']
        return f"""Generate a fictional scientific hypothesis based on the following phenomenon and provide a coherent explanation of the hypothesis. Your explanation should include the following elements:
1. A brief description of the hypothesis.
2. An explanation of how the hypothesis accounts for the phenomenon.
3. Any potential implications or applications of the hypothesis.
4. Any assumptions or limitations of the hypothesis.

Ensure that your hypothesis is novel, imaginative, and scientifically plausible.

Phenomenon: {phenomenon}

Submit your response in the following format:

Hypothesis: [Your hypothesis]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The hypothesis should be coherent and account for the given phenomenon.',
            'The explanation should be logical and detailed.',
            'The hypothesis should demonstrate creativity and scientific knowledge.',
            'The submission should include potential implications or applications and any assumptions or limitations.',
            'The hypothesis should be novel and scientifically plausible.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
