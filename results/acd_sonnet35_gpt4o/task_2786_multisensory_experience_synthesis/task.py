import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'tactile', 'proprioceptive']
        abstract_concepts = ['time', 'causality', 'balance', 'transformation']
        applications = ['virtual reality therapy', 'robotic skill acquisition', 'augmented sensory experiences', 'cognitive enhancement']
        
        tasks = [
            {
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice([m for m in sensory_modalities if m != primary_modality]),
                "abstract_concept": random.choice(abstract_concepts),
                "application": random.choice(applications)
            } for primary_modality in sensory_modalities
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks[:2])}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a multisensory experience that primarily utilizes the {t['primary_modality']} modality, integrates it with the {t['secondary_modality']} modality, and explores the abstract concept of {t['abstract_concept']}. Then, analyze its potential application in {t['application']}. Your response should include the following sections:

1. Experience Design (300-350 words):
   a) Describe the core components of your multisensory experience.
   b) Explain how the {t['primary_modality']} and {t['secondary_modality']} modalities are integrated.
   c) Detail how the experience explores the concept of {t['abstract_concept']}.
   d) Discuss any novel features or technologies incorporated into your design.

2. Sensory Integration Mechanisms (250-300 words):
   a) Explain the theoretical basis for integrating {t['primary_modality']} and {t['secondary_modality']} inputs.
   b) Describe potential neural mechanisms involved in processing this multisensory experience.
   c) Discuss how the integration of these modalities might enhance the perception of {t['abstract_concept']}.

3. Embodied AI Implementation (200-250 words):
   a) Propose how an embodied AI system could be designed to process and learn from this multisensory experience.
   b) Explain potential challenges in implementing this experience for AI and how they might be overcome.
   c) Discuss how this implementation might differ from human sensory processing.

4. Application Analysis (200-250 words):
   a) Analyze how your multisensory experience could be applied in {t['application']}.
   b) Describe potential benefits and limitations of using this experience in this context.
   c) Propose a specific use case and explain how it would work in practice.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to creating and using this multisensory experience.
   b) Discuss how these ethical concerns might be addressed.
   c) Consider broader societal implications of advanced multisensory technologies.

6. Future Directions (150-200 words):
   a) Propose potential advancements or iterations of your multisensory experience.
   b) Suggest areas for further research in multisensory integration for embodied AI.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of sensory perception, embodied cognition, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates {t['primary_modality']} and {t['secondary_modality']} modalities in the experience design.",
            f"The explanation of how the experience explores the concept of {t['abstract_concept']} is clear and innovative.",
            f"The analysis of the application in {t['application']} is thorough and plausible.",
            "The response demonstrates a deep understanding of sensory perception, embodied cognition, and artificial intelligence.",
            "The ethical considerations and future directions are thoughtfully discussed.",
            "The overall response is creative, scientifically grounded, well-structured, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
