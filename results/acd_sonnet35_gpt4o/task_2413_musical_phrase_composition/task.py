import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        techniques = [
            {
                "technique": "Retrograde",
                "constraint": "Use only quarter notes and eighth notes",
                "explanation": "Retrograde involves reversing the order of notes in a musical phrase."
            },
            {
                "technique": "Inversion",
                "constraint": "Use a C major pentatonic scale (C, D, E, G, A)",
                "explanation": "Inversion involves flipping the intervals of a melody upside down."
            },
            {
                "technique": "Augmentation",
                "constraint": "Start and end on the tonic note (first note of the scale)",
                "explanation": "Augmentation involves doubling the duration of each note in a melody."
            }
        ]
        return {str(i+1): technique for i, technique in enumerate(random.sample(techniques, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical phrase using the compositional technique of {t['technique']} and adhering to the following constraint: {t['constraint']}. {t['explanation']}

For techniques that don't specify a key or scale, use C major scale (C, D, E, F, G, A, B).

Your task has four parts:

1. Original Phrase (exactly 8 measures):
   - Compose a musical phrase that demonstrates the specified technique.
   - Ensure your phrase adheres to the given constraint.
   - Represent your phrase using the following format: [Note][Octave][Duration], e.g., "C4 q, D4 e, E4 e, F4 q" where q = quarter note, e = eighth note, h = half note, w = whole note.
   - Example of a correctly formatted measure: "C4 q, D4 e, E4 e, F4 q"

2. Technique Application (3-4 sentences):
   - Explain how you applied the {t['technique']} technique in your phrase.
   - Describe how you incorporated the constraint into your composition.
   - Provide a brief example of how the phrase would sound different without applying the technique.

3. Musical Analysis (5-6 sentences):
   - Analyze the melodic contour of your phrase.
   - Discuss any interesting harmonic implications.
   - Explain how your phrase might function within a larger musical structure.
   - Describe the emotional or stylistic character of your phrase.
   - Discuss how the technique and constraint influence the overall musical effect.

4. Creative Variation (2-3 sentences):
   - Suggest a creative way to further develop or vary your phrase while maintaining the original technique and constraint. Describe this variation; do not notate it.

Ensure your composition and analysis demonstrate a clear understanding of music theory and the specified technique. Be creative within the given constraints.

Format your response as follows:

Original Phrase:
[Your musical phrase here]

Technique Application:
[Your explanation here]

Musical Analysis:
[Your analysis here]

Creative Variation:
[Your suggestion here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The musical phrase should correctly apply the {t['technique']} technique",
            f"The phrase should adhere to the constraint: {t['constraint']}",
            "The phrase should be exactly 8 measures long and use the specified notation format",
            "The technique application explanation should accurately describe how the technique was used and include an example of how the phrase would sound different without the technique",
            "The musical analysis should demonstrate understanding of melodic contour, harmonic implications, musical structure, and the influence of the technique and constraint",
            "The creative variation suggestion should be consistent with the original technique and constraint",
            "The response should follow the specified format"
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
