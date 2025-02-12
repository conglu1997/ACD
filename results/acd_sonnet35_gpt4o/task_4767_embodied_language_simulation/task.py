import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'sensory_modality': 'tactile',
                'conceptual_domain': 'texture',
                'linguistic_feature': 'adjectives',
                'physical_interaction': 'touching various surfaces'
            },
            {
                'sensory_modality': 'proprioceptive',
                'conceptual_domain': 'spatial relations',
                'linguistic_feature': 'prepositions',
                'physical_interaction': 'moving objects in space'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the acquisition and use of language based on embodied experiences, focusing on how sensorimotor interactions shape conceptual understanding and linguistic expression. Your system should specifically address the {t['sensory_modality']} sensory modality, the conceptual domain of {t['conceptual_domain']}, and the linguistic feature of {t['linguistic_feature']} through the physical interaction of {t['physical_interaction']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system models the relationship between physical experiences and language acquisition.
   c) Detail how the system incorporates the specified sensory modality, conceptual domain, and linguistic feature.

2. Embodied Learning Process (250-300 words):
   a) Outline the steps your system takes to learn language from embodied experiences.
   b) Explain how the system processes and integrates sensorimotor information.
   c) Describe how conceptual understanding emerges from physical interactions.

3. Language Generation and Comprehension (250-300 words):
   a) Explain how your system generates language based on embodied experiences.
   b) Describe how it comprehends language related to the specified conceptual domain.
   c) Provide examples of how the system would express concepts learned through physical interaction.

4. Evaluation and Testing (200-250 words):
   a) Propose methods to evaluate your system's language acquisition and use.
   b) Describe experiments that could test the system's embodied understanding.
   c) Discuss how you would compare your system's performance to human language acquisition.

5. Cognitive Science Implications (200-250 words):
   a) Analyze how your system's approach relates to theories of embodied cognition.
   b) Discuss potential insights your model could provide for understanding human language acquisition.
   c) Address any limitations in using AI to model embodied language learning.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical issues related to simulating embodied language acquisition.
   b) Discuss the implications of your system for AI development and cognitive science research.
   c) Propose two future research directions that could build upon your system.

Ensure your response demonstrates a deep understanding of embodied cognition, linguistics, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the {t['sensory_modality']} sensory modality, the conceptual domain of {t['conceptual_domain']}, and the linguistic feature of {t['linguistic_feature']} through the physical interaction of {t['physical_interaction']}.",
            "The system design demonstrates a deep understanding of embodied cognition and its relationship to language acquisition.",
            "The response includes innovative yet scientifically plausible approaches to simulating embodied language learning.",
            "All required sections are present and adequately addressed.",
            "The response shows interdisciplinary integration of cognitive science, linguistics, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
