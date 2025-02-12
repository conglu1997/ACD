import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "Free will",
            "Consciousness",
            "Justice",
            "Time",
            "Beauty"
        ]
        cultures = [
            "Western",
            "East Asian",
            "African",
            "Middle Eastern",
            "Indigenous American"
        ]
        sensory_modalities = [
            "Visual",
            "Auditory",
            "Tactile",
            "Olfactory",
            "Gustatory"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "concept": random.choice(abstract_concepts),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "sensory_modality1": random.choice(sensory_modalities),
                "sensory_modality2": random.choice(sensory_modalities)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates abstract concepts across different sensory modalities and cultural contexts. Then, use your system to represent the concept of {t['concept']} in both {t['culture1']} and {t['culture2']} cultures, expressing it through {t['sensory_modality1']} and {t['sensory_modality2']} modalities. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cross-modal and cross-cultural concept translation.
   b) Explain how your system integrates knowledge from various domains (e.g., philosophy, anthropology, cognitive science).
   c) Detail the mechanisms used to map abstract concepts to sensory representations.
   d) Discuss how your system accounts for cultural variations in concept interpretation.
   e) Include a high-level diagram of your system architecture (described textually).

2. Concept Analysis (250-300 words):
   a) Analyze the concept of {t['concept']} from both {t['culture1']} and {t['culture2']} perspectives.
   b) Identify key similarities and differences in how these cultures interpret the concept.
   c) Discuss any challenges in reconciling these cultural interpretations.

3. Sensory Representation (300-350 words):
   a) Describe how your system would represent {t['concept']} using the {t['sensory_modality1']} modality for the {t['culture1']} interpretation.
   b) Explain the representation of {t['concept']} using the {t['sensory_modality2']} modality for the {t['culture2']} interpretation.
   c) Discuss how these sensory representations capture the essence of the concept in each cultural context.
   d) Address any limitations or challenges in using these specific sensory modalities.

4. Cross-Modal Translation Process (200-250 words):
   a) Explain the process of translating between the {t['sensory_modality1']} and {t['sensory_modality2']} representations.
   b) Discuss how your system preserves the core meaning of the concept across modalities.
   c) Address any potential loss or distortion of information in this translation process.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and cultural authenticity of your system's representations.
   b) Suggest experiments to validate the effectiveness of the cross-modal and cross-cultural translations.
   c) Discuss potential biases in your system and how you would mitigate them.

6. Ethical Considerations and Implications (150-200 words):
   a) Discuss ethical issues related to representing and translating cultural concepts.
   b) Address potential misuse or misinterpretation of your system's outputs.
   c) Propose guidelines for the responsible development and use of such AI systems.

Ensure your response demonstrates a deep understanding of cross-cultural communication, sensory perception, and abstract reasoning. Use appropriate terminology from relevant fields and provide clear explanations for complex ideas. Be innovative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and adheres to the specified word count limits for each section.",
            f"The system design demonstrates a deep understanding of cross-cultural communication, sensory perception, and abstract reasoning, particularly in relation to the concept of {t['concept']}.",
            f"The analysis of {t['concept']} shows a nuanced understanding of both {t['culture1']} and {t['culture2']} perspectives.",
            f"The sensory representations using {t['sensory_modality1']} and {t['sensory_modality2']} modalities are creative, culturally appropriate, and effectively capture the essence of the concept.",
            "The cross-modal translation process is well-explained and addresses potential challenges and limitations.",
            "The proposed evaluation methods and ethical considerations are thoughtful and comprehensive.",
            "The overall response demonstrates creativity, cultural sensitivity, and scientific rigor in its approach to cross-modal cultural concept translation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
