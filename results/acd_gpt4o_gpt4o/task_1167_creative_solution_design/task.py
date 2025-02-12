class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": ["Design a device that helps people with limited mobility to perform daily tasks independently.", "The device should be affordable and easy to use.", "It should be portable and not require permanent installation."]},
            "2": {"constraints": ["Create an app to help reduce food waste in households.", "The app should provide practical tips and reminders for using up ingredients.", "It should also allow users to share recipes and tips with a community."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = '\n'.join(t['constraints'])
        return f"""Your task is to design a creative solution or product based on the given constraints and describe its functionality, benefits, and potential challenges. Ensure that your response is comprehensive and well-organized.

Constraints:
{constraints}

Provide your response in plain text format with the following structure:
1. Solution: [Your solution description]
2. Functionality: [Detailed description of how it works]
3. Benefits: [Benefits of the solution]
4. Challenges: [Potential challenges and how to address them]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
