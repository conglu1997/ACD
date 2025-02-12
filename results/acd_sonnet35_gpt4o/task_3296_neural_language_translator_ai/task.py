import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                "region": "Broca's area",
                "function": "speech production",
                "constraint": "minimize invasiveness"
            },
            {
                "region": "Wernicke's area",
                "function": "language comprehension",
                "constraint": "real-time processing"
            }
        ]
        return {
            "1": random.choice(brain_regions),
            "2": random.choice(brain_regions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are a leading expert in neuroscience, artificial intelligence, and natural language processing. Your task is to design an AI system capable of bidirectional translation between neural activity patterns in {t['region']} and natural language, focusing on its role in {t['function']}. Your design must address the constraint of {t['constraint']}. Then, analyze its potential applications and ethical implications in neuroscience and communication.\n\nYour response should include the following sections:\n\n1. Neural-Linguistic Interface (300-350 words):\n   a) Describe the overall architecture of your AI system for neural-to-language and language-to-neural translation.\n   b) Explain how your system interfaces with {t['region']} to capture and interpret neural activity related to {t['function']}.\n   c) Detail the key components and algorithms used in your translation process.\n   d) Discuss any novel approaches or technologies incorporated in your design.\n   e) Explain how your design addresses the constraint of {t['constraint']}.\n\n2. Data Processing and Machine Learning (250-300 words):\n   a) Explain the data preprocessing steps for both neural signals and language inputs.\n   b) Describe the machine learning models used for the bidirectional translation.\n   c) Discuss how your system handles variability in neural patterns across individuals.\n   d) Explain how the system learns and improves its translation accuracy over time.\n\n3. Language Model Integration (200-250 words):\n   a) Describe how your system integrates with existing natural language processing models.\n   b) Explain how context and semantics are preserved in the translation process.\n   c) Discuss any limitations in language complexity or expressiveness in your system.\n\n4. Neuroscientific Implications (200-250 words):\n   a) Analyze how your system could contribute to our understanding of {t['function']} and language processing in the brain.\n   b) Discuss potential applications of your system in neuroscience research.\n   c) Explain how your system might be adapted to work with other brain regions involved in language.\n\n5. Practical Applications (150-200 words):\n   a) Propose three potential real-world applications of your neural-linguistic translation system.\n   b) Explain the benefits and challenges of each application.\n   c) Discuss how your system could be integrated with existing technologies or practices.\n\n6. Ethical Considerations (200-250 words):\n   a) Discuss the ethical implications of direct neural-to-language translation technology.\n   b) Address privacy concerns related to decoding thoughts and neural activity.\n   c) Explore potential misuses of this technology and propose safeguards.\n   d) Discuss the societal impact of such technology, including issues of access and inequality.\n\n7. Future Directions (150-200 words):\n   a) Propose two potential improvements or extensions to your system.\n   b) Discuss how advancements in neuroscience or AI might enhance neural-linguistic translation in the future.\n   c) Speculate on the long-term implications of this technology for human communication and cognition.\n\n8. Comparative Analysis (200-250 words):\n   a) Compare your proposed system with existing brain-computer interface technologies.\n   b) Discuss the advantages and limitations of your approach compared to current methods.\n   c) Explain how your system addresses challenges that have hindered progress in this field.\n\nEnsure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.\n\nFormat your response with clear headings for each section. Your total response should be between 1650-2050 words. Begin each section with the heading (e.g., '1. Neural-Linguistic Interface') on a new line, followed by your response for that section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the neural basis of {t['function']} in {t['region']}.",
            "The AI system design is innovative yet plausible, integrating current neuroscientific and AI knowledge.",
            f"The design effectively addresses the constraint of {t['constraint']}.",
            "The response addresses all required sections comprehensively.",
            "The proposed applications and ethical considerations are well-reasoned and insightful.",
            "The response uses appropriate technical terminology from neuroscience, linguistics, and AI fields.",
            "The ideas presented are coherent, well-structured, and demonstrate interdisciplinary thinking.",
            "The comparative analysis provides a thorough evaluation of the proposed system against existing technologies.",
            "The response follows the required format and falls within the specified word count range (1650-2050 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0