class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"},
            "2": {"puzzle": "You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following riddle or puzzle and provide a detailed and logical explanation for your solution:

{t['riddle'] if 'riddle' in t else t['puzzle']}

Your explanation should include:
1. A clear statement of the solution.
2. A step-by-step explanation of your reasoning process.

Ensure your explanation is clear and demonstrates your reasoning process. Provide your response in plain text format and label each section clearly as 'Solution' and 'Explanation'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear solution and a detailed explanation of the reasoning process."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
