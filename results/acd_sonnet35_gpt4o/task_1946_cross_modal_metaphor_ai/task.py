import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'olfactory', 'gustatory', 'tactile']
        abstract_concepts = ['time', 'justice', 'love', 'knowledge', 'freedom', 'chaos', 'infinity', 'consciousness']
        
        tasks = {
            "1": {
                "modality_1": random.choice(sensory_modalities),
                "modality_2": random.choice(sensory_modalities),
                "abstract_concept": random.choice(abstract_concepts)
            },
            "2": {
                "modality_1": random.choice(sensory_modalities),
                "modality_2": random.choice(sensory_modalities),
                "abstract_concept": random.choice(abstract_concepts)
            }
        }
        
        # Ensure the two modalities are different for each task
        while tasks["1"]["modality_1"] == tasks["1"]["modality_2"]:
            tasks["1"]["modality_2"] = random.choice(sensory_modalities)
        
        while tasks["2"]["modality_1"] == tasks["2"]["modality_2"]:
            tasks["2"]["modality_2"] = random.choice(sensory_modalities)
        
        # Ensure the abstract concepts are different for each task
        while tasks["2"]["abstract_concept"] == tasks["1"]["abstract_concept"]:
            tasks["2"]["abstract_concept"] = random.choice(abstract_concepts)
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of understanding and generating metaphors that bridge different sensory modalities, then use it to create novel metaphors for abstract concepts. Focus on bridging the {t['modality_1']} and {t['modality_2']} modalities, and apply your system to create metaphors for the concept of {t['abstract_concept']}. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your AI system and how they interact.\n   b) Explain how your system represents and processes information from different sensory modalities.\n   c) Detail the mechanism for generating cross-modal metaphors.\n   d) Discuss any novel techniques or approaches used in your design.\n\n2. Cognitive and Linguistic Foundations (200-250 words):\n   a) Explain the cognitive and linguistic theories that underpin your system's approach to metaphor generation.\n   b) Discuss how your system accounts for the embodied nature of human cognition in its metaphor creation process.\n   c) Address any challenges in computationally modeling human-like metaphorical thinking.\n\n3. Cross-Modal Mapping (250-300 words):\n   a) Describe how your system creates mappings between the {t['modality_1']} and {t['modality_2']} modalities.\n   b) Provide examples of how features or experiences from one modality might be translated into the other.\n   c) Explain how your system ensures the metaphors remain coherent and meaningful across modalities.\n   d) Provide a brief example of how your system would process a specific input, detailing each step.\n\n4. Metaphor Generation for {t['abstract_concept'].capitalize()} (250-300 words):\n   a) Use your system to generate at least three novel metaphors for {t['abstract_concept']}, bridging the {t['modality_1']} and {t['modality_2']} modalities.\n   b) Explain the reasoning behind each generated metaphor.\n   c) Analyze the strengths and potential limitations of each metaphor in conveying the concept of {t['abstract_concept']}.\n\n5. Evaluation and Refinement (200-250 words):\n   a) Propose methods for evaluating the quality, novelty, and effectiveness of the generated metaphors.\n   b) Describe how you would refine and improve your system based on these evaluations.\n   c) Discuss potential biases or limitations in your approach and how you might address them.\n\n6. Implications and Applications (200-250 words):\n   a) Discuss the potential implications of your system for our understanding of human cognition and creativity.\n   b) Explore possible applications in fields such as education, art, therapy, or human-computer interaction.\n   c) Consider any ethical considerations or potential misuses of such a system.\n\nEnsure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence in the context of cross-modal metaphor generation.",
            f"The proposed AI system architecture is well-described and includes novel approaches to bridging the {t['modality_1']} and {t['modality_2']} modalities.",
            f"The explanation of cognitive and linguistic foundations is thorough and relevant to metaphor generation.",
            f"The cross-modal mapping process is clearly explained with specific examples related to the {t['modality_1']} and {t['modality_2']} modalities.",
            f"A brief example of how the system would process a specific input is provided, detailing each step.",
            f"At least three novel and coherent metaphors for {t['abstract_concept']} are generated, bridging the {t['modality_1']} and {t['modality_2']} modalities.",
            "The generated metaphors are creative, appropriate, and effectively convey the abstract concept.",
            "The evaluation methods, potential applications, and ethical considerations are thoughtfully discussed.",
            "The response is well-structured, creative, and demonstrates interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
