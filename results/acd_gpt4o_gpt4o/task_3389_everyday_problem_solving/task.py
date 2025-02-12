class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "You are locked out of your house and have no spare key. What steps can you take to get back inside?", "description": "Provide a practical, step-by-step solution to regain access to your house."},
            "2": {"problem": "Your phone battery is critically low, and you need to make an important call. What are your options?", "description": "Suggest practical solutions to ensure you can make the important call despite the low battery."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        description = t["description"]
        instructions = f"""Your task is to solve the following practical problem:\n\nProblem: {problem}\n\nDescription: {description}\n\nProvide your solution as a list of steps or options in plain text format. Ensure that your solution is feasible and practical for the given scenario."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
