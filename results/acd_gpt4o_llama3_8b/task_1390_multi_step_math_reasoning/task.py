class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A rectangular garden has a length that is twice its width. The perimeter of the garden is 48 meters. Determine the area of the garden."},
            "2": {"problem": "A car travels 60 km in 1.5 hours, then 80 km in 2 hours, and finally 100 km in 2.5 hours. Calculate the car's average speed for the entire journey."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"""Solve the following mathematical problem based on the given scenario:\n\n{problem}\n\nProvide your solution with detailed steps and calculations. Submit your solution as a plain text string in the following format:\n\nStep 1: [Description of step and calculations]\nStep 2: [Description of step and calculations]\n...\nFinal Answer: [Your final answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly follow the steps to solve the problem.",
            "Each step should be clearly described and logically follow from the previous one.",
            "The final answer should be correct and match the calculations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
