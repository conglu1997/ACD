class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"equation": "3x + 5 = 20", "scenario": "linear equation"},
            "2": {"equation": "A = πr^2", "scenario": "area of a circle"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and accurate word problem based on the following mathematical equation or scenario:

Equation: {t["equation"]}
Scenario: {t["scenario"]}

Ensure that the word problem is clear, understandable, and accurately represents the given mathematical equation or scenario. The word problem should be feasible and realistic in a real-world context. Provide the word problem as a plain text string. Format your response as follows:

Word Problem: [Your word problem]

Example:
For the equation 'x + 3 = 7', a suitable word problem could be: 'John has three more apples than Mary. If John has seven apples, how many apples does Mary have?'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The word problem should accurately represent the given equation or scenario.",
            "The word problem should be clear and understandable.",
            "The word problem should be coherent and contextually appropriate.",
            "The word problem should be feasible and realistic in a real-world context.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
