import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_movements = [
            "Surrealism",
            "Cubism",
            "Abstract Expressionism",
            "Pop Art",
            "Minimalism",
            "Digital Art"
        ]
        cognitive_principles = [
            "Conceptual Blending",
            "Divergent Thinking",
            "Analogical Reasoning",
            "Embodied Cognition",
            "Perceptual Restructuring",
            "Cognitive Fluidity"
        ]
        return {
            "1": {
                "art_movement": random.choice(art_movements),
                "cognitive_principle": random.choice(cognitive_principles)
            },
            "2": {
                "art_movement": random.choice(art_movements),
                "cognitive_principle": random.choice(cognitive_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates novel artistic concepts within the {t['art_movement']} movement, incorporating the cognitive principle of {t['cognitive_principle']}. Then, evaluate the creativity and potential impact of the generated concepts. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and evaluating artistic concepts.
   b) Explain how your system incorporates principles from {t['art_movement']} and {t['cognitive_principle']}.
   c) Detail the machine learning techniques used in your system (e.g., neural networks, evolutionary algorithms).
   d) Provide a high-level diagram of your system architecture (described in words).

2. Artistic Concept Generation (250-300 words):
   a) Explain the process by which your system generates novel artistic concepts.
   b) Describe how {t['cognitive_principle']} is implemented in the generation process.
   c) Provide an example of a generated artistic concept, including its visual description and conceptual explanation.
   d) Discuss how your system ensures the generated concepts align with {t['art_movement']} principles.

3. Creativity Evaluation (250-300 words):
   a) Define the criteria your system uses to evaluate the creativity of generated concepts.
   b) Explain how these criteria relate to cognitive theories of creativity and art appreciation.
   c) Describe the algorithm or process used to assign creativity scores to generated concepts.
   d) Provide an example of how your system would evaluate the creativity of the concept from section 2.

4. Impact Assessment (200-250 words):
   a) Explain how your system predicts the potential impact of generated artistic concepts.
   b) Discuss the factors considered in this assessment (e.g., novelty, cultural relevance, emotional resonance).
   c) Describe how your system might use external data sources or knowledge bases in this process.
   d) Provide an example impact assessment for the concept from section 2.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in using AI for artistic creation and evaluation.
   b) Discuss how your system addresses concerns about AI replacing human artists or critics.
   c) Propose guidelines for the responsible development and use of computational creativity systems in art.

6. Comparative Analysis (200-250 words):
   a) Compare your proposed system to existing approaches in computational creativity for art.
   b) Discuss the potential advantages and limitations of your system.
   c) Explain how your system addresses challenges that current approaches struggle with.

7. Future Directions (150-200 words):
   a) Propose potential extensions or improvements to your system.
   b) Suggest a novel research question that could be investigated using your system.
   c) Discuss how your approach might be adapted to other creative domains (e.g., music, literature).

Ensure your response demonstrates a deep understanding of art theory, cognitive science, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively incorporates principles from {t['art_movement']} and {t['cognitive_principle']}",
            "The artistic concept generation process is clearly explained and aligns with the specified art movement",
            "The creativity evaluation criteria are well-defined and grounded in cognitive theories",
            "The impact assessment process is logical and considers relevant factors",
            "Ethical considerations are thoughtfully addressed",
            "The comparative analysis demonstrates a deep understanding of computational creativity in art",
            "The proposed future directions are innovative and well-reasoned",
            "The response demonstrates interdisciplinary knowledge integration and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
