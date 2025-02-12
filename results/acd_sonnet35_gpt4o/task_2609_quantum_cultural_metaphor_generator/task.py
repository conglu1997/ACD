import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Japanese', 'Maori', 'Inuit', 'Yoruba', 'Mayan']
        concepts = ['time', 'love', 'death', 'nature', 'knowledge']
        quantum_principles = ['superposition', 'entanglement', 'quantum tunneling', 'quantum coherence']
        
        return {
            "1": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "concept": random.choice(concepts),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "concept": random.choice(concepts),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-based natural language processing system that can analyze and generate culturally-specific metaphors, then use it to translate metaphors between cultures. Your system should focus on translating metaphors related to the concept of {t['concept']} from {t['source_culture']} culture to {t['target_culture']} culture, while incorporating the quantum principle of {t['quantum_principle']}. Your response should include:

1. Quantum-Cultural Metaphor System Architecture (300-350 words):
   a) Describe the key components of your quantum-based NLP system for metaphor analysis and generation.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your system's design.
   c) Detail how your system integrates cultural knowledge and linguistic patterns.
   d) Provide a high-level diagram or pseudocode illustrating your system's architecture.

2. Quantum-Linguistic Mapping (250-300 words):
   a) Explain how your system maps linguistic structures to quantum states or operations.
   b) Describe how cultural context is encoded in your quantum representation.
   c) Discuss any novel quantum algorithms you've developed for metaphor processing.
   d) Provide an example of how a simple metaphor might be represented in your quantum system.

3. Cultural Knowledge Integration (200-250 words):
   a) Describe how your system acquires and represents knowledge about {t['source_culture']} and {t['target_culture']} cultures.
   b) Explain how this cultural knowledge influences metaphor analysis and generation.
   c) Discuss any challenges in representing diverse cultural perspectives in a quantum framework.

4. Metaphor Translation Process (250-300 words):
   a) Outline the step-by-step process your system uses to translate a metaphor from {t['source_culture']} to {t['target_culture']} culture.
   b) Explain how quantum operations are used in this translation process.
   c) Provide an example of translating a specific metaphor for {t['concept']} between these cultures.
   d) Discuss how your system ensures cultural sensitivity and accuracy in translations.

5. Evaluation and Limitations (200-250 words):
   a) Propose methods to evaluate the accuracy and cultural appropriateness of your system's metaphor translations.
   b) Discuss the limitations of your quantum-cultural metaphor system.
   c) Suggest potential improvements or extensions to your system.

6. Ethical Considerations and Implications (200-250 words):
   a) Discuss ethical implications of using quantum AI for cultural metaphor translation.
   b) Address potential issues of cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of such systems.
   d) Explore potential applications and impacts of your system in fields like intercultural communication, education, or AI ethics.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, cultural anthropology, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of quantum computing, particularly {t['quantum_principle']}, and how it can be applied to natural language processing.",
            f"The system architecture effectively integrates quantum computing principles with cultural and linguistic knowledge for metaphor analysis and generation.",
            f"The approach to translating metaphors between {t['source_culture']} and {t['target_culture']} cultures is well-explained and culturally sensitive.",
            "The quantum-linguistic mapping is innovative and logically consistent.",
            "The cultural knowledge integration process is comprehensive and addresses the challenges of representing diverse cultural perspectives.",
            "The metaphor translation process is clearly outlined and includes a specific example related to the given concept.",
            "The evaluation methods and limitations are thoughtfully discussed.",
            "Ethical considerations are thoroughly addressed, including issues of cultural appropriation and responsible AI development.",
            "The response is well-structured, coherent, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
