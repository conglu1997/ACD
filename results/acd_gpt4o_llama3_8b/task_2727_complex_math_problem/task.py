class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A rectangular garden has a length that is 2 meters more than twice its width. If the perimeter of the garden is 34 meters, find the length and width of the garden."},
            "2": {"problem": "Solve the following system of equations for x and y: 3x + 4y = 18 and 2x - y = 3."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem step-by-step: '{t["problem"]}'. Show all your work, including intermediate steps and calculations, and provide the final answer at the end. Ensure that your solution is clear, logically structured, and correct. Submit your response in the following format:

Solution:
[Your step-by-step solution]

Final Answer:
[Your final answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be clear and logically structured.",
            "All steps of the solution should be shown.",
            "The final answer should be correct.",
            "The mathematical reasoning should be sound and accurate.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
