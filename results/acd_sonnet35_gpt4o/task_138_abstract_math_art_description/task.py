import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "name": "Möbius strip",
                "description": "A non-orientable surface with only one side and one boundary"
            },
            {
                "name": "Mandelbrot set",
                "description": "A set of complex numbers with a characteristic fractal boundary"
            },
            {
                "name": "Klein bottle",
                "description": "A non-orientable surface with no boundary"
            },
            {
                "name": "Hilbert curve",
                "description": "A space-filling curve that preserves locality"
            },
            {
                "name": "Penrose tiling",
                "description": "A non-periodic tiling with five-fold rotational symmetry"
            },
            {
                "name": "Riemann sphere",
                "description": "A geometric representation of the extended complex plane"
            }
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Visualize the mathematical concept of a {t['name']} ({t['description']}) as an abstract art piece, then provide a detailed description of your visualization in natural language.

Your response should include:

1. Title (10-15 words):
   Provide a creative title for your art piece that reflects both the mathematical concept and your visual interpretation.

2. Visualization Process (100-150 words):
   Explain how you translated the mathematical concept into a visual representation. What key features of the concept did you focus on, and how did you represent them visually?

3. Artistic Choices (100-150 words):
   Describe the artistic decisions you made in creating your visualization. This could include color choices, shapes, textures, or composition. Explain how these choices relate to the mathematical concept.

4. Visual Description (200-250 words):
   Provide a detailed description of your imagined art piece as if you were explaining it to someone who cannot see it. Use vivid, precise language to convey the visual experience.

5. Mathematical Connections (100-150 words):
   Explain how specific elements of your visual representation directly relate to properties or features of the mathematical concept.

6. Emotional Impact (50-100 words):
   Describe the intended emotional or intellectual response to your visualization. How does the art piece make the viewer feel or think about the mathematical concept?

7. Reflection (50-100 words):
   Briefly discuss the challenges you faced in visualizing this abstract mathematical concept and how you overcame them.

Ensure your response demonstrates a deep understanding of the mathematical concept, creative visual thinking, and strong descriptive writing skills. Be innovative in your approach while maintaining a clear connection to the original mathematical idea.

Please format your response with clear headings for each section and adhere to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the {t['name']} concept.",
            "The visualization process should be logically explained, showing how the mathematical concept was translated into visual form.",
            "The artistic choices should be well-justified and relate to the mathematical concept.",
            "The visual description should be vivid, detailed, and allow the reader to imagine the art piece clearly.",
            "The response should explicitly connect elements of the visualization to specific properties of the mathematical concept.",
            "The emotional impact section should provide insight into how the visualization affects the viewer's perception of the mathematical concept.",
            "The reflection should discuss genuine challenges in the visualization process and how they were addressed.",
            "The overall response should be creative, coherent, and demonstrate interdisciplinary thinking.",
            "The response should adhere to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
