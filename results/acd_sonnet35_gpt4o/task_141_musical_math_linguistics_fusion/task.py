import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'math_sequence': 'Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, ...)',
                'linguistic_pattern': 'Alliteration',
                'musical_element': 'Rhythm',
                'scale': 'Pentatonic (C, D, E, G, A)'
            },
            {
                'math_sequence': 'Prime number sequence (2, 3, 5, 7, 11, 13, ...)',
                'linguistic_pattern': 'Rhyme scheme (ABAB)',
                'musical_element': 'Melody',
                'scale': 'Chromatic (all 12 semitones)'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a musical structure that integrates the {t['math_sequence']}, the linguistic pattern of {t['linguistic_pattern']}, and focuses on the musical element of {t['musical_element']} using the {t['scale']} scale.

This task combines mathematical sequences, linguistic patterns, and musical elements to test interdisciplinary knowledge integration and creative problem-solving.

Your task:
1. Design a short musical piece (4 measures) that incorporates these elements.
2. Provide a textual representation of your musical structure using the following notation:
   - Use letters (A-G) to represent notes
   - Use numbers (1-4) to represent note durations (1 = quarter note, 2 = half note, 4 = whole note)
   - Use '-' for rests (e.g., -1 for a quarter rest)
   - Use '|' to separate measures
   Example: C1 D2 E1 | G2 -2 | C1 A1 G1 E1 | C4 |

3. Explain how your musical structure incorporates each element:
   a) Mathematical sequence: Describe how the sequence is used in note selection or rhythm.
   b) Linguistic pattern: Provide a 4-line text that fits the music and demonstrates the linguistic pattern.
   c) Musical element: Explain how the specified element is emphasized in your composition.
   d) Scale: List the specific notes from the given scale that you used.

4. Identify one potential challenge in performing this piece and propose a solution.

5. Briefly discuss how this fusion of mathematics, linguistics, and music might reveal one insight about pattern recognition in AI systems.

Example (do not use this exact response):
Musical Structure:
C1 E1 G2 | C2 G1 E1 | G1 E1 C2 | G4 |

Explanation:
a) Mathematical sequence: The Fibonacci sequence is used for note durations (1, 1, 2, 2, 1, 1, 1, 1, 2, 4).
b) Linguistic pattern:
Careful cats create chaos,
Curious canines cause commotion.
Clever crows caw constantly,
Crafty creatures' cacophony.
Alliteration is used with the repetition of the 'c' sound at the beginning of words.
c) Musical element: The rhythm follows a pattern of short-short-long, emphasizing the rhythmic aspect.
d) Scale: C, E, G (from the pentatonic scale)

Challenge and Solution:
Challenge: Maintaining precise rhythm while emphasizing alliteration in performance.
Solution: Practice with a metronome and exaggerate consonant sounds.

Insight on AI Pattern Recognition:
This task demonstrates how AI systems might need to integrate patterns across different domains (math, language, music) to generate creative and coherent outputs, highlighting the importance of interdisciplinary learning in AI.

Format your response as follows:

Musical Structure:
[Your 4-measure textual representation]

Explanation:
a) Mathematical sequence: [Your explanation]
b) Linguistic pattern:
[Your 4-line text]
[Explanation of how it fits the pattern]
c) Musical element: [Your explanation]
d) Scale: [List of used notes]

Challenge and Solution:
[Identify one challenge and propose a solution]

Insight on AI Pattern Recognition:
[Brief discussion of one insight]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The musical structure is provided in the correct 4-measure format using the specified notation.",
            f"The explanation clearly demonstrates how the {t['math_sequence']} is incorporated into the musical structure.",
            f"A 4-line text demonstrating the {t['linguistic_pattern']} is provided and correctly explained.",
            f"The explanation shows how the {t['musical_element']} is emphasized in the composition.",
            f"The used notes from the {t['scale']} scale are correctly listed and match the musical structure.",
            "A specific performance challenge and viable solution are identified.",
            "A relevant and thoughtful insight about AI pattern recognition is briefly discussed.",
            "The response demonstrates integration of mathematical, linguistic, and musical elements in a creative and coherent manner."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
