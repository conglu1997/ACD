class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "task": "How to make a simple paper airplane", "constraints": "The instructions should be clear, detailed, and suitable for a beginner. Use no more than 10 steps. Do not use any images or diagrams. Ensure each step is logically sequenced and easy to follow. Provide an example of a common mistake and how to avoid it."},
            "2": {"task_type": "following", "instructions": "1. Take a piece of paper.\n2. Fold the paper in half lengthwise.\n3. Unfold the paper and fold the top two corners to the center crease.\n4. Fold the top edges to the center crease again.\n5. Fold the paper in half along the original center crease.\n6. Fold the wings down, matching the top edges to the bottom edge of the body.\n7. Your paper airplane is ready to fly!"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generation":
            return f"Generate a clear and detailed set of step-by-step instructions for the following task: {t['task']}. Ensure that the instructions are suitable for a beginner and use no more than 10 steps. Do not use any images or diagrams. Ensure each step is logically sequenced and easy to follow. Provide an example of a common mistake and how to avoid it. Submit your instructions as a plain text string in the following format: 'Step 1: [instruction]\nStep 2: [instruction]\n...\nStep 10: [instruction]\nCommon Mistake: [description of mistake and how to avoid it]'"
        elif t["task_type"] == "following":
            return f"Follow the given set of instructions to complete the task. Provide a description of the completed task and any observations. Ensure your description reflects an accurate completion of the task. Submit your response as a plain text string in the following format: 'Completed Task: [description]\nObservations: [any observations]' Instructions:\n{t['instructions']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generation":
            criteria = ["The generated instructions should be clear, detailed, suitable for a beginner, and not exceed 10 steps. No images or diagrams should be used. Each step should be logically sequenced and easy to follow. An example of a common mistake and how to avoid it should be included."]
        elif t["task_type"] == "following":
            criteria = ["The response should accurately describe the completed task and any observations, reflecting an accurate completion of the task."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
