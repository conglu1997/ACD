class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"key": "C Major", "meter": "4/4", "motif": "C D E F"},
            "2": {"key": "G Minor", "meter": "3/4", "motif": "G A Bb"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        key = t["key"]
        meter = t["meter"]
        motif = t["motif"]
        instructions = f"""Your task is to compose a short piece of music based on the following constraints:

Key: {key}
Meter: {meter}
Motif: {motif}

Please provide your composition in plain text format using standard musical notation. Ensure that your piece is coherent, adheres to the given key and meter, and incorporates the given motif prominently. The composition should be at least 16 bars long. The motif should appear at least twice in the piece."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should adhere to the specified key.",
            "The composition should adhere to the specified meter.",
            "The composition should incorporate the given motif at least twice.",
            "The composition should be at least 16 bars long.",
            "The composition should be coherent and musically sensible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
