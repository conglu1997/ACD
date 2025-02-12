class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A simple house with a triangular roof, a rectangular door in the center, and two square windows on each side of the door. The house is in a green field with a tree to the left.",
                "task_type": "text_to_visual"
            },
            "2": {
                "image_description": "A park with a fountain in the center, trees around the fountain, and people sitting on benches. A dog is playing near the fountain and a child is flying a kite.",
                "task_type": "visual_to_text"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        task_type = t.get("task_type")
        if task_type == "text_to_visual":
            return f"""Your task is to generate a visual representation based on the following textual description:

{t['description']}

Ensure that your representation accurately reflects the details provided in the description. Provide your response in plain text format describing the visual representation, such as:

Description: [Your description]"""
        elif task_type == "visual_to_text":
            return f"""Your task is to interpret the following visual representation described in text form and provide a detailed textual description:

{t['image_description']}

Ensure that your description accurately reflects the details provided in the visual description. Provide your response in plain text format, such as:

Description: [Your description]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_type = t.get("task_type")
        if task_type == "text_to_visual":
            criteria = [
                "The submission should accurately reflect the details provided in the description.",
                "The submission should be coherent and detailed.",
                "The submission should be in plain text format."
            ]
        elif task_type == "visual_to_text":
            criteria = [
                "The submission should accurately translate the visual description into a coherent and detailed textual description.",
                "The submission should be in plain text format."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
