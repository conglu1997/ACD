import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_areas = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Supramarginal gyrus",
            "Arcuate fasciculus"
        ]
        linguistic_phenomena = [
            "Syntactic processing",
            "Semantic comprehension",
            "Phonological awareness",
            "Lexical retrieval",
            "Pragmatic interpretation"
        ]
        vr_applications = [
            "Language learning",
            "Aphasia rehabilitation",
            "Linguistic research",
            "Cross-cultural communication training",
            "Neurodiversity awareness"
        ]
        return {
            "1": {
                "brain_area": random.choice(language_areas),
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "vr_application": random.choice(vr_applications)
            },
            "2": {
                "brain_area": random.choice(language_areas),
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "vr_application": random.choice(vr_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a virtual reality system that simulates altered states of language perception based on neurolinguistic principles. Your system should focus on the {t['brain_area']} and its role in {t['linguistic_phenomenon']}. Then, analyze its potential applications in {t['vr_application']} and broader implications. Your response should include the following sections:\n\n1. Neurolinguistic Basis (250-300 words):\n   a) Explain the function of the {t['brain_area']} in language processing.\n   b) Describe how {t['linguistic_phenomenon']} is typically processed in the brain.\n   c) Propose a hypothesis about how altering the function of this brain area might affect language perception.\n\n2. VR System Design (300-350 words):\n   a) Describe the key components of your VR system for simulating altered language perception.\n   b) Explain how your system simulates changes in the functioning of the {t['brain_area']}.\n   c) Detail how users would interact with the system and experience altered {t['linguistic_phenomenon']}.\n   d) Propose a novel feature that distinguishes your system from existing VR language simulations.\n   e) Include a simple diagram or flowchart of your system's architecture (describe it textually).\n\n3. User Experience Simulation (200-250 words):\n   a) Provide a detailed scenario of a user's experience in your VR environment.\n   b) Describe specific examples of how {t['linguistic_phenomenon']} would be altered in this simulation.\n   c) Explain how the simulation maintains scientific accuracy while providing an immersive experience.\n\n4. Applications in {t['vr_application']} (200-250 words):\n   a) Analyze how your VR system could be applied in the field of {t['vr_application']}.\n   b) Discuss potential benefits and challenges of using this system in this context.\n   c) Propose a specific use case or experiment utilizing your system in this field.\n\n5. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss potential ethical implications of simulating altered language perception.\n   b) Address concerns related to psychological effects on users and potential misuse.\n   c) Identify limitations of your system and areas where further research is needed.\n\n6. Broader Implications and Future Directions (150-200 words):\n   a) Discuss how your system might contribute to our understanding of language processing and perception.\n   b) Propose two potential advancements or modifications to your system for future development.\n   c) Suggest a research agenda for further exploring the intersection of neurolinguistics and VR technology.\n\nEnsure your response demonstrates a deep understanding of neuroscience, linguistics, and VR technology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific accuracy and plausibility.\n\nFormat your response with clear headings for each section and use the following structure for each section:\n\n[Section Title]\n[Your content here]\n\nYour total response should be between 1250-1550 words.\n\nNote: Your response will be evaluated based on scientific accuracy, creativity, and the integration of concepts from neuroscience, linguistics, and VR technology. Ensure that your proposed system is innovative yet grounded in current scientific understanding."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            f"The neurolinguistic basis demonstrates a clear and accurate understanding of the {t['brain_area']} and its role in {t['linguistic_phenomenon']}.",
            "The VR system design is innovative, coherent, and scientifically plausible, with a novel feature clearly described.",
            f"The user experience simulation provides a vivid and scientifically accurate description of altered {t['linguistic_phenomenon']} perception.",
            f"The application in {t['vr_application']} is well-analyzed, presents a compelling use case, and addresses potential challenges.",
            "The ethical considerations and limitations section thoughtfully addresses potential issues and areas for further research.",
            "The broader implications section provides insightful contributions to language processing understanding and proposes feasible future directions.",
            "The response demonstrates creativity, interdisciplinary knowledge integration, and critical thinking throughout.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
