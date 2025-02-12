import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "superposition",
            "entanglement",
            "tunneling",
            "coherence",
            "quantum collapse"
        ]
        cognitive_processes = [
            "decision making",
            "memory formation",
            "attention",
            "learning",
            "perception"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "quantum_effect": random.choice(quantum_effects),
                "cognitive_process": random.choice(cognitive_processes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of simulating the quantum effect of {t['quantum_effect']} in neural networks, specifically focusing on its potential role in the cognitive process of {t['cognitive_process']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI system that enable quantum neural simulation.\n   b) Explain how these components interact to model both quantum and neural dynamics.\n   c) Discuss any novel algorithms or techniques your system would use to bridge quantum mechanics and neuroscience.\n\n2. Quantum-Neural Interface (200-250 words):\n   a) Detail how your system models the interaction between quantum effects and neural activity.\n   b) Explain how {t['quantum_effect']} is incorporated into the neural network model.\n   c) Discuss the challenges in simulating quantum effects at the scale of neural networks and how your system addresses them.\n\n3. Cognitive Process Simulation (200-250 words):\n   a) Describe how your system simulates the cognitive process of {t['cognitive_process']}.\n   b) Explain how the incorporation of quantum effects might alter our understanding of this process.\n   c) Propose a specific hypothesis about how {t['quantum_effect']} might influence {t['cognitive_process']}.\n\n4. Experimental Design (150-200 words):\n   a) Propose an experiment using your system to test the hypothesis you formulated.\n   b) Describe the data you would collect and how you would analyze it.\n   c) Discuss potential outcomes and their implications for our understanding of quantum effects in cognition.\n\n5. Implications for Consciousness (150-200 words):\n   a) Discuss how your system and its findings might contribute to our understanding of consciousness.\n   b) Explain how quantum effects in neural networks could potentially explain aspects of subjective experience.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Identify potential ethical concerns or implications of your system and its applications.\n   b) Discuss the limitations of your approach and potential future improvements.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and AI systems. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} and how it might relate to neural networks and {t['cognitive_process']}",
            "The proposed AI system presents a plausible and creative approach to simulating quantum effects in neural networks",
            "The experimental design is well-thought-out and addresses the challenges of bridging quantum mechanics and neuroscience",
            "The implications for consciousness are thoroughly and insightfully discussed",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
