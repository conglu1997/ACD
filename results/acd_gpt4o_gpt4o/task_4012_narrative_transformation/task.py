class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_narrative": "Once upon a time, in a small village, there was a young boy named Jack. Jack loved exploring the nearby forest, where he discovered a hidden cave filled with ancient treasures. One day, while exploring the cave, he found a mysterious map that led to a magical land.",
                "transformation_instructions": "Transform the narrative into a science fiction story set in a futuristic city. Maintain the key elements of exploration, discovery, and a map leading to a mysterious place."
            },
            "2": {
                "original_narrative": "In a kingdom far away, there lived a brave knight named Sir Lancelot. Sir Lancelot was known for his courage and kindness. One day, he embarked on a quest to rescue a princess from a dragon's lair. Along the way, he faced numerous challenges but never gave up.",
                "transformation_instructions": "Transform the narrative into a modern-day adventure involving a detective. Maintain the key elements of courage, a quest to rescue someone, and facing challenges along the way."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        original_narrative = t["original_narrative"]
        transformation_instructions = t["transformation_instructions"]
        instructions = f"""Your task is to transform the given narrative based on the specific instructions provided. Ensure that the transformed narrative remains coherent and retains the key elements mentioned in the instructions.

Original Narrative: {original_narrative}

Transformation Instructions: {transformation_instructions}

Provide your transformed narrative in plain text format. Ensure that it is coherent, creative, and respects the key elements specified in the instructions."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed narrative should be coherent and well-structured.",
            "The transformed narrative should creatively follow the transformation instructions.",
            "The key elements from the original narrative should be maintained in the transformed narrative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
