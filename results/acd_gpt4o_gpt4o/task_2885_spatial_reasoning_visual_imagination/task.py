class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape": "square",
                "transformation": "rotate 90 degrees clockwise"
            },
            "2": {
                "layout": "The bookshelf is to the left of the desk. The lamp is on the desk. The chair is in front of the desk. The window is behind the chair.",
                "question": "Where is the window in relation to the bookshelf?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "transformation" in t:
            return f"""Your task is to visualize the following transformation of a shape: {t["transformation"]} for a {t["shape"]}. Describe the final position and orientation of the shape after the transformation. Provide your answer in a single sentence."""
        else:
            return f"""Your task is to understand the spatial layout described and answer the following question: {t["question"]}. The layout is: {t["layout"]}. Provide a clear and concise answer in a single sentence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "transformation" in t:
            criteria = ["The description should accurately reflect the final position and orientation of the shape after the transformation."]
        else:
            criteria = ["The answer should correctly describe the spatial relationship based on the given layout."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
