import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            "Fractal geometry",
            "Topology",
            "Group theory",
            "Complex analysis",
            "Differential geometry",
            "Number theory",
            "Chaos theory",
            "Knot theory"
        ]
        art_forms = [
            "Visual art",
            "Music composition"
        ]
        return {
            "1": {"math_concept": random.choice(math_concepts), "art_form": random.choice(art_forms)},
            "2": {"math_concept": random.choice(math_concepts), "art_form": random.choice(art_forms)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing mathematical art and music compositions based on complex mathematical concepts, then use it to create and interpret a specific piece. Focus on the mathematical concept of {t['math_concept']} and the art form of {t['art_form']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for mathematical art/music generation and analysis.
   b) Explain how your system incorporates the specified mathematical concept into its creative process.
   c) Discuss any novel algorithms or techniques used in your system.
   d) Include a simple diagram or flowchart illustrating the system's architecture.

2. Mathematical-Artistic Integration (200-250 words):
   a) Explain how your system translates the chosen mathematical concept into artistic elements.
   b) Describe the mapping between mathematical properties and artistic features.
   c) Discuss any challenges in this integration and how your system addresses them.

3. Composition Generation (250-300 words):
   a) Provide a detailed description of a composition your system might generate.
   b) Explain the mathematical principles underlying the composition.
   c) Describe how the composition manifests the chosen mathematical concept in the specified art form.
   d) If the art form is music, include a short musical notation or description of the sound. If it's visual art, describe the visual elements in detail.

4. Analytical Capabilities (200-250 words):
   a) Explain how your system would analyze and interpret the generated composition.
   b) Describe the metrics or methods used to evaluate the mathematical complexity and artistic merit of the piece.
   c) Discuss how your system might identify and explain patterns or structures in the composition.

5. Cognitive and Perceptual Implications (150-200 words):
   a) Discuss how exposure to such mathematically-derived art or music might influence human cognition or perception.
   b) Explore potential applications in fields such as education, therapy, or cognitive enhancement.

6. Ethical and Philosophical Considerations (150-200 words):
   a) Discuss the implications of using AI to create mathematically-based art and music.
   b) Explore questions of creativity, authorship, and the nature of mathematical beauty.
   c) Address potential concerns about the impact on human artists and composers.

Ensure your response demonstrates a deep understanding of the specified mathematical concept, the chosen art form, and AI system design. Be creative and innovative in your approach while maintaining scientific and artistic plausibility. Use appropriate terminology from mathematics, art theory, and computer science, providing clear explanations for complex concepts.

Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified mathematical concept and its potential applications in art or music.",
            "The AI system design is innovative, well-explained, and plausibly capable of generating and analyzing mathematical art or music.",
            "The composition generation example clearly illustrates the integration of the mathematical concept with the chosen art form.",
            "The analytical capabilities of the system are well-defined and demonstrate a sophisticated approach to interpreting mathematical art or music.",
            "The discussion of cognitive, ethical, and philosophical implications is thoughtful and considers multiple perspectives.",
            "The overall response is well-structured, coherent, and demonstrates a high level of interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
