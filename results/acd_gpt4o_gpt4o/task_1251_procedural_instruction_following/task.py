class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Build a paper airplane", "steps": ["Fold the paper in half vertically.", "Unfold the paper and fold each of the top corners into the center line.", "Fold the peak down to meet the edge of the previous fold.", "Fold the upper sides into the center line.", "Fold the top edges to the center line.", "Fold the plane in half so that the wings are on the outside.", "Fold the wings down so that they meet the bottom edge of the plane.", "Tweak the wings to ensure they are symmetrical.", "Test the plane to ensure it flies correctly.", "Make adjustments if necessary to improve flight."]},
            "2": {"task": "Make a cup of tea", "steps": ["Boil water in a kettle.", "Place a tea bag into a cup.", "Pour the boiling water into the cup.", "Let the tea steep for 3-5 minutes.", "Remove the tea bag.", "Add milk and sugar to taste.", "Stir the tea.", "Check the temperature before serving.", "Serve the tea in a clean cup.", "Clean up any spills and put away the kettle."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        task = t["task"]
        steps = t["steps"]
        instructions = f"""Your task is to create a set of detailed, multi-step instructions for the following task: {task}.\n\nThe steps to complete this task are:\n"""
        for step in steps:
            instructions += f"- {step}\n"
        instructions += "\nEnsure that each step is clearly explained and logically sequenced. Your instructions should be easy to follow and result in the successful completion of the task. Provide your response in the following format:\n\nInstructions:\n[Your detailed, step-by-step instructions]\n"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clearly explained.",
            "The steps should be logically sequenced.",
            "The instructions should result in the successful completion of the task.",
            "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
