class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A car travels at a constant speed of 60 km/h. It starts its journey at 8:00 AM and travels until 10:30 AM without stopping. How far will it travel during this time? Show all steps in your calculations."},
            "2": {"problem": "A ball is thrown vertically upwards with an initial velocity of 20 m/s from the ground level. Ignoring air resistance, calculate the time it will take for the ball to reach its highest point and the maximum height it will achieve. (Assume g = 9.8 m/s²). Show all steps in your calculations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to interpret and solve the following scientific word problem:\n\nProblem: {problem}\n\nProvide a clear and concise solution, including all necessary calculations and the final answer. Ensure your response is logically coherent and accurately applies relevant scientific principles.\n\nResponse Format:\nSolution: <Your solution with detailed steps>\nAnswer: <Your final answer>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should include all necessary calculations.",
            "The final answer should be correct and clearly stated.",
            "The response should logically apply relevant scientific principles."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
