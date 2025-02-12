class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe the auditory experience of listening to a gentle rain shower with occasional thunder. Include details about the sounds, the atmosphere it creates, and any emotions it evokes."},
            "2": {"prompt": "Describe the auditory experience of being in a busy city street during rush hour, with honking cars, people talking, and street performers. Include details about the various sounds you hear, the atmosphere it creates, and any emotions it evokes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Complete the following task based on the given prompt:\n\n{prompt}\n\nSubmit your response as a plain text string. Your response should be structured as follows:\n\nDescription: [Detailed description here, 100-200 words]\n\nInterpretation: [Interpretation of the auditory experience including any emotions it evokes, 100-200 words]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should provide detailed and vivid sensory information about the auditory experience.",
            "The interpretation should include thoughtful insights into the emotions or sensations evoked by the auditory experience.",
            "The response should follow the given format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
