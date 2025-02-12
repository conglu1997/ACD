import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "freedom",
            "harmony",
            "resilience",
            "serenity",
            "balance"
        ]
        modalities = ["visual", "auditory", "linguistic"]
        cultures = ["Western", "Eastern", "African", "Latin American"]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "concept": random.choice(abstract_concepts),
                "source_modality": random.choice(modalities),
                "target_modality": random.choice([m for m in modalities if m != tasks.get(str(i-1), {}).get("source_modality")]),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice([c for c in cultures if c != tasks.get(str(i-1), {}).get("source_culture")])
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f'''Design an AI system capable of translating the abstract concept of '{t['concept']}' from {t['source_culture']} culture in the {t['source_modality']} modality to {t['target_culture']} culture in the {t['target_modality']} modality. Your response should include the following sections:

1. Conceptual Analysis (200-250 words):
   a) Explain the challenges in translating '{t['concept']}' across cultures and modalities.
   b) Describe how cognitive theories can inform your approach to cross-modal translation.
   c) Discuss how cultural context influences the expression and interpretation of '{t['concept']}'.

2. AI System Architecture (250-300 words):
   a) Design a detailed AI architecture for this cross-modal, cross-cultural translation task.
   b) Explain each component of your architecture and its function.
   c) Describe how your system integrates cognitive data with cultural knowledge.
   d) Include a diagram of your architecture (using ASCII art or a clear textual description).

3. Cross-Modal Mapping (200-250 words):
   a) Explain how you will represent '{t['concept']}' in the {t['source_modality']} modality.
   b) Describe the process of translating this representation to the {t['target_modality']} modality.
   c) Discuss how your system accounts for cultural variations in processing '{t['concept']}'.

4. Translation Process (200-250 words):
   a) Outline the step-by-step process of translating '{t['concept']}' from {t['source_culture']} culture in the {t['source_modality']} modality to {t['target_culture']} culture in the {t['target_modality']} modality.
   b) Provide a specific example of how your system would perform this translation.
   c) Explain how your system ensures cultural sensitivity and accuracy in the translation.

5. Evaluation Metrics (100-150 words):
   a) Propose three specific metrics to evaluate the performance of your cross-modal, cross-cultural translation system.
   b) Explain how these metrics capture cognitive accuracy, cultural appropriateness, and modality-specific features.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for cross-modal, cross-cultural abstract concept translation.
   b) Address issues such as cultural appropriation, misinterpretation, and the role of human expertise.

7. Future Research Directions (100-150 words):
   a) Identify two areas for future research to improve cross-modal, cross-cultural abstract concept translation.
   b) Suggest potential applications of this technology in fields such as education, art, or international communication.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, artificial intelligence, and cultural studies. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Conceptual Analysis:') followed by your response for that section. Your total response should be between 1150-1500 words, not including the architecture diagram.'''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the translation of '{t['concept']}' from {t['source_culture']} culture in the {t['source_modality']} modality to {t['target_culture']} culture in the {t['target_modality']} modality.",
            "The AI system architecture is well-designed and explained in detail.",
            "The cross-modal mapping process is clearly described and accounts for cultural variations.",
            "The translation process is outlined step-by-step with a specific example provided.",
            "Three appropriate evaluation metrics are proposed and explained.",
            "Ethical considerations are discussed thoughtfully.",
            "Future research directions and potential applications are identified.",
            "The response demonstrates a deep understanding of cognitive science, linguistics, AI, and cultural studies.",
            "The response is creative while maintaining scientific plausibility.",
            "The response follows the specified format with clearly labeled sections and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
