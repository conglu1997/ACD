class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A cat is sitting to the left of a dog. A bird is flying above the dog. A mouse is hiding under a table to the right of the cat. Describe the spatial relationships between the cat, dog, bird, and mouse.",
                "instructions": "Interpret the spatial relationships described and provide a clear, concise description of the positions of the cat, dog, bird, and mouse relative to each other. Submit your response as a plain text string."
            },
            "2": {
                "description": "There is a tree in the center of a garden. A bench is placed 5 meters north of the tree. A fountain is 3 meters south-east of the tree. A statue is 2 meters west of the bench. Describe the spatial relationships between the tree, bench, fountain, and statue.",
                "instructions": "Interpret the spatial relationships described and provide a clear, concise description of the positions of the tree, bench, fountain, and statue relative to each other. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the spatial relationships described in the following text and provide a clear, concise description of the positions of the objects relative to each other: {t['description']} Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description must accurately reflect the spatial relationships described in the text.",
            "The response should be clear and concise.",
            "The spatial relationships should be logically consistent and easy to understand."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
