import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        shapes = [
            "5-dimensional hypercube (penteract)",
            "4-dimensional Klein bottle"
        ]
        applications = [
            "quantum computing circuit design",
            "multidimensional data visualization"
        ]
        return {
            str(i+1): {
                'shape': shape,
                'application': application
            } for i, (shape, application) in enumerate(zip(shapes, applications))
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an origami-inspired folding pattern for a {t['shape']}, and analyze its properties and potential applications in {t['application']}. Your response should include:

1. Geometric Description (200-250 words):
   a) Describe the key geometric properties of the {t['shape']}.
   b) Explain how these properties might be represented in a lower-dimensional 'unfolded' state.
   c) Discuss any unique challenges in conceptualizing this shape compared to 3D objects.

2. Folding Pattern Design (250-300 words):
   a) Propose an origami-inspired folding pattern that could theoretically create the {t['shape']}.
   b) Describe the key folds and transformations required, using appropriate geometric terminology.
   c) Explain how your design maintains the essential properties of the shape during the folding process.
   d) Include a textual representation or description of a diagram that illustrates your folding pattern.

3. Mathematical Analysis (200-250 words):
   a) Discuss the topological properties of your folded structure.
   b) Analyze how the folding process affects the symmetries of the original shape.
   c) Propose a mathematical formula or algorithm that describes a key aspect of your folding pattern.

4. Application in {t['application']} (200-250 words):
   a) Explain how your hyperdimensional origami design could be applied to {t['application']}.
   b) Describe specific benefits or novel capabilities that this approach might offer.
   c) Discuss any potential challenges in implementing this design in the chosen application.

5. Interdisciplinary Connections (150-200 words):
   a) Explore how your hyperdimensional origami design might inform or be informed by concepts in another scientific field (e.g., physics, biology, computer science).
   b) Propose a specific research question that bridges your design with this other field.

Ensure your response demonstrates a deep understanding of geometry, topology, and the principles of origami. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative in your approach while maintaining mathematical and scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the geometric properties of the given hyperdimensional shape",
            "The proposed folding pattern is creative, well-described, and theoretically plausible for the given shape",
            "The mathematical analysis shows a deep understanding of topology and symmetry in higher dimensions",
            "The application of the design to the given field is innovative and well-reasoned",
            "The interdisciplinary connections and research question are insightful and demonstrate broad scientific understanding"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
