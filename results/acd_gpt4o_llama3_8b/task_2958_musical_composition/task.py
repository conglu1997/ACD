class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"mood": "happy", "example_chord_progression": "C - G - Am - F", "example_melody": "C E G E D C E F G E"},
            "2": {"mood": "sad", "example_chord_progression": "Am - F - C - G", "example_melody": "A C E C B A C D E C"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        mood = t["mood"]
        example_chord_progression = t["example_chord_progression"]
        example_melody = t["example_melody"]
        return f"""Your task is to create a chord progression and a corresponding melody that reflects the specified mood: {mood}.

A chord progression is a series of chords played in sequence. Each chord can be represented by a letter (e.g., C, G, Am, F). The melody should be a sequence of notes that fit well with the chord progression. Each note can be represented by a letter (e.g., C, D, E, F, G, A, B).

Here is an example of a chord progression and melody for the mood '{mood}':

Chord Progression: {example_chord_progression}
Melody: {example_melody}

Submit your chord progression as a plain text string in the format 'Chord Progression: [your chord progression]'.
Submit your melody as a plain text string in the format 'Melody: [your melody]'. Ensure that each chord and note is separated by a space."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        submission_lines = submission.strip().split('\n')
        if len(submission_lines) != 2 or not submission_lines[0].startswith('Chord Progression:') or not submission_lines[1].startswith('Melody:'):
            return 0.0
        criteria = [
            "The chord progression should consist of at least 4 chords and reflect the specified mood.",
            "The melody should fit well with the chord progression and reflect the specified mood.",
            "The submission should follow the specified format for chord progression and melody."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
