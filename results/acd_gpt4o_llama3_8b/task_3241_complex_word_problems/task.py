class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A train leaves City A at 9:00 AM traveling at 60 km/h. Another train leaves City B at 10:00 AM traveling at 80 km/h towards City A. The distance between City A and City B is 300 km. At what time will the two trains meet?",
                "criteria": "The response should include the exact time (HH:MM AM/PM) at which the trains will meet, along with a clear, step-by-step explanation of the calculations involved."
            },
            "2": {
                "description": "A farmer has a rectangular field that is 150 meters long and 80 meters wide. He wants to divide the field into smaller rectangular plots, each with an area of 1200 square meters. How many such plots can he create?",
                "criteria": "The response should include the number of smaller plots that can be created, along with a clear, step-by-step explanation of the calculations involved."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the given word problem by extracting and processing the mathematical information from the description.

Description:
{t['description']}

Response Format:
Provide the solution with a clear, step-by-step explanation of the calculations involved. For Task 1, include the exact time (HH:MM AM/PM) at which the trains will meet. For Task 2, include the number of smaller plots that can be created. Ensure that your explanation is detailed and logical. Your response should be in the following format:

Final Answer: [Your final answer here]
Explanation: [Your detailed explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [t['criteria']]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
