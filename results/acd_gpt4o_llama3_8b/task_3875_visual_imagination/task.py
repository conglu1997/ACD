class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine a futuristic city where nature and technology coexist harmoniously."},
            "2": {"prompt": "Describe an underwater world inhabited by fantastical creatures."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Generate a vivid and detailed visual description based on the following prompt: '{prompt}'. Ensure that your description includes sensory details, such as colors, sounds, textures, and any other elements that bring the scene to life. Your response should be coherent, imaginative, and at least 150 words long. Submit your response as a plain text string in the format: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be vivid and detailed.",
            "The description should be at least 150 words long.",
            "The description should include sensory details such as colors, sounds, and textures.",
            "The response should be coherent and imaginative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
