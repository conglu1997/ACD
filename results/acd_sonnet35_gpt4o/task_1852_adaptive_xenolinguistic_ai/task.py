import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        communication_types = [
            "Visual patterns",
            "Acoustic frequencies",
            "Chemical signals",
            "Electromagnetic pulses",
            "Gravitational waves"
        ]
        cognitive_structures = [
            "Hive mind",
            "Distributed consciousness",
            "Time-dilated perception",
            "Multidimensional thinking",
            "Quantum entangled cognition"
        ]
        environmental_factors = [
            "Extreme gravity",
            "Liquid methane atmosphere",
            "Plasma state matter",
            "Subterranean habitat",
            "Interstellar void"
        ]
        
        return {
            "1": {
                "communication_type": random.choice(communication_types),
                "cognitive_structure": random.choice(cognitive_structures),
                "environmental_factor": random.choice(environmental_factors)
            },
            "2": {
                "communication_type": random.choice(communication_types),
                "cognitive_structure": random.choice(cognitive_structures),
                "environmental_factor": random.choice(environmental_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of rapidly learning and adapting to an alien species' language or communication system in real-time. The alien species uses {t['communication_type']} for communication, has a {t['cognitive_structure']}, and lives in an environment characterized by {t['environmental_factor']}. Your response should include:\n\n1. AI System Architecture (250-300 words):\n   a) Describe the key components of your AI system for rapid language acquisition.\n   b) Explain how it processes and adapts to the alien species' unique communication type.\n   c) Discuss how the system accounts for the species' cognitive structure in its learning process.\n\n2. Learning Algorithm (200-250 words):\n   a) Outline the core learning algorithm or approach your AI system uses.\n   b) Explain how it differs from traditional natural language processing techniques.\n   c) Describe how the algorithm rapidly generates and tests hypotheses about the alien language.\n\n3. Sensory Processing and Output Generation (200-250 words):\n   a) Detail how your system processes the alien species' {t['communication_type']}.\n   b) Explain how it generates responses using the same communication modality.\n   c) Discuss any challenges posed by the {t['environmental_factor']} and how your system overcomes them.\n\n4. Cognitive Modeling (200-250 words):\n   a) Describe how your AI system models and interacts with the aliens' {t['cognitive_structure']}.\n   b) Explain how this modeling improves the system's language acquisition and communication.\n   c) Discuss any ethical considerations in modeling non-human cognition.\n\n5. Real-time Adaptation Mechanisms (150-200 words):\n   a) Explain how your system adapts to new information and corrects errors in real-time.\n   b) Describe the feedback mechanisms that enable continuous learning and improvement.\n   c) Discuss how the system maintains coherence and consistency in its language model as it learns.\n\n6. Cross-cultural and Pragmatic Understanding (150-200 words):\n   a) Explain how your AI system goes beyond literal translation to understand cultural context and pragmatic meaning.\n   b) Describe how it handles concepts that may not have direct equivalents in human languages.\n   c) Discuss strategies for avoiding or resolving potential misunderstandings.\n\n7. Limitations and Future Improvements (150-200 words):\n   a) Identify potential limitations of your proposed AI system.\n   b) Suggest areas for future research or improvements.\n   c) Discuss how this technology could be applied to other scenarios beyond alien communication.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence principles.",
            "The AI system design is innovative, plausible, and well-suited to the specific alien communication type, cognitive structure, and environmental factor.",
            "The response addresses all required sections comprehensively and coherently.",
            "The proposed system effectively integrates interdisciplinary concepts and demonstrates creative problem-solving.",
            "Ethical considerations and limitations are thoughtfully analyzed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
