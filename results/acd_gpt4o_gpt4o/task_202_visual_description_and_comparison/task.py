class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_description": "A photograph of a bustling city street during the day, with people walking on the sidewalks, cars driving by, and tall buildings in the background. Notice the variety of people, the types of vehicles, and any advertisements or signs visible."},
            "2": {"image_description_1": "A serene beach at sunset with waves gently crashing onto the shore, a few people walking along the water's edge, and the sky painted in hues of orange and pink. Notice the details of the beach, the colors in the sky, and the presence of any objects or people.", "image_description_2": "A quiet forest path in autumn, with fallen leaves covering the ground, trees with golden and red foliage, and a soft light filtering through the branches. Notice the details of the foliage, the path, and any objects or animals present."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "image_description" in t:
            return f"Your task is to generate a detailed textual description of the following visual scene: \n\nScene: {t['image_description']}\n\nEnsure your description is vivid, clear, and captures all relevant details of the scene, including people, objects, colors, and any visible text. Provide your description in plain text format."
        else:
            return f"Your task is to compare the following two visual descriptions and highlight their similarities and differences: \n\nDescription 1: {t['image_description_1']}\n\nDescription 2: {t['image_description_2']}\n\nEnsure your comparison is thorough, clear, and captures all relevant aspects of both descriptions, including details, colors, objects, and overall atmosphere. Provide your comparison in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "image_description" in t:
            criteria = [
                "The description should be vivid, clear, and capture all relevant details of the scene, including people, objects, colors, and any visible text.",
                "The description should be coherent and well-structured."]
        else:
            criteria = [
                "The comparison should highlight both similarities and differences.",
                "The comparison should be thorough, clear, and well-structured.",
                "The comparison should include details, colors, objects, and overall atmosphere."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
