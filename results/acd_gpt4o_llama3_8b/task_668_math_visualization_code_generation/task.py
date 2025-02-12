class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirement": "Write a Python script using Matplotlib to plot a sine wave from 0 to 2π. The plot should include labeled axes, a title, and a legend."
            },
            "2": {
                "requirement": "Write a Python script using Matplotlib to create a scatter plot of 100 random data points within the range (-10, 10) for both x and y axes. The scatter plot should have a different color for each quadrant, labeled axes, a title, and a legend."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a Python script based on the given requirement:

Requirement:
{t['requirement']}

Ensure the Python code is syntactically correct and produces the specified visualization using Matplotlib. Include necessary imports, data generation, and all required plot elements. Submit your code as a plain text string in the following format:

[Your Python code here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The Python code should be syntactically correct.", "The script should use Matplotlib to generate the specified visualization.", "The plot should include all required elements such as labeled axes, title, and legend."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
