class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Generate a simple melody in C major using quarter notes and eighth notes. The melody should be 4 bars long and must include at least one rest.", "constraints": "Key: C major, Note durations: quarter notes and eighth notes, Length: 4 bars, Include at least one rest"},
            "2": {"description": "Interpret the provided musical score and describe the melody in natural language, including note sequences, rhythms, and any notable patterns.", "score": "C4 E4 G4 C5 | G4 F4 E4 D4 | C4 C4 E4 G4 | G4 F4 E4 D4"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'constraints' in t:
            return f"""Your task is to generate a simple melody based on the given constraints. Ensure that the melody adheres to the specified key, note durations, and length. Include at least one rest.

Constraints: {t['constraints']}

Provide your melody in musical notation format (e.g., C4 E4 G4 C5 | G4 F4 E4 D4)."""
        else:
            return f"""Your task is to interpret the provided musical score and describe the melody in natural language. Ensure that your description captures the key elements of the melody, including note sequences, rhythms, and any notable patterns.

Musical Score: {t['score']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'constraints' in t:
            criteria = ["The generated melody should be in C major.", "The melody should use only quarter notes and eighth notes.", "The melody should be 4 bars long.", "The melody should include at least one rest."]
        else:
            criteria = ["The description should accurately capture the note sequences in the provided score.", "The description should include rhythms and any notable patterns.", "The description should be coherent and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
