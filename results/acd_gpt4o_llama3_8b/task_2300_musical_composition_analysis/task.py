class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"music_snippet": "C E G B D F A C, rhythmic pattern: 1 0.5 0.5 1 0.5 0.5 1 1"},
            "2": {"music_snippet": "E G# B D F# A C# E, rhythmic pattern: 0.5 0.5 1 0.5 0.5 1 1 1"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        music_snippet = t["music_snippet"]
        return f"""Analyze the following music snippet for its compositional elements (e.g., scale, key, chord progression, rhythm, etc.): '{music_snippet}'. After analyzing the snippet, create a new piece of music that employs similar techniques. Ensure your explanations are clear and your new composition is creative and original. Submit your response as a plain text string with the following sections labeled: 'Analysis', 'Explanation', and 'New Composition'.

Example format:
Analysis:
1. Compositional element 1
2. Compositional element 2

Explanation:
1. Explanation of compositional element 1
2. Explanation of compositional element 2

New Composition:
1. New music snippet using compositional element 1
2. New music snippet using compositional element 2

Example response:
Analysis:
1. Scale: Major
2. Rhythm: Steady quarter notes

Explanation:
1. The music snippet is in a major scale, which gives it a bright and happy sound.
2. The rhythm is composed of steady quarter notes, creating a simple and regular beat.

New Composition:
1. Scale: C E G B D F A C
2. Rhythm: C (quarter note), E (eighth note), G (eighth note), B (quarter note), D (eighth note), F (eighth note), A (quarter note), C (quarter note)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The compositional elements should be correctly identified.",
            "The explanations should be clear and accurate.",
            "The new composition should creatively and correctly employ the identified techniques.",
            "The response should follow the provided format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
