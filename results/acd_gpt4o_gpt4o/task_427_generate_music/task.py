class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Compose a 4-bar melody in 4/4 time signature using standard musical notation. The melody should start with a C note and end with a G note. Use at least one rest and include a variety of note durations. Describe the melody in plain text and provide the musical notation."},
            "2": {"description": "Compose a 2-bar rhythm pattern in 3/4 time signature using standard musical notation. The rhythm should include at least one dotted note and one triplet. Describe the rhythm in plain text and provide the musical notation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a musical composition based on the given constraints. Use standard musical notation to represent the composition. Ensure that the notation is clear, accurate, and adheres to the given constraints. Here is the information about the task:\n\n{t['description']}\n\nSubmit your composition in plain text format using standard musical notation symbols. Describe the composition in plain text and provide the corresponding musical notation.\n\nExample format for musical notation:\n\nC4 E4 G4 | F4 E4 D4 | C4 D4 E4 | G4 R R R\n\nThis indicates a melody where each note's pitch and duration are clearly specified. Include the bar lines (|) to separate the measures. Use 'R' to represent rests if needed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should use standard musical notation.",
            "The composition should adhere to the given constraints.",
            "The notation should be clear and accurate.",
            "The composition should be musically coherent.",
            "The composition should include a variety of note durations.",
            "The description should match the notation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
