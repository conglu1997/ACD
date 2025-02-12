class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["All humans are mortal.", "Socrates is a human."], "conclusion": "Socrates is mortal.", "description": "Generate a logical argument using the given premises and conclusion. Ensure the argument is valid and logically sound."},
            "2": {"premises": ["If it rains, the ground will be wet.", "It is raining."], "conclusion": "The ground is wet.", "description": "Generate a logical argument using the given premises and conclusion. Ensure the argument is valid and logically sound."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a logical argument based on the given premises and conclusion. Ensure that your argument is valid and logically sound.

Premises: {', '.join(t['premises'])}

Conclusion: {t['conclusion']}

{t['description']}

Ensure your argument includes:
1. A clear and valid logical structure.
2. A demonstration of how the conclusion follows from the premises.
3. Coherent and concise reasoning.
4. Avoid any logical fallacies or irrelevant information.

Provide your argument in plain text format.

Example response format:
1. Argument: [Your logical argument here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should have a clear and valid logical structure.",
            "The argument should demonstrate how the conclusion follows from the premises.",
            "The argument should be coherent and concise.",
            "The argument should directly address the given premises and conclusion without deviating from the logical framework.",
            "The argument should avoid any logical fallacies or irrelevant information."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
