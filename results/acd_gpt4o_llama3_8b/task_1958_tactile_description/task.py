class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe the tactile experience of touching a piece of silk fabric. Include details about its texture, temperature, and any emotions it evokes."},
            "2": {"prompt": "Describe the tactile experience of holding a smooth, polished stone in your hand. Include details about its weight, texture, temperature, and any emotions it evokes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Complete the following task based on the given prompt:\n\n{prompt}\n\nSubmit your response as a plain text string. Your response should be structured as follows:\n\nDescription: [Detailed description here, 100-200 words]\n\nInterpretation: [Interpretation of the tactile experience including any emotions it evokes, 100-200 words]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should provide detailed and vivid sensory information about the tactile experience.",
            "The interpretation should include thoughtful insights into the emotions or sensations evoked by the tactile experience.",
            "The response should follow the given format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
