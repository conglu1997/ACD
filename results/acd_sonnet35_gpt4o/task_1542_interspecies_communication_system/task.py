import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species_pairs = [
            ("Dolphin", "Honeybee"),
            ("Octopus", "Bat"),
            ("Elephant", "Mantis Shrimp"),
            ("Slime Mold", "Hummingbird"),
            ("Tree", "Ant Colony")
        ]
        communication_types = [
            "Mating rituals",
            "Danger warnings",
            "Food source locations",
            "Social hierarchies",
            "Environmental changes"
        ]
        return {
            "1": {"species_pair": random.choice(species_pairs), "communication_type": random.choice(communication_types)},
            "2": {"species_pair": random.choice(species_pairs), "communication_type": random.choice(communication_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        species1, species2 = t['species_pair']
        return f"Design a hypothetical communication system that allows {species1}s and {species2}s to exchange information about {t['communication_type']}. Your response should include:\n\n1. Species Analysis (200-250 words):\n   a) Briefly describe the sensory capabilities and cognitive structures of both species.\n   b) Identify the key challenges in enabling communication between these species.\n   c) Discuss any existing communication methods used by each species that could be leveraged.\n\n2. Communication System Design (300-350 words):\n   a) Propose an innovative communication system that bridges the gap between the two species.\n   b) Explain how your system accounts for the different sensory modalities and cognitive abilities of each species.\n   c) Describe the basic 'vocabulary' or 'grammar' of your communication system.\n   d) Discuss how your system ensures accurate and efficient information transfer.\n\n3. Information Encoding and Decoding (200-250 words):\n   a) Explain how information about {t['communication_type']} would be encoded in your system.\n   b) Describe the process by which each species would decode messages from the other.\n   c) Provide an example of a specific message being encoded and decoded in your system.\n\n4. Implementation and Training (150-200 words):\n   a) Propose a method for implementing your communication system in practice.\n   b) Describe how individuals of each species would learn to use the system.\n   c) Discuss any potential challenges in the implementation and how they might be overcome.\n\n5. Evolutionary and Ecological Implications (150-200 words):\n   a) Speculate on how this interspecies communication system might affect the evolution of both species.\n   b) Discuss potential ecological impacts of enabling this type of communication.\n   c) Consider any unintended consequences that might arise from this system.\n\n6. Broader Applications (150-200 words):\n   a) Suggest two potential applications of your communication system design beyond interspecies communication.\n   b) Discuss how insights from this design might inform human-AI communication or other fields.\n\nEnsure your response demonstrates a deep understanding of biology, information theory, and linguistics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1150-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the biology and sensory capabilities of both species.",
            "The proposed communication system is innovative and scientifically plausible.",
            "The design effectively addresses the challenges of interspecies communication.",
            "The information encoding and decoding process is clearly explained and logically sound.",
            "The response considers implementation, ecological implications, and broader applications of the system.",
            "The overall response is well-structured, creative, and demonstrates interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
