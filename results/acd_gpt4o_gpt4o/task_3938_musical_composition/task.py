class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"key": "C Major", "tempo": "120 BPM", "theme": "joyful", "length": "16 bars"},
            "2": {"key": "A Minor", "tempo": "90 BPM", "theme": "melancholic", "length": "16 bars"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        key = t["key"]
        tempo = t["tempo"]
        theme = t["theme"]
        length = t["length"]
        instructions = f"""Your task is to compose a melody based on the following constraints:\n\n- Key: {key}\n- Tempo: {tempo}\n- Theme: {theme}\n- Length: {length}\n\nEnsure that your melody adheres to the given key and tempo, and reflects the specified theme. Provide your response in plain text format using standard musical notation. Use letters for notes (e.g., C, D, E) and numbers for rhythm (e.g., '1' for whole note, '1/2' for half note, '1/4' for quarter note). Separate notes and rhythms with spaces.\n\nExample of a melody in C Major, 120 BPM, joyful theme:\nC 1/4 D 1/4 E 1/4 F 1/4 G 1/2 E 1/4 D 1/4 C 1/4 G 1/2 A 1/4 B 1/4 C 1\n\nYour melody should have a similar structure, reflecting the given key, tempo, and theme."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The melody should adhere to the given key.",
            "The melody should adhere to the given tempo.",
            "The melody should reflect the specified theme.",
            "The melody should be of the specified length."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
