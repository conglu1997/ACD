import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        abstract_domains = ['emotions', 'time', 'mathematics', 'ethics', 'philosophy']
        concepts = ['freedom', 'balance', 'complexity', 'harmony', 'chaos']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'modality': random.choice(modalities),
                'abstract_domain': random.choice(abstract_domains),
                'concept': random.choice(concepts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates a novel concept by blending ideas from the sensory modality of {t['modality']}, the abstract domain of {t['abstract_domain']}, and the concept of {t['concept']}. Your response should include:

1. Conceptual Blending Framework (250-300 words):
   a) Describe the architecture of your conceptual blending system.
   b) Explain how it integrates information from different modalities and abstract domains.
   c) Detail the process of generating novel concepts through blending.

2. Novel Concept Generation (200-250 words):
   a) Generate a novel concept using your system, blending {t['modality']}, {t['abstract_domain']}, and {t['concept']}.
   b) Provide a clear and detailed description of the resulting concept.
   c) Explain how each component (modality, domain, and concept) contributes to the blended concept.

3. Linguistic Expression (200-250 words):
   a) Create a new term or phrase that captures the essence of your blended concept.
   b) Provide a definition for this term, as it might appear in a dictionary of the future.
   c) Use the term in three sentences that demonstrate its meaning and usage.

4. Conceptual Analysis (250-300 words):
   a) Analyze the emergent properties of your blended concept.
   b) Discuss how this concept differs from its constituent parts.
   c) Explore potential applications or implications of this new concept in science, art, or philosophy.

5. Cross-Modal Evaluation (200-250 words):
   a) Propose a method to evaluate the coherence and creativity of your blended concept.
   b) Discuss how your concept might be perceived differently across various sensory modalities.
   c) Consider potential challenges in communicating this concept to individuals with different sensory capabilities.

Ensure your response demonstrates a deep understanding of conceptual blending, cross-modal integration, and linguistic creativity. Be innovative in your approach while maintaining logical consistency. Use appropriate terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual blending and cross-modal integration.",
            "The generated concept successfully blends ideas from the specified modality, abstract domain, and concept.",
            "The linguistic expression of the new concept is creative, clear, and consistently used.",
            "The conceptual analysis shows insight into the emergent properties and potential applications of the blended concept.",
            "The cross-modal evaluation proposal is thoughtful and considers different sensory perspectives.",
            "The overall response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
