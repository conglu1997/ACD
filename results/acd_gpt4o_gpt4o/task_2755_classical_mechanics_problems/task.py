class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A 5 kg block is placed on a frictionless inclined plane of 30 degrees. Calculate the acceleration of the block down the plane."},
            "2": {"problem": "A projectile is launched with an initial velocity of 20 m/s at an angle of 45 degrees to the horizontal. Calculate the maximum height reached by the projectile."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following classical mechanics problem using principles of physics and mathematics. Show all steps and provide the final answer.\n\nProblem:\n{t['problem']}\n\nSubmit your solution in the following format:\n\nSolution:\n[Your detailed solution here]\nFinal Answer:\n[Your final answer here with units]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        problem = t["problem"]
        if "frictionless inclined plane" in problem:
            criteria = [
                "The solution should correctly identify the forces acting on the block.",
                "The solution should use the correct formula for acceleration on an inclined plane.",
                "The final answer should be accurate and include correct units."
            ]
        elif "projectile is launched" in problem:
            criteria = [
                "The solution should correctly decompose the initial velocity into horizontal and vertical components.",
                "The solution should use the correct kinematic equations to find the maximum height.",
                "The final answer should be accurate and include correct units."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
