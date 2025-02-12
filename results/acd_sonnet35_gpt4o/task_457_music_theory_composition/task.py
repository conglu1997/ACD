import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "Polyrhythm",
                "description": "The simultaneous use of two or more conflicting rhythms that are not readily perceived as deriving from one another.",
                "example": "3 against 2: A rhythm that superimposes a division of 3 against a division of 2 over the same time span."
            },
            {
                "concept": "Modal Interchange",
                "description": "The borrowing of chords from a parallel key (same tonic, different mode).",
                "example": "Using chords from C minor in a piece in C major, such as borrowing an Ab major chord (bVI) in a C major progression."
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given musical concept and compose a short musical piece that demonstrates your understanding and creative application of the concept. Your task has the following parts:

1. Concept Analysis (100-150 words):
   Explain the musical concept of {t['concept']} in your own words. Discuss its significance in music theory and how it affects the listener's experience.

2. Composition Description (200-250 words):
   Describe a short musical piece (16-32 measures) that demonstrates the use of {t['concept']}. Your description should include:
   a) The overall structure of the piece (e.g., AABA form, theme and variations)
   b) The key or mode of the piece
   c) A detailed explanation of how you incorporated {t['concept']} into your composition
   d) Any other notable musical elements or techniques used

3. Notational Representation (100-150 words):
   Provide a textual representation of a key section of your composition that specifically demonstrates {t['concept']}. Use a combination of note names, rhythm indicators, and any other relevant musical notation symbols. Explain how to interpret your notation.

4. Creative Rationale (100-150 words):
   Explain your creative decisions in composing this piece. How does your use of {t['concept']} contribute to the overall musical expression? What mood or emotion were you aiming to convey?

5. Listening Guide (100-150 words):
   Write a brief guide for a listener, explaining what they should pay attention to in your composition to appreciate your use of {t['concept']}. Include any challenges they might face in perceiving this musical element and how to overcome them.

Ensure your response demonstrates a deep understanding of music theory and composition techniques. Be creative in your approach while maintaining musical coherence and adhering to established theoretical principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the musical concept '{t['concept']}'",
            "The composition description is detailed and coherent, showing how the concept is applied",
            "The notational representation is clear and accurately demonstrates the musical concept",
            "The creative rationale shows thoughtful consideration of how the concept contributes to musical expression",
            "The listening guide provides helpful insights for appreciating the use of the concept in the composition"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
