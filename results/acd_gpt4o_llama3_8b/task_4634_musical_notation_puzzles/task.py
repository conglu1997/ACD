class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the following musical notation and identify the key signature, time signature, and any notable patterns or motifs.\n\nNotation: G, A, B, C, D, E, F#, G (Treble Clef), 4/4 time signature, Key Signature: 1 sharp"},
            "2": {"prompt": "Solve the following puzzle based on the given musical notation and theory. Identify the chord progression and explain the harmonic function of each chord.\n\nNotation: C, E, G (Chord 1), G, B, D (Chord 2), A, C, E (Chord 3), F, A, C (Chord 4), 4/4 time signature"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "key signature" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nEnsure that your analysis adheres to the following requirements:\n1. Identify the key signature based on the provided notation.\n2. Identify the time signature.\n3. Describe any notable patterns or motifs present in the notation.\n4. Ensure that your response is logically structured and coherent.\n\nSubmit your response as a plain text string in the following format:\n\nResponse: [Your detailed analysis here]"""
        else:
            return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nEnsure that your analysis adheres to the following requirements:\n1. Identify the chord progression based on the provided notation.\n2. Explain the harmonic function of each chord in the progression.\n3. Provide any relevant examples of similar chord progressions if possible.\n4. Ensure that your response is logically structured and coherent.\n\nSubmit your response as a plain text string in the following format:\n\nResponse: [Your detailed analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "key signature" in t["prompt"]:
            criteria = ["Identify the key signature based on the provided notation.", "Identify the time signature.", "Describe any notable patterns or motifs present in the notation.", "Ensure that the response is logically structured and coherent.", "The response should integrate all provided data points accurately."]
        else:
            criteria = ["Identify the chord progression based on the provided notation.", "Explain the harmonic function of each chord in the progression.", "Provide any relevant examples of similar chord progressions if possible.", "Ensure that the response is logically structured and coherent.", "The response should integrate all provided data points accurately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
