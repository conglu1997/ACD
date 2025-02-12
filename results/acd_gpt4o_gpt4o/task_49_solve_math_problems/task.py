class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Calculate the area of a triangle with base 10 units and height 5 units."},
            "2": {"prompt": "Find the roots of the quadratic equation: x^2 - 4x + 4 = 0."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following mathematical problem and provide a detailed solution:

Prompt: {t['prompt']}

Ensure your solution includes all necessary steps and explanations. Provide your solution in plain text format, showing your work clearly. For example, if the task is to find the area of a triangle, you should write:

Step 1: Identify the base and height.
Step 2: Apply the formula for the area of a triangle (Area = 0.5 * base * height).
Step 3: Calculate the area.

Your final answer should be clearly indicated."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be correct.", "The solution should include all necessary steps and explanations.", "The final answer should be clearly indicated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
