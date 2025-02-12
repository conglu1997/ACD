class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "You need to paint a room. The room is 12 feet long, 10 feet wide, and 8 feet high. Calculate the amount of paint needed if one gallon covers 350 square feet. Provide your step-by-step solution and final answer."},
            "2": {"problem": "You are planning a road trip. Your car's fuel efficiency is 25 miles per gallon, and the total distance of the trip is 500 miles. Calculate the total cost of fuel if the price per gallon is $3.50. Provide your step-by-step solution and final answer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following practical problem. Provide a detailed, step-by-step solution and the final answer.

Problem: {t['problem']}

Ensure your solution is clear, logical, and accurate. Format your response as follows:

Steps: 
1. [Step 1]
2. [Step 2]
...

Final Answer: [Your final answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be detailed and step-by-step.",
            "The final answer should be accurate.",
            "The reasoning should be logical and clear.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
