class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "arrangement": "A large oak tree in the center of a grassy field, with a small pond to the left of the tree and a wooden bench to the right. In the background, there are rolling hills with wildflowers and a distant snow-capped mountain range. To the far left, a dirt path leads into a dense forest."
            },
            "2": {
                "arrangement": "A bustling city street with tall skyscrapers on either side. In the foreground, there is a street vendor selling fruits from a colorful cart. To the left, a bus stop with a group of people waiting, including a child holding a balloon. To the right, a coffee shop with outdoor seating where two people are engaged in conversation. Above, a clear blue sky with a few scattered clouds."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed description of the visual scene based on the following abstract spatial arrangement: {t['arrangement']}.

Ensure your description captures the spatial relationships and elements mentioned in the arrangement. Use descriptive language to bring the scene to life. Your response should be at least 150 words long. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately capture the spatial relationships and elements mentioned in the arrangement.",
            "The language should be descriptive and bring the scene to life.",
            "The response should be coherent and well-organized.",
            "The length of the submission should be at least 150 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
