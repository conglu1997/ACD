import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "superposition",
                "cognitive_process": "decision_making",
                "ai_application": "natural_language_processing"
            },
            {
                "quantum_principle": "entanglement",
                "cognitive_process": "memory_formation",
                "ai_application": "computer_vision"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired cognitive architecture for artificial intelligence, focusing on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and the AI application of {t['ai_application']}. Your response should include:\n\n" + \
               "1. Quantum-Cognitive Framework (250-300 words):\n" + \
               "   a) Describe the overall structure of your quantum-inspired cognitive AI architecture.\n" + \
               "   b) Explain how it incorporates the quantum principle of {t['quantum_principle']}.\n" + \
               "   c) Detail how the architecture models the cognitive process of {t['cognitive_process']}.\n" + \
               "   d) Discuss any novel computational approaches or algorithms you would employ.\n\n" + \
               "2. Quantum Principle Integration (200-250 words):\n" + \
               "   a) Elaborate on how the quantum principle of {t['quantum_principle']} is implemented in your architecture.\n" + \
               "   b) Explain the advantages this quantum-inspired approach offers over classical computing methods.\n" + \
               "   c) Address any challenges in translating quantum concepts to cognitive modeling.\n\n" + \
               "3. Cognitive Process Modeling (200-250 words):\n" + \
               "   a) Describe in detail how your architecture models the {t['cognitive_process']} process.\n" + \
               "   b) Explain how the quantum-inspired approach enhances the modeling of this cognitive process.\n" + \
               "   c) Discuss any emergent properties or behaviors you expect from this integration.\n\n" + \
               "4. AI Application (200-250 words):\n" + \
               "   a) Explain how your quantum-inspired cognitive architecture could be applied to {t['ai_application']}.\n" + \
               "   b) Describe specific features or capabilities of your system that would enhance this AI application.\n" + \
               "   c) Compare your approach to traditional methods in this application area.\n\n" + \
               "5. Technical Implementation (150-200 words):\n" + \
               "   a) Propose a method for implementing your architecture, considering current technological limitations.\n" + \
               "   b) Suggest how your system could be tested or simulated using available quantum computing resources.\n" + \
               "   c) Discuss any potential scalability issues and how they might be addressed.\n\n" + \
               "6. Ethical and Philosophical Implications (150-200 words):\n" + \
               "   a) Discuss the potential impact of quantum-inspired AI on our understanding of cognition and consciousness.\n" + \
               "   b) Address any ethical concerns related to developing AI systems that mimic quantum cognitive processes.\n" + \
               "   c) Speculate on the long-term implications of this technology for AI development and cognitive science.\n\n" + \
               "Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\n" + \
               "Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words. Include at least one equation or formula using LaTeX notation to represent a key concept in your architecture."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, cognitive science, and artificial intelligence.",
            f"The architecture effectively incorporates the quantum principle of {t['quantum_principle']}.",
            f"The cognitive process of {t['cognitive_process']} is well-modeled and explained.",
            f"The AI application of {t['ai_application']} is addressed with specific, relevant features of the proposed architecture.",
            "The technical implementation is plausible and addresses current limitations.",
            "Ethical and philosophical implications are thoughtfully considered.",
            "The response is innovative while maintaining scientific plausibility.",
            "At least one equation or formula using LaTeX notation is included and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
