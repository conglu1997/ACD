import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = ['time', 'freedom', 'balance', 'complexity', 'harmony']
        modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        
        tasks = {}
        for i in range(1, 3):
            concept = random.choice(concepts)
            source_modality = random.choice(modalities)
            target_modality = random.choice([m for m in modalities if m != source_modality])
            tasks[str(i)] = {
                'concept': concept,
                'source_modality': source_modality,
                'target_modality': target_modality
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for translating the abstract concept of '{t['concept']}' from the {t['source_modality']} modality to the {t['target_modality']} modality. Cross-modal translation involves representing information from one sensory domain in another while preserving its essential meaning. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your cross-modal translation system.
   b) Explain how your system processes and represents the concept in the source modality.
   c) Detail the mechanism for mapping the concept to the target modality.
   d) Discuss how your system handles the challenges of preserving meaning across modalities.

2. Cognitive Model (200-250 words):
   a) Explain how your system models the cognitive processes involved in cross-modal abstraction.
   b) Describe how it accounts for the subjective and cultural aspects of sensory experiences.
   c) Discuss any novel computational or AI techniques your system employs to mimic human-like cross-modal thinking.

3. Concept Translation (250-300 words):
   a) Provide a detailed description of how your system would represent '{t['concept']}' in the {t['source_modality']} modality.
   b) Explain the step-by-step process of translating this representation to the {t['target_modality']} modality.
   c) Describe the final representation of '{t['concept']}' in the {t['target_modality']} modality.
   d) Discuss how the essential qualities of the concept are preserved or transformed in this translation.

4. Evaluation and Applications (200-250 words):
   a) Propose metrics or methods to evaluate the effectiveness of your cross-modal translation.
   b) Discuss potential applications of your system in fields such as AI, psychology, art, or assistive technologies.
   c) Explore how this system might enhance our understanding of human cognition and perception.

5. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or challenges in your cross-modal translation system.
   b) Discuss any ethical considerations related to developing and using such technology.
   c) Propose guidelines for the responsible development and use of cross-modal AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, perception, and AI. Be creative in your system design and concept translation while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1300 words, not including the headings."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive description of a system for translating the concept of '{t['concept']}' from {t['source_modality']} to {t['target_modality']} modality.",
            "The system architecture is well-explained and addresses the challenges of cross-modal translation.",
            "The cognitive model demonstrates a deep understanding of cross-modal abstraction processes.",
            "The concept translation process is detailed and creative, while maintaining scientific plausibility.",
            "The response includes thoughtful evaluation methods and potential applications of the system.",
            "Limitations and ethical considerations are adequately addressed.",
            "The overall response demonstrates interdisciplinary knowledge, creativity, and analytical reasoning.",
            "The response follows the specified format with clear headings and appropriate length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
