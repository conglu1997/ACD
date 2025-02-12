class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "prompt": "Compose a simple melody in C major using quarter notes and half notes."},
            "2": {"task_type": "interpretation", "notation": "C4 E4 G4 C5 | G4 E4 C4 G4"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == "generation":
            return f"""Your task is to generate a simple musical melody based on the following prompt:\n\nPrompt: {t['prompt']}\n\nProvide your response in plain text format using standard musical notation (e.g., C4 E4 G4 C5). Ensure the melody is coherent, follows the given constraints, and is presented in a readable format."""
        elif t['task_type'] == "interpretation":
            return f"""Your task is to interpret the following musical notation and describe the melody in detail:\n\nNotation: {t['notation']}\n\nProvide your response in plain text format. Ensure that your description captures the rhythm, notes, intervals, and overall structure of the melody. Describe any patterns or repetitions you observe."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == "generation":
            criteria = ["The melody should be in C major and use only quarter notes and half notes.", "The melody should be coherent, follow the given constraints, and be presented in a readable format."]
        elif t['task_type'] == "interpretation":
            criteria = ["The description should accurately capture the rhythm, notes, intervals, and overall structure of the melody.", "The description should mention any patterns or repetitions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
