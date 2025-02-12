class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"paragraph": "Their is many reasons why people likes to travel. Firstly, traveling allows one to explore new places and cultures. It can also be a great way to relax and escape the daily routine. However, travelings can also be stressful, especially if things goes wrong."},
            "2": {"paragraph": "The company have implemented a new policy to improve productivity. Employees are requires to submit weekly reports and attend regular meetings. While some employees feel the policy is to strict, others believes it will lead to better communication and collaboration."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and correct errors in the following paragraph. Ensure that your corrections improve the overall clarity, readability, and grammatical accuracy of the text. Submit the corrected paragraph as a plain text string.

Paragraph:
{t["paragraph"]}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The corrected paragraph should be free of grammatical, syntactical, and stylistic errors.", "The overall clarity and readability of the paragraph should be improved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
