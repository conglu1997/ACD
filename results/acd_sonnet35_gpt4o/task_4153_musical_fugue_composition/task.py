import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        subjects = [
            "C4 D4 E4 C4",
            "G4 F4 E4 D4",
            "A4 G4 F4 E4",
            "D4 F4 A4 D5"
        ]
        composers = [
            "J.S. Bach",
            "G.F. Handel",
            "W.A. Mozart",
            "L. van Beethoven"
        ]
        return {
            "1": {"subject": random.choice(subjects), "composer": random.choice(composers)},
            "2": {"subject": random.choice(subjects), "composer": random.choice(composers)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""A fugue is a type of musical composition where a short melody (the subject) is introduced and then repeated in different voices, often with variations. Your task is to compose a simple musical fugue based on the given subject: {t['subject']}. Then, analyze its structure, emotional impact, and historical context. Your response should include:

1. Fugue Composition (200-250 words):
   a) Describe the structure of your fugue, including the number of voices (minimum 2) and key.
   b) Explain how you develop the subject throughout the fugue.
   c) Provide a textual representation of the exposition of your fugue, using standard musical notation. For example:
      Voice 1: C4 D4 E4 C4 | F4 G4 A4 F4 | G4 A4 B4 G4 |
      Voice 2: --- --- --- --- | C4 D4 E4 C4 | F4 G4 A4 F4 |

2. Structural and Emotional Analysis (200-250 words):
   a) Analyze the contrapuntal techniques used in your fugue.
   b) Describe the overall emotional character of your fugue.
   c) Explain how specific elements (e.g., rhythm, harmony, texture) contribute to this emotional impact.

3. Historical Context (150-200 words):
   a) Compare your fugue to the style of {t['composer']}.
   b) Discuss how your composition reflects or diverges from historical fugue writing practices.

4. Creative Variation (100-150 words):
   a) Propose one creative variation on your fugue that significantly alters its character.
   b) Explain how this variation would affect the emotional impact of the piece.

5. Cross-Domain Application (150-200 words):
   a) Suggest how the concept of a fugue (a theme repeated and developed in different 'voices') could be applied to a non-musical field of your choice.
   b) Briefly explain how this application would work and what insights it might provide.

Ensure your response demonstrates an understanding of music theory and composition techniques. Use appropriate musical terminology and provide clear explanations for your choices.

Format your response with clear headings for each section. Your total response should be between 800-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a simple fugue composition based on the given subject.",
            "The structural and emotional analysis demonstrates an understanding of basic contrapuntal techniques and emotional expression in music.",
            "The historical context section provides a reasonable comparison to the specified composer's style.",
            "The creative variation proposed alters the character of the fugue in a meaningful way.",
            "The cross-domain application demonstrates an understanding of the basic concept of a fugue and its potential application outside of music.",
            "The response uses appropriate musical terminology.",
            "The textual representation of the fugue uses standard musical notation correctly."
        ]
        scores = [float(eval_with_llm_judge(instructions, submission, [criterion])) for criterion in criteria]
        return sum(scores) / len(criteria)
