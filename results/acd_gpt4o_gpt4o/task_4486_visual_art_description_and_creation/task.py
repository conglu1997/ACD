class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_piece": "A painting of a serene lake surrounded by mountains during sunset.", "criteria": "Generate a description of a new art piece that evokes a sense of mystery and uses a forest as the main setting."},
            "2": {"art_piece": "A sculpture of an abstract human figure with elongated limbs in a dynamic pose.", "criteria": "Generate a description of a new art piece that symbolizes freedom and uses a bird as the main element."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given visual art piece and generate a new visual art concept based on the specified criteria.

Art Piece: {t['art_piece']}
Criteria: {t['criteria']}

Provide the description of the new art piece in a clear and detailed manner, ensuring it aligns with the given criteria."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The new art piece description must evoke the intended emotion specified in the criteria.", "The description should be detailed and vivid.", "The main element of the art piece should align with the criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
