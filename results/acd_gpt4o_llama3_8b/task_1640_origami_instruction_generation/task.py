class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"origami_model": "crane", "complexity": "intermediate"},
            "2": {"origami_model": "frog", "complexity": "beginner"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        origami_model = t["origami_model"]
        complexity = t["complexity"]
        return f"""Generate step-by-step instructions for creating an origami {origami_model}. The model has a complexity level of {complexity}. Ensure your instructions are clear, detailed, and easy to follow for someone unfamiliar with the model. Each step should include specific folds, creases, and tips to achieve the desired shape. The steps should be concise, logically ordered, and easy to understand. Submit your instructions as a plain text string in the following format:\n\n1. [Step 1]\n2. [Step 2]\n3. [Step 3]\n..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and detailed enough for someone to follow.",
            "The instructions should correctly describe the process of creating the specified origami model.",
            "The steps should be logically ordered and easy to understand.",
            "The instructions should be appropriate for the specified complexity level.",
            "Each step should be concise and logically follow from the previous step.",
            "The instructions should include specific folds, creases, and tips to achieve the desired shape."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
