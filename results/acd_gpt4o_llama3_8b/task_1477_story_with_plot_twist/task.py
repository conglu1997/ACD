class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "A detective is investigating a series of mysterious disappearances in a small town."
            },
            "2": {
                "prompt": "A scientist discovers a new element that has the potential to revolutionize energy production."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['prompt']
        return f"""Generate a short story (between 300 to 500 words) based on the following prompt. Your story should include a surprising plot twist that is coherent and logically consistent with the rest of the narrative.

Prompt: {prompt}

Your story should be creative, engaging, and maintain narrative coherence even with the introduction of a plot twist. Submit your story as a plain text string in the following format:

Story: [Your Story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be based on the given prompt.",
            "The story should include a surprising plot twist.",
            "The plot twist should be coherent and logically consistent with the rest of the narrative.",
            "The story should be engaging and demonstrate creativity.",
            "The story should be between 300 to 500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
