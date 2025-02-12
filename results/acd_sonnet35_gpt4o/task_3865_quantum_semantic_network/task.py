import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'interference']
        cognitive_processes = ['semantic memory', 'contextual inference', 'analogical reasoning']
        nlp_challenges = ['word sense disambiguation', 'metaphor comprehension', 'pragmatic inference']
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "nlp_challenge": random.choice(nlp_challenges)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "nlp_challenge": random.choice(nlp_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired language model that captures the contextual and probabilistic nature of semantic networks in human cognition, then apply it to solve a complex natural language understanding problem. Your model should incorporate the quantum principle of {t['quantum_principle']}, focus on the cognitive process of {t['cognitive_process']}, and address the NLP challenge of {t['nlp_challenge']}. Your response should include:\n\n1. Quantum Semantic Network Model (300-350 words):\n   a) Describe the key components and architecture of your quantum-inspired language model.\n   b) Explain how it incorporates the specified quantum principle to represent semantic relationships.\n   c) Detail how your model simulates the given cognitive process.\n   d) Provide a mathematical formulation or pseudocode for a core function of your model.\n\n2. Quantum-Cognitive Integration (250-300 words):\n   a) Analyze how your model integrates quantum mechanics with cognitive theories of language processing.\n   b) Discuss potential insights this integration might offer into human language understanding.\n   c) Explain any novel emergent properties or behaviors in your quantum semantic network.\n\n3. NLP Challenge Application (250-300 words):\n   a) Apply your quantum semantic network model to the specified NLP challenge.\n   b) Provide a step-by-step explanation of how your model processes and solves the problem.\n   c) Discuss potential advantages of your approach compared to classical NLP methods.\n   d) Propose a method for evaluating the performance of your quantum-inspired NLP solution.\n\n4. Theoretical Implications (200-250 words):\n   a) Discuss how your model challenges or extends current theories in cognitive science and NLP.\n   b) Analyze the philosophical implications of using quantum principles to model human language processing.\n   c) Propose testable hypotheses derived from your quantum semantic network model.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues arising from the development and use of quantum-inspired language models.\n   b) Discuss how these issues might be addressed or mitigated.\n   c) Propose guidelines for responsible development and use of this technology.\n\n6. Future Directions (150-200 words):\n   a) Suggest potential improvements or extensions to your quantum semantic network model.\n   b) Discuss how advancements in quantum computing might impact the future development of your model.\n   c) Propose novel applications of your model in fields beyond NLP.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and natural language processing. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, cognitive science, and natural language processing.",
            "The proposed quantum semantic network model is innovative, scientifically plausible, and well-explained.",
            "The integration of quantum principles with cognitive theories is thoughtfully analyzed and offers novel insights.",
            "The application to the NLP challenge is thorough and demonstrates clear advantages over classical methods.",
            "Ethical considerations are thoughtfully addressed and future implications are creatively explored.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        result = eval_with_llm_judge(instructions, submission, criteria)
        return 1.0 if result else 0.0
