class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A car accelerates uniformly from rest to a speed of 20 m/s in 10 seconds. Calculate the acceleration of the car and the distance it travels in this time. Additionally, find the car's velocity at 5 seconds."},
            "2": {"problem": "A point charge of 5 μC is placed at the origin. Calculate the electric field at a point 3 meters away from the charge. Use the value of the electric constant (ε₀) as 8.85 x 10^-12 C²/(N·m²). Additionally, determine the force experienced by a 2 μC charge placed at this point."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following physics problem by applying the relevant principles and concepts.

Problem:
{t['problem']}

Instructions:
1. Identify the relevant principles and concepts needed to solve the problem.
2. Perform the necessary calculations step-by-step to arrive at the solution. Show all work clearly.
3. Clearly explain each step and the reasoning behind it.
4. Provide the final answer with appropriate units.

Your response should be in the following format:
Explanation: [Your explanation]
Calculations: [Step-by-step calculations]
Answer: [Final answer with units]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should clearly identify the relevant principles and concepts.", "The calculations should be performed step-by-step and be correct.", "The final answer should be provided with appropriate units."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
