class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Generate a 4-bar melody in 4/4 time signature using the C major scale. Include at least one instance of each note in the C major scale (C, D, E, F, G, A, B)."},
            "2": {"musical_piece": "G E D C D E F G A B C B A G F E D C", "criteria": "Analyze the given musical piece. Identify the key signature, time signature, and any notable patterns or repetitions in the melody."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "criteria" in t:
            return f"""Your task is to generate a musical score based on the following criteria:\n{t['criteria']}\n\nProvide your response in plain text format using the following notation:\n- C, D, E, F, G, A, B for notes\n- | for bar lines\nExample response:\nC D E F | G A B C | D E F G | A B C D\n\nEnsure that the melody follows the 4-bar structure and uses all the notes in the C major scale at least once. Double-check that the time signature is 4/4 and that each bar contains exactly 4 beats."""
        else:
            return f"""Your task is to analyze the given musical piece. Identify the key signature, time signature, and any notable patterns or repetitions in the melody.\n\nMusical piece: {t['musical_piece']}\n\nProvide your analysis in plain text format. Ensure your response is clear and well-structured with the following points:\n- Key signature: [Your answer]\n- Time signature: [Your answer]\n- Notable patterns/repetitions: [Your answer]\n\nExample response:\n- Key signature: C major\n- Time signature: 4/4\n- Notable patterns/repetitions: The melody ascends and then descends in a stepwise motion."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "criteria" in t:
            criteria = ["The melody should be a 4-bar melody in 4/4 time signature.", "The melody should use all notes of the C major scale at least once.", "Each bar should contain exactly 4 beats."]
        else:
            criteria = ["The analysis should correctly identify the key signature.", "The analysis should correctly identify the time signature.", "The analysis should identify notable patterns or repetitions in the melody."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
