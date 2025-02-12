class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "identify", "notes": "C, E, G", "question": "Identify the musical chord formed by these notes."},
            "2": {"task_type": "generate", "description": "Generate a major seventh chord starting from the note G.", "criteria": "The chord should consist of four notes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "identify":
            instructions = f"""Your task is to identify the musical chord formed by the following notes:

Notes: {t['notes']}

Question: {t['question']}

Provide your answer in plain text format as the name of the chord (e.g., 'C major')."""
        else:
            instructions = f"""Your task is to generate a musical chord based on the following description:

{t['description']}

Ensure the chord consists of four notes and is formatted as a comma-separated list of notes. For example: C, E, G, B."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "identify":
            criteria = ["The response should correctly identify the chord formed by the given notes."]
        else:
            criteria = ["The generated chord should consist of four notes.", "The chord should be a major seventh chord starting from the specified note."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
