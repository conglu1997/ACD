class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Compose a 16-bar melody in C major, including a simple harmony using chords I, IV, and V. The melody should be suitable for a beginner pianist."
            },
            "2": {
                "constraints": "Compose a short piece of music (8 bars) in 3/4 time signature, in the key of G minor. Include a simple harmonic progression and a contrasting middle section."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t['constraints']
        return f"""Compose a piece of music based on the following constraints: {constraints}. Ensure that the piece adheres to the given key, time signature, and harmonic structure. Submit your composition as a plain text string in the format:

[Bar 1]: [Notes] [Chords]
[Bar 2]: [Notes] [Chords]
...

For example:

[Bar 1]: C E G [C]
[Bar 2]: D F A [G]
[Bar 3]: E G B [F]
[Bar 4]: F A C [G]
[Bar 5]: G B D [C]
...

Remember to:
1. Adhere to the key (e.g., C major or G minor).
2. Follow the specified time signature (e.g., 4/4 or 3/4).
3. Use the given harmonic progression (e.g., I, IV, V chords).
4. Ensure the melody is suitable for the specified instrument or level.
5. Include the specified number of bars in your composition.
6. Double-check that your composition meets all constraints before submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should adhere to the given key.",
            "The composition should follow the specified time signature.",
            "The harmonic progression should use the specified chords.",
            "The melody should be suitable for the given instrument or level.",
            "The composition should include the specified number of bars.",
            "The composition should be clearly formatted as specified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
