class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A car is traveling at a constant speed of 60 km/h. How long will it take to travel 150 km? Provide your answer in hours. Use the formula Time = Distance / Speed. Show all your work."},
            "2": {"problem": "You have a solution with a concentration of 2 M. How many moles of solute are there in 500 mL of this solution? Convert the volume from milliliters to liters before applying the formula Molarity = moles of solute / volume of solution in liters. Show all your work."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t['problem']
        return f"""Solve the following scientific problem: '{problem}'. Provide a detailed explanation of your solution, including any formulas or principles used.
Ensure to show all steps in your calculations and reasoning clearly.
Submit your response as a plain text string in the format:

Solution: [Your detailed solution here]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be correct and clearly explained.",
            "All relevant scientific principles and formulas should be correctly applied.",
            "The solution should include all steps in the calculation and reasoning.",
            "The answer should be provided with appropriate units."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
