import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        topological_concepts = [
            {
                "concept": "Homeomorphism",
                "definition": "A continuous function between topological spaces that has a continuous inverse function",
                "example": "A coffee mug and a donut are topologically equivalent",
                "application": "Computer graphics and 3D modeling"
            },
            {
                "concept": "Homotopy",
                "definition": "A continuous deformation of one function into another",
                "example": "Transforming a circle into a square without breaking the curve",
                "application": "Path planning in robotics"
            },
            {
                "concept": "Manifold",
                "definition": "A topological space that locally resembles Euclidean space",
                "example": "The surface of a sphere is a 2-dimensional manifold",
                "application": "General relativity in physics"
            },
            {
                "concept": "Knot theory",
                "definition": "The study of mathematical knots and their properties",
                "example": "The trefoil knot is the simplest non-trivial knot",
                "application": "Analyzing DNA structure in biology"
            }
        ]
        return {
            "1": random.choice(topological_concepts),
            "2": random.choice(topological_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and apply the topological concept of {t['concept']} to solve a real-world problem. Your task has four parts:

1. Concept Explanation (200-250 words):
   a) Define the topological concept of {t['concept']} in your own words.
   b) Explain the given example: {t['example']}
   c) Describe how this concept relates to other areas of topology or mathematics.
   d) Provide a specific example of how this concept has been applied in the real world, outside of the given application domain.

2. Visual Representation (describe in 150-200 words):
   Create a visual representation or diagram that illustrates the concept of {t['concept']}. Describe this visual representation in detail, explaining how it captures the key aspects of the concept.

3. Problem Solving (300-350 words):
   Consider the application domain: {t['application']}
   a) Identify a specific problem or challenge in this domain that could be addressed using the concept of {t['concept']}.
   b) Propose a solution that leverages this topological concept.
   c) Explain how your solution works and why it's effective.
   d) Discuss any limitations or potential issues with your proposed solution.
   e) Suggest how your solution could be extended or improved in the future.

4. Future Developments (100-150 words):
   Discuss potential future developments or extensions of the {t['concept']} concept in mathematics or its applications. Consider emerging technologies or interdisciplinary connections that could lead to new insights or uses for this topological concept.

Ensure your response demonstrates a deep understanding of the topological concept, creative problem-solving, and the ability to apply abstract mathematical ideas to practical scenarios."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation of {t['concept']} is accurate, comprehensive, and demonstrates a deep understanding of the topological concept.",
            "The visual representation description clearly illustrates the key aspects of the concept and is well-explained.",
            f"The proposed solution in the domain of {t['application']} effectively applies the concept of {t['concept']} and addresses a relevant problem.",
            "The response shows creativity and originality in applying topological concepts to real-world problems.",
            "The limitations and potential issues of the proposed solution are thoughtfully discussed.",
            "The example of real-world application outside the given domain is relevant and well-explained.",
            "The discussion of future developments demonstrates insight into potential extensions of the concept."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
