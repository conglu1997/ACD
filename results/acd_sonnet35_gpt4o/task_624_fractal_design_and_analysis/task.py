import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        fractal_types = [
            {
                "base_shape": "triangle",
                "transformation": "rotation and scaling",
                "example_property": "Hausdorff dimension between 1 and 2"
            },
            {
                "base_shape": "square",
                "transformation": "iteration and subdivision",
                "example_property": "Self-similarity at multiple scales"
            }
        ]
        return {
            "1": random.choice(fractal_types),
            "2": random.choice(fractal_types)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel fractal based on a {t['base_shape']} using {t['transformation']}. Your fractal should exhibit the following property: {t['example_property']}. Respond in the following format:\n\n" + \
               "1. Fractal Design (250-300 words):\n" + \
               "   a) Describe your fractal's basic structure and how it's generated.\n" + \
               "   b) Explain how you've incorporated the given base shape and transformation.\n" + \
               "   c) Discuss any unique features or properties of your fractal.\n" + \
               "   d) Provide a detailed visual description of your fractal.\n\n" + \
               "2. Mathematical Analysis (300-350 words):\n" + \
               "   a) Explain the mathematical principles underlying your fractal.\n" + \
               "   b) Calculate and discuss its dimension (Hausdorff dimension).\n" + \
               "   c) Analyze any symmetries or self-similarities in your fractal.\n" + \
               "   d) Provide at least two relevant mathematical formulas or equations.\n" + \
               "   e) Explain how your fractal exhibits the given example property.\n\n" + \
               "3. Generation Algorithm (250-300 words):\n" + \
               "   a) Describe a simple algorithm to generate your fractal.\n" + \
               "   b) Provide pseudocode or high-level programming language code for the key steps.\n" + \
               "   c) Discuss any limitations or potential optimizations of your algorithm.\n" + \
               "   d) Explain how the algorithm ensures the fractal exhibits the given property.\n\n" + \
               "4. Applications and Implications (200-250 words):\n" + \
               "   a) Propose a real-world application for your fractal design.\n" + \
               "   b) Discuss how your fractal might be used in art, science, or technology.\n" + \
               "   c) Explain any insights your fractal provides about natural or mathematical patterns.\n" + \
               "   d) Discuss potential future research directions based on your fractal design.\n\n" + \
               "Ensure your response demonstrates a deep understanding of fractal geometry, mathematical principles, and basic algorithmic thinking. Be creative in your fractal design while maintaining mathematical accuracy and plausibility. Your total response should be between 1000-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The fractal design is novel, creative, and incorporates the given base shape and transformation",
            "The mathematical analysis is accurate, detailed, and demonstrates a deep understanding of fractal geometry",
            "The generation algorithm is clearly explained, logically sound, and includes pseudocode or high-level programming language code",
            "The proposed application is innovative and plausible",
            "The response includes a detailed visual description of the fractal",
            "The fractal design exhibits the given example property, and this is adequately explained",
            "The overall response shows interdisciplinary knowledge application and creative problem-solving",
            "The response meets the specified word count requirements for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
