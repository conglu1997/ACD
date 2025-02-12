class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instructions": "1. Take a piece of paper. 2. Fold the paper in half lengthwise. 3. Draw a star on the folded paper. 4. Cut out the star along the lines you drew. 5. Unfold the paper to reveal the star cut-out."},
            "2": {"task": "Create a set of procedural instructions for making a simple paper airplane."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "instructions" in t:
            return f"Your task is to follow the given set of procedural instructions and describe the final outcome:\n\n{t['instructions']}\n\nProvide your description of the final outcome in plain text format. Your response should be clear and accurately reflect the result of following the instructions.\n\nResponse format:\nFinal Outcome: [Your description here]"
        elif "task" in t:
            return f"Your task is to create a set of procedural instructions for the following task:\n\n{t['task']}\n\nEnsure that the instructions are clear, logically sequenced, and easy to follow. Provide your instructions in plain text format.\n\nResponse format:\nProcedural Instructions: [Your instructions here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "instructions" in t:
            criteria = [
                "The description should accurately reflect the result of following the procedural instructions.",
                "The response should be clear and logically sequenced.",
                "The response should match the expected format."]
        elif "task" in t:
            criteria = [
                "The procedural instructions should be clear and easy to follow.",
                "The instructions should be logically sequenced and complete the task as described.",
                "The response should match the expected format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0