import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "math_concept": "Golden Ratio",
                "cultural_tradition": "West African",
                "musical_element": "Rhythm"
            },
            {
                "math_concept": "Fractal Geometry",
                "cultural_tradition": "Indian Classical",
                "musical_element": "Melody"
            },
            {
                "math_concept": "Modular Arithmetic",
                "cultural_tradition": "Javanese Gamelan",
                "musical_element": "Harmony"
            },
            {
                "math_concept": "Fibonacci Sequence",
                "cultural_tradition": "Native American",
                "musical_element": "Form"
            },
            {
                "math_concept": "Chaos Theory",
                "cultural_tradition": "Middle Eastern",
                "musical_element": "Timbre"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and create a musical structure based on the mathematical concept of {t['math_concept']}, incorporating elements from {t['cultural_tradition']} musical tradition, focusing on the musical element of {t['musical_element']}.

Your task:

1. Explain how the {t['math_concept']} can be applied to music composition, particularly in relation to {t['musical_element']} (2-3 sentences).

2. Describe a key characteristic of {t['cultural_tradition']} music, especially regarding {t['musical_element']} (2-3 sentences).

3. Create a short musical piece (or section) that combines the mathematical concept and the cultural tradition. Provide a textual representation of your musical structure using an appropriate notation system. Explain your notation if it's not standard Western notation (4-6 lines of music or equivalent).

4. Analyze your composition, explaining how it incorporates:
   a) The mathematical concept (2-3 sentences)
   b) The cultural tradition (2-3 sentences)
   c) The specified musical element (1-2 sentences)

5. Discuss one challenge you encountered in combining these elements and how you resolved it (2-3 sentences).

6. Propose an experiment to test how this mathematically and culturally informed approach to composition might influence listeners' perception or emotional response to the music (3-4 sentences).

Ensure your response demonstrates a deep understanding of the mathematical concept, the cultural tradition, and music theory. Be creative in your approach while maintaining mathematical and cultural accuracy.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the mathematical concept and its application to music.",
            f"The answer shows knowledge of {t['cultural_tradition']} musical tradition, particularly regarding {t['musical_element']}.",
            "The created musical piece effectively combines the mathematical concept and cultural tradition.",
            "The analysis of the composition is thorough and accurately reflects the incorporation of all required elements.",
            "The proposed experiment is creative and relevant to the composition approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
