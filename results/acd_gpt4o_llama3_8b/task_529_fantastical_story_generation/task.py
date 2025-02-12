class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a world where gravity works in reverse, and people live in floating cities. Include a character who dreams of reaching the ground."},
            "2": {"prompt": "Write a short story about a magical library where every book can transport the reader into the story. Include a character who gets trapped in a book and must find a way out."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Generate a short story based on the following prompt:

Prompt: {prompt}

Ensure that your story is creative, coherent, and engaging. The story should be between 300 to 500 words. Submit your response as a plain text string in the following format:

Story: [Your short story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be creative and engaging.",
            "The narrative should be coherent and logically structured.",
            "The story should adhere to the prompt and include the specified elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
