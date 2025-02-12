class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A farmer has a rectangular field that is 150 meters long and 80 meters wide. He wants to build a fence around the field and also divide it into two equal parts with a fence parallel to the shorter side. Calculate the total length of the fence he needs to buy.",
                "solution": "To find the total length of the fence, first calculate the perimeter of the field which is 2*(length + width). Then, add the length of the dividing fence. The total length of the fence is 2*(150 + 80) + 150 = 460 meters."
            },
            "2": {
                "problem": "A water tank is being filled with water at a rate of 30 liters per minute. The tank has a capacity of 1200 liters. If the tank was initially empty, how long will it take to fill the tank completely? Provide your answer in hours and minutes.",
                "solution": "To find the time to fill the tank, divide the total capacity by the filling rate. The time in minutes is 1200 / 30 = 40 minutes. Converting 40 minutes to hours and minutes, the time is 0 hours and 40 minutes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following real-world math problem and provide a detailed solution. Ensure that your solution includes all necessary calculations and clearly explains each step. Here is the problem:

{t["problem"]}

Your response should be clear, logically structured, and include the final answer. Submit your solution as a plain text string in the following format:

Step-by-step solution...
Final answer: <your final answer>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should include all necessary calculations.",
            "The solution should clearly explain each step.",
            "The final answer should be correct and clearly stated as 'Final answer: <your final answer>'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
