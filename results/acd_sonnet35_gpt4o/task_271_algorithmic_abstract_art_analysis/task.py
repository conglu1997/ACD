import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        algorithms = [
            'Cellular Automaton',
            'L-System',
            'Fractal',
            'Voronoi Diagram',
            'Perlin Noise'
        ]
        art_movements = [
            'Cubism',
            'Suprematism',
            'De Stijl',
            'Abstract Expressionism',
            'Op Art'
        ]
        tasks = {
            "1": {
                "algorithm": random.choice(algorithms),
                "art_movement": random.choice(art_movements)
            },
            "2": {
                "algorithm": random.choice(algorithms),
                "art_movement": random.choice(art_movements)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze an abstract art piece based on the {t['algorithm']} algorithm, inspired by the {t['art_movement']} art movement. Your task has four parts:

1. Algorithm Description (100-150 words):
   a) Explain the basic principles of the {t['algorithm']} algorithm.
   b) Describe how this algorithm can be used to generate visual patterns or structures.

2. Art Movement Context (100-150 words):
   a) Briefly describe the key characteristics of the {t['art_movement']} movement.
   b) Explain how these characteristics can be interpreted or expressed through algorithmic art.

3. Artwork Conception (200-250 words):
   a) Design an abstract artwork that combines the {t['algorithm']} algorithm with the principles of {t['art_movement']}.
   b) Describe the visual elements of your artwork (e.g., shapes, colors, composition) and how they relate to both the algorithm and the art movement.
   c) Explain the process you would use to generate this artwork, including any modifications or interpretations of the algorithm.

4. Analysis and Interpretation (150-200 words):
   a) Analyze how your artwork reflects both the mathematical properties of the algorithm and the aesthetic principles of the art movement.
   b) Discuss any emergent properties or unexpected visual effects that arise from this combination.
   c) Reflect on how this approach to creating art might influence our understanding of creativity, randomness, and structure in visual arts.

Ensure your response demonstrates a deep understanding of both the specified algorithm and art movement, as well as creative thinking in combining these elements. Be specific in your descriptions and analysis, using relevant terminology from both computer science and art theory."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections: Algorithm Description, Art Movement Context, Artwork Conception, and Analysis and Interpretation.",
            f"The explanation of the {t['algorithm']} algorithm is accurate and clear.",
            f"The description of the {t['art_movement']} movement is accurate and relevant.",
            "The artwork conception successfully integrates the algorithm and art movement principles.",
            "The analysis demonstrates understanding of both mathematical and aesthetic aspects of the artwork.",
            "The overall response shows creativity, interdisciplinary knowledge integration, and analytical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
