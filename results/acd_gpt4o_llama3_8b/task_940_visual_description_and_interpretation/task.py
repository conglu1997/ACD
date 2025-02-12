class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scene": "A bustling city street with people walking, cars driving, various storefronts, a street musician playing a guitar, and a dog chasing a ball."},
            "2": {"scene": "A serene beach at sunset with waves gently crashing, seagulls flying, a silhouette of a couple walking, a child building a sandcastle, and a sailboat in the distance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following visual scene, describe it in detail. Your description should cover key elements such as people, objects, activities, and overall atmosphere. Additionally, interpret the significance of at least two key visual elements in the scene. Submit your response as a plain text string in the following format:\n\nDescription: [Your detailed description]\nInterpretation: [Your interpretation of two key visual elements]\n\nScene: {t['scene']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be detailed and cover key elements such as people, objects, activities, and overall atmosphere.", "The interpretation should accurately explain the significance of at least two key visual elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
