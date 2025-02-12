class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"visual_description": "A serene beach at sunset with waves gently crashing against the shore, a lone seagull in the sky, and a couple walking hand-in-hand along the water's edge."},
            "2": {"visual_description": "A bustling city street at night, illuminated by neon signs and streetlights, with people hurrying to and fro, a street musician playing a saxophone, and a food vendor serving hot dogs."},
            "3": {"visual_description": "A dense forest with towering trees, dappled sunlight filtering through the leaves, a deer grazing near a babbling brook, and a child exploring the undergrowth with a sense of wonder."},
            "4": {"visual_description": "A futuristic cityscape with towering skyscrapers, flying cars zipping through the air, holographic advertisements, and people in modern attire walking along elevated walkways."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a creative narrative or description based on the following visual prompt described in text. Ensure your narrative is engaging, coherent, and vividly brings the scene to life. Here is the visual description:\n\n{t['visual_description']}\n\nSubmit your narrative in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should be engaging and imaginative.", "The narrative should be coherent and logically structured.", "The narrative should vividly bring the scene to life based on the visual description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
