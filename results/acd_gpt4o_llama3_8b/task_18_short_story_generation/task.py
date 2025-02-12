class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A lonely astronaut explores a distant planet.", "elements": ["a surprising discovery", "a moment of reflection", "a twist ending"]},
            "2": {"prompt": "A young girl discovers she has magical powers.", "elements": ["a mentor figure", "a conflict with a friend", "an unexpected ally"]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        elements = ", ".join(t["elements"])
        return f"""Generate a short story based on the following prompt: '{prompt}'. Your story should include the following narrative elements: {elements}. Ensure that the story is coherent, engaging, and incorporates all the specified elements. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and engaging.",
            "The story should include all the specified narrative elements.",
            "The story should be relevant to the given prompt.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
