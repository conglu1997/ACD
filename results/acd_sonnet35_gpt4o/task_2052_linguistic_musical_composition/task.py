import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_structures = [
            "syntax tree for 'The cat that the dog chased quickly ate the mouse'",
            "phonological rule for vowel harmony and consonant assimilation in Finnish",
            "semantic network for 'time' and 'space' concepts in Hopi language",
            "morphological paradigm for Arabic broken plurals"
        ]
        musical_elements = [
            "melody and counterpoint",
            "harmony and chord progressions",
            "rhythm and meter",
            "timbre and orchestration"
        ]
        return {
            "1": {"structure": random.choice(linguistic_structures), "element": random.choice(musical_elements)},
            "2": {"structure": random.choice(linguistic_structures), "element": random.choice(musical_elements)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""In this task, you will create a musical composition based on a linguistic structure and use it to solve a language-based puzzle. Follow these steps:

1. Linguistic-Musical Mapping (200-250 words):
   a) Create a system for mapping the linguistic structure of {t['structure']} to the musical elements of {t['element']}.
   b) Explain how specific aspects of the linguistic structure correspond to features of the musical elements.
   c) Provide an example of how a simple linguistic construct would be represented musically using your system.

2. Composition Creation (250-300 words):
   a) Using your mapping system, create a short musical composition based on the given linguistic structure: {t['structure']}.
   b) Describe the composition in detail, explaining how each part represents the linguistic structure.
   c) Provide a brief musical notation or textual representation of your composition (e.g., "C4 quarter note, D4 half note, rest, E4 eighth note").
   d) Discuss any challenges you encountered in translating the linguistic structure to music and how you resolved them.

3. Reverse Translation Puzzle (200-250 words):
   a) Present a puzzle where the goal is to decipher a specific linguistic structure from a given musical phrase using your mapping system.
   b) Provide the 'musical phrase' in text format, describing its key features (e.g., "A repeating pattern of three short notes followed by one long note, with rising pitch").
   c) Explain the steps one would take to solve the puzzle and uncover the underlying linguistic structure.
   d) Provide the correct answer to your puzzle, but encrypt it using a simple substitution cipher (e.g., A=1, B=2, etc.).

4. Analysis and Implications (200-250 words):
   a) Analyze the strengths and limitations of your linguistic-musical mapping system.
   b) Discuss how this approach might reveal new insights about the chosen linguistic structure or language processing in general.
   c) Propose an extension or variation of your system that could be applied to other areas of linguistics or cognitive science.

5. Creative Application (150-200 words):
   a) Suggest an innovative, real-world application of your linguistic-musical mapping system.
   b) Explain how this application could benefit fields such as language learning, music therapy, or computational creativity.

Ensure your response demonstrates a deep understanding of both linguistics and music theory. Be creative in your approach while maintaining logical consistency in your mapping system. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear and creative mapping between the {t['structure']} and {t['element']}.",
            "The musical composition based on the linguistic structure is well-described and logically consistent, including a brief musical notation or textual representation.",
            "The reverse translation puzzle is challenging yet solvable using the established mapping system, with an encrypted correct answer provided.",
            "The analysis shows deep understanding of both linguistic and musical concepts.",
            "The proposed real-world application is innovative and well-explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
