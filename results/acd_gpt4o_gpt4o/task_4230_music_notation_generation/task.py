class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "theme": "happy"},
            "2": {"task_type": "interpretation", "notation": "C4 E4 G4 C5"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generation':
            return f"""Your task is to generate a simple music notation based on the following theme:

Theme: {t['theme']}

Your music notation should be clear, follow standard music notation conventions, and creatively embody the theme. Provide your response in plain text format using note names (e.g., C, D, E, F, G, A, B) with octaves (e.g., C4, D4, etc.). The sequence should be between 4 and 8 notes long. Here is an example response format:

Notation: C4 D4 E4 F4

Explanation: The sequence should embody the theme by using notes that are typically associated with a happy mood, such as major intervals. Avoid using minor intervals or dissonant notes."""
        else:
            return f"""Your task is to interpret the following music notation:

Notation: {t['notation']}

Provide a clear, step-by-step explanation of the meaning conveyed by the notation. Ensure your explanation is detailed and includes the pitch and octave of each note. Your response should be between 50 and 100 words and provided in plain text format. Here is an example response format:

Explanation: The notation consists of the notes C4, E4, G4, and C5. These notes form a C major chord, which is often associated with a happy and uplifting sound. The pitch and octave of each note are clearly indicated, with C4 being the lowest and C5 being the highest. Include why the sequence might be considered 'happy'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpretation':
            criteria = ["The explanation should accurately interpret the given music notation.", "The explanation should be detailed and include the pitch and octave of each note.", "The response should be between 50 and 100 words.", "The explanation should include why the sequence might be considered 'happy'."]
        else:
            criteria = ["The generated music notation should be clear and follow standard music notation conventions.", "The music notation should creatively embody the given theme.", "The sequence should be between 4 and 8 notes long.", "The notation should avoid using minor intervals or dissonant notes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
