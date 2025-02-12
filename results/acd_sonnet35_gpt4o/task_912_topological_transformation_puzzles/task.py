import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        shapes = ['cube', 'torus', 'sphere', 'cylinder', 'mobius strip', 'klein bottle', 'projective plane', 'trefoil knot']
        transformations = ['stretching', 'twisting', 'folding', 'puncturing', 'gluing', 'embedding', 'inverting', 'knotting']
        return {
            "1": {
                "shape": random.choice(shapes),
                "transformation": random.choice(transformations),
                "comparison_transformation": random.choice([t for t in transformations if t != transformations[0]])
            },
            "2": {
                "shape": random.choice(shapes),
                "transformation": random.choice(transformations),
                "comparison_transformation": random.choice([t for t in transformations if t != transformations[0]])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Consider a {t['shape']} undergoing a topological transformation through {t['transformation']}. " \
               f"Analyze this transformation and provide the following:\n\n" \
               f"1. A step-by-step description of the {t['transformation']} process.\n" \
               f"2. An analysis of how this transformation affects the object's Euler characteristic, " \
               f"if applicable.\n" \
               f"3. A discussion of any holes, boundaries, or connected components created or destroyed " \
               f"by this transformation.\n" \
               f"4. A brief description of how you would visually represent this transformation, as if explaining " \
               f"it to someone who cannot see.\n" \
               f"5. An example of a real-world object or situation that could be analogous to this " \
               f"topological transformation.\n" \
               f"6. A potential application of this topological transformation in a scientific or engineering context.\n" \
               f"7. Identification and explanation of any limitations or edge cases in the transformation process.\n" \
               f"8. A comparison and contrast of the {t['transformation']} process with the {t['comparison_transformation']} process, " \
               f"highlighting key similarities and differences.\n\n" \
               f"Ensure your explanation is clear, accurate, and accessible to someone with basic " \
               f"knowledge of topology. Limit your response to 600 words or less."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation accurately describes the topological transformation process.",
            "The analysis of the Euler characteristic (if applicable) is correct.",
            "The discussion of holes, boundaries, and connected components is accurate and complete.",
            "The visual representation description is clear and helpful for someone who cannot see.",
            "The real-world analogy is appropriate and clearly explained.",
            "The scientific or engineering application is plausible and well-explained.",
            "Limitations or edge cases of the transformation are correctly identified and explained.",
            "The comparison with the other transformation process is insightful and accurate.",
            "The explanation is clear, concise (600 words or less), and accessible to someone with basic knowledge of topology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
