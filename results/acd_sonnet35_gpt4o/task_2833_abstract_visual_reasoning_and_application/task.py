import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        patterns = [
            {
                "name": "Fractal Spirals",
                "description": "Repeating spiral patterns that maintain self-similarity at different scales",
                "challenge": "Urban planning for a sustainable eco-city"
            },
            {
                "name": "Voronoi Tessellation",
                "description": "A partition of a plane into regions based on distance to points in a specific subset of the plane",
                "challenge": "Optimizing wireless network coverage in a mountainous region"
            },
            {
                "name": "Phyllotaxis",
                "description": "The arrangement of leaves on a plant stem, often following the Fibonacci sequence",
                "challenge": "Designing an energy-efficient solar panel array for a curved building surface"
            }
        ]
        return {
            "1": random.choice(patterns),
            "2": random.choice(patterns)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the abstract visual pattern '{t['name']}' and apply it to solve the real-world design challenge: {t['challenge']}. Your response should include:

1. Pattern Analysis (200-250 words):
   a) Describe the key characteristics and principles of the {t['name']} pattern.
   b) Explain how this pattern occurs or is used in nature or existing human designs.
   c) Discuss the mathematical or geometric principles underlying this pattern.

2. Application to Design Challenge (300-350 words):
   a) Propose an innovative solution to the challenge using the {t['name']} pattern as inspiration.
   b) Explain how your solution incorporates the key principles of the pattern.
   c) Describe the main components and functionality of your design.
   d) Discuss how your solution addresses specific aspects of the challenge.

3. Visual Representation (150-200 words):
   a) Provide a detailed textual description of how your solution would look if implemented.
   b) Use ASCII art or other text-based visual representation to illustrate key aspects of your design.
   c) Explain how your visual representation captures the essence of the {t['name']} pattern.

4. Advantages and Limitations (200-250 words):
   a) Discuss the potential benefits of using this pattern-inspired approach for the given challenge.
   b) Analyze any limitations or potential issues with your design.
   c) Compare your approach to a more conventional solution to the same challenge.

5. Interdisciplinary Connections (150-200 words):
   a) Identify at least two other fields or disciplines where this pattern or your solution could be applied.
   b) Explain how insights from these fields could further enhance your design.
   c) Propose a potential research question that bridges your design concept with another scientific domain.

Ensure your response demonstrates a deep understanding of the abstract visual pattern and its application to real-world problems. Be creative in your approach while maintaining practicality and scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes and analyzes the {t['name']} pattern.",
            f"The proposed solution creatively applies the {t['name']} pattern to address the {t['challenge']}.",
            "The visual representation effectively communicates the design concept using text-based methods.",
            "The response demonstrates interdisciplinary thinking and identifies relevant connections to other fields.",
            "The writing is clear, well-structured, and adheres to the specified word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
