import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "freedom",
            "time",
            "love",
            "justice",
            "knowledge",
            "chaos",
            "harmony"
        ]
        sensory_modalities = [
            "visual",
            "auditory",
            "tactile",
            "olfactory",
            "gustatory"
        ]
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice([m for m in sensory_modalities if m != "primary_modality"])
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "primary_modality": random.choice(sensory_modalities),
                "secondary_modality": random.choice([m for m in sensory_modalities if m != "primary_modality"])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system based on synesthesia, focusing on the abstract concept of {t['concept']}. Your system should primarily use the {t['primary_modality']} modality, with the {t['secondary_modality']} modality as a secondary component. Your task has the following parts:

1. Synesthetic Encoding System (250-300 words):
   a) Describe how your system encodes the concept of {t['concept']} using {t['primary_modality']} and {t['secondary_modality']} sensory inputs.
   b) Explain the rationale behind your encoding choices, drawing from principles of neuroscience, information theory, and synesthesia research.
   c) Provide an example of how a specific aspect of {t['concept']} would be encoded in your system.

2. Communication Protocol (200-250 words):
   a) Outline the basic 'grammar' or structure of your communication system.
   b) Explain how complex ideas related to {t['concept']} can be conveyed using combinations of your basic encodings.
   c) Describe how your system handles ambiguity or nuance in communication.

3. Message Encoding and Decoding (200-250 words):
   a) Encode the message "{t['concept']} is essential for human flourishing" using your system. Provide a detailed description of the resulting sensory experience.
   b) Explain the decoding process: how would someone trained in your system interpret this message?
   c) Discuss potential challenges in encoding and decoding, and how your system addresses them.

4. Learning and Adaptation (150-200 words):
   a) Describe how someone would learn to use your communication system.
   b) Explain how your system could adapt to convey concepts or ideas it wasn't originally designed for.
   c) Discuss the potential for your system to enhance cognitive abilities or alter perception in its users.

5. Cross-modal Integration (150-200 words):
   a) Explain how your system integrates information from {t['primary_modality']} and {t['secondary_modality']} modalities.
   b) Discuss any synergistic effects or emergent properties that arise from this integration.
   c) Compare your system's cross-modal integration to natural synesthesia in humans.

6. Practical Applications and Implications (200-250 words):
   a) Propose two potential real-world applications for your synesthetic communication system.
   b) Discuss how your system might influence our understanding of perception, cognition, or consciousness.
   c) Address any ethical considerations or potential negative consequences of using such a system.

Ensure your response demonstrates a deep understanding of sensory perception, information encoding, and cognitive science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs a synesthetic communication system for the concept of {t['concept']} using {t['primary_modality']} and {t['secondary_modality']} modalities.",
            "The encoding system and communication protocol are well-explained, scientifically plausible, and include specific examples.",
            "The response demonstrates a deep understanding of sensory perception, information encoding, and cognitive science, using appropriate technical terminology.",
            "The system's learning process, adaptability, and cross-modal integration are thoroughly discussed.",
            "The response is creative and innovative while maintaining scientific rigor, and proposes practical applications and implications.",
            "The response follows the specified format, including clear headings and staying within the word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
