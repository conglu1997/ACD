class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"goal_model": "crane", "initial_step": "Start with a square piece of paper with the colored side up."},
            "2": {"goal_model": "frog", "initial_step": "Start with a square piece of paper with the colored side up."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate step-by-step origami instructions to create the specified origami model. Begin with the given initial step and ensure that each step is clear, detailed, and necessary. The final step should complete the origami model. Here is the information about the task:\n\nGoal Model: {t['goal_model']}\nInitial Step: {t['initial_step']}\n\nSubmit your instructions in plain text format. Use the following format for each step:\nStep 1: [Description of step]\nStep 2: [Description of step]\n...\nFinal Step: [Final description completing the model]\n\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The instructions should lead to the creation of a {t['goal_model']}.", "Each step should be clear, detailed, and necessary.", "The final step should complete the origami model."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
