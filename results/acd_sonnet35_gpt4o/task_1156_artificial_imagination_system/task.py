import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "Time",
            "Freedom",
            "Justice",
            "Chaos",
            "Harmony",
            "Evolution",
            "Infinity",
            "Consciousness",
            "Entropy",
            "Synergy",
            "Emergence",
            "Duality"
        ]
        imagery_types = [
            "Visual",
            "Auditory",
            "Tactile",
            "Olfactory",
            "Gustatory",
            "Kinesthetic"
        ]
        cognitive_processes = [
            "Memory consolidation",
            "Conceptual blending",
            "Analogical reasoning",
            "Pattern recognition",
            "Emotional processing",
            "Abstraction",
            "Mental rotation",
            "Counterfactual thinking"
        ]
        
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "imagery_type": random.choice(imagery_types),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "imagery_type": random.choice(imagery_types),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system for generating and manipulating mental imagery, then use it to create a vivid scene based on the abstract concept of '{t['concept']}'. Your response should include the following sections:\n\n1. System Architecture (275-325 words):\n   a) Describe the key components of your artificial imagination system.\n   b) Explain how it generates and manipulates mental imagery, focusing on {t['imagery_type']} imagery.\n   c) Discuss how it incorporates the cognitive process of {t['cognitive_process']}.\n   d) Explain any novel AI techniques or algorithms your system employs.\n   e) Ensure your design is scientifically plausible and grounded in current AI and cognitive science research.\n\n2. Cognitive Model (225-275 words):\n   a) Describe how your system models the cognitive processes involved in imagination.\n   b) Explain how it represents and manipulates abstract concepts.\n   c) Discuss how your system accounts for the subjective and personal nature of imagination.\n\n3. Scene Generation (275-325 words):\n   a) Use your artificial imagination system to generate a vivid scene based on the concept of '{t['concept']}'.\n   b) Describe the scene in detail, emphasizing {t['imagery_type']} elements.\n   c) Explain how the scene incorporates or represents the abstract concept.\n   d) Discuss how the cognitive process of {t['cognitive_process']} influenced the scene generation.\n\n4. Analysis and Implications (225-275 words):\n   a) Analyze the strengths and limitations of your artificial imagination system.\n   b) Discuss potential applications of your system in fields such as AI, psychology, or the arts.\n   c) Explore the philosophical implications of artificial imagination for our understanding of consciousness and creativity.\n\n5. Ethical Considerations (175-225 words):\n   a) Discuss potential ethical issues related to developing and using artificial imagination systems.\n   b) Propose guidelines for the responsible development and use of such technology.\n\nEnsure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the nature of imagination. Be creative in your system design and scene generation while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1175-1425 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science and artificial intelligence principles.",
            "The artificial imagination system design is innovative, plausible, and well-explained.",
            "The system effectively incorporates the specified imagery type and cognitive process.",
            "The generated scene is vivid, creative, and clearly relates to the given abstract concept.",
            "The analysis of the system's implications and ethical considerations is thoughtful and comprehensive.",
            "The response addresses all required sections coherently and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
