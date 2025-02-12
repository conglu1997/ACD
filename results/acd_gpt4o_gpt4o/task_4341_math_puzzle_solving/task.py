class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A train leaves City A at 7:00 AM traveling at 60 km/h. Another train leaves City B at 8:00 AM traveling at 80 km/h towards City A on the same track. The distance between City A and City B is 400 km. At what time will the two trains meet?"
            },
            "2": {
                "problem": "You have a 3-liter jug and a 5-liter jug, both unmarked. You need to measure exactly 4 liters of water using these two jugs. Explain how you would do it."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following mathematical problem:

Problem: {t['problem']}

Provide a clear and detailed solution to the problem. Your response should include all necessary steps and rationale for your solution. Additionally, provide a brief explanation of your solution to ensure transparency in your reasoning process.

Your response should be structured as follows:
1. Solution: [Your solution here]
2. Explanation: [Your explanation here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should include all necessary steps and rationale.",
            "The solution should be mathematically correct.",
            "The explanation should be clear and transparent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
