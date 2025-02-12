class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine a futuristic cityscape painting featuring flying cars, towering skyscrapers with neon lights, and people in advanced suits. Include details such as a hovering billboard displaying advertisements, a robot vendor, and the reflection of the city lights on wet pavement. Describe this painting in detail, including colors, composition, and mood."},
            "2": {"prompt": "Imagine a serene countryside landscape painting with a flowing river, lush green fields dotted with wildflowers, a small stone cottage with smoke coming out of the chimney, and people enjoying a picnic under a large oak tree. Include details such as the sound of birds chirping, the gentle breeze rustling the leaves, and the sunlight filtering through the tree branches. Describe this painting in detail, including colors, composition, and mood."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['prompt']
        return f"Generate a detailed description of an artwork based on the following prompt: {prompt}. Ensure that your description includes details about colors, composition, and mood. Submit your description as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be detailed and vivid.",
            "The description should cover colors, composition, and mood.",
            "The description should align with the given prompt and include all specified elements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
