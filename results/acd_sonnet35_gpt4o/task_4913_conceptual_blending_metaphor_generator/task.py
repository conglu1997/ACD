import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scientific_concepts = [
            {
                "concept": "quantum entanglement",
                "domain1": "social relationships",
                "domain2": "communication technology"
            },
            {
                "concept": "neural plasticity",
                "domain1": "urban planning",
                "domain2": "ecosystem adaptation"
            },
            {
                "concept": "dark matter",
                "domain1": "economics",
                "domain2": "art history"
            },
            {
                "concept": "epigenetics",
                "domain1": "software development",
                "domain2": "cultural anthropology"
            }
        ]
        return {
            "1": random.choice(scientific_concepts),
            "2": random.choice(scientific_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates novel metaphors using conceptual blending theory, then apply it to explain the complex scientific concept of {t['concept']}. Your metaphor should blend elements from the domains of {t['domain1']} and {t['domain2']}. Provide your response in the following format:

1. Conceptual Blending System Design (300-350 words):
   a) Describe the key components of your AI system for conceptual blending and metaphor generation.
   b) Explain how your system implements the principles of conceptual blending theory.
   c) Discuss how your system selects and combines elements from different conceptual domains.
   d) Address any novel approaches or algorithms used in your design.

2. Metaphor Generation Process (250-300 words):
   a) Outline the step-by-step process your system uses to generate metaphors.
   b) Explain how your system ensures the relevance and coherence of generated metaphors.
   c) Discuss how your approach balances creativity with comprehensibility.

3. Application to Scientific Concept (300-350 words):
   a) Use your AI system to generate a novel metaphor that explains {t['concept']}.
   b) Describe how your system blends elements from {t['domain1']} and {t['domain2']} to create this metaphor.
   c) Explain the scientific concept using your generated metaphor, highlighting how the metaphor captures key aspects of the concept.

4. Analysis and Evaluation (200-250 words):
   a) Analyze the strengths and limitations of your generated metaphor in explaining the scientific concept.
   b) Discuss how your system's approach compares to human-generated metaphors for scientific explanations.
   c) Propose a method for evaluating the effectiveness and creativity of your system's metaphors.

5. Ethical and Cognitive Implications (150-200 words):
   a) Discuss potential ethical considerations in using AI-generated metaphors for science communication.
   b) Explore how exposure to novel, AI-generated metaphors might influence human cognition and understanding.
   c) Propose guidelines for the responsible use of AI-generated metaphors in educational contexts.

Ensure your response demonstrates a deep understanding of conceptual blending theory, cognitive linguistics, and the chosen scientific concept. Be creative in your system design and metaphor generation while maintaining scientific accuracy. Use appropriate terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of conceptual blending theory and its application to metaphor generation.",
            f"The proposed AI system design is coherent and scientifically plausible.",
            f"The generated metaphor effectively explains the concept of {t['concept']} by blending elements from {t['domain1']} and {t['domain2']}.",
            "The response shows creativity in system design and metaphor generation while maintaining scientific accuracy.",
            "The analysis of the generated metaphor is insightful and considers both strengths and limitations.",
            "The ethical and cognitive implications are thoughtfully considered.",
            "The response is well-structured and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
