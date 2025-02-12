class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Compose a short piece of music for a solo piano in the style of a classical waltz. The piece should be in 3/4 time signature with a tempo of 120 beats per minute and should include at least 16 measures."},
            "2": {"prompt": "Analyze the following musical piece: 'Für Elise' by Ludwig van Beethoven. Your analysis should include the structure of the piece, key motifs, and the emotional impact of the music."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "Compose" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Your composition should be:
1. In 3/4 time signature.
2. At a tempo of 120 beats per minute.
3. At least 16 measures long.

Submit your composition as a plain text string in a format that clearly describes the notes and their durations, such as MIDI or ABC notation. For example:

C4/4 D4/4 E4/4 | F4/4 G4/4 A4/4 | ... (continue for 16 measures)"""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Your analysis should include:
1. The structure of the piece (e.g., ABA, sonata form).
2. Key motifs and themes present in the music.
3. The emotional impact and how it is achieved through musical elements.

For example, an analysis might look like this:

Structure: The piece follows an ABA form, with the main theme introduced in the A section, followed by a contrasting B section, and then a return to the main theme in the A section.

Motifs: The piece features a recurring motif of a short, descending melodic line that creates a sense of longing.

Emotional Impact: The use of dynamics and tempo variations throughout the piece creates a sense of ebb and flow, enhancing the emotional impact of the music.

Ensure your analysis is detailed, accurate, and demonstrates a deep understanding of musical theory. Submit your analysis as a plain text string in the following format:

Structure:
[Your detailed analysis of the structure]

Motifs:
[Your detailed analysis of the key motifs]

Emotional Impact:
[Your detailed analysis of the emotional impact]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "Compose" in t["prompt"]:
            criteria = ["The composition should be in 3/4 time signature.", "The tempo should be 120 beats per minute.", "The piece should include at least 16 measures.", "The notes and durations should be clearly described."]
        else:
            criteria = ["The analysis should cover the structure of the piece.", "The analysis should identify key motifs and themes.", "The analysis should discuss the emotional impact of the music.", "The analysis should be structured into sections: Structure, Motifs, and Emotional Impact."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
