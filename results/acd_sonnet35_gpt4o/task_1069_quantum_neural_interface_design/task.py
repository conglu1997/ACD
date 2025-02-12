import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            "Memory enhancement",
            "Pattern recognition",
            "Decision-making",
            "Language processing"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum error correction"
        ]
        
        tasks = {}
        for i in range(1, 3):
            cognitive_function = random.choice(cognitive_functions)
            quantum_principle = random.choice(quantum_principles)
            tasks[str(i)] = {
                "cognitive_function": cognitive_function,
                "quantum_principle": quantum_principle
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical quantum-neural interface that enhances the cognitive function of {t['cognitive_function']} by leveraging the quantum principle of {t['quantum_principle']}. Your response should include:\n\n1. Interface Design (300-350 words):\n   a) Describe the overall architecture of your quantum-neural interface.\n   b) Explain how it incorporates the specified quantum principle.\n   c) Detail how the interface interacts with biological neural networks to enhance the given cognitive function.\n   d) Provide a conceptual diagram of your interface (describe it textually).\n\n2. Quantum-Neural Integration (250-300 words):\n   a) Explain how your interface translates quantum states into neural signals and vice versa.\n   b) Describe how the specified quantum principle enhances or modifies the given cognitive function.\n   c) Discuss potential challenges in integrating quantum and biological systems and how you address them.\n\n3. Cognitive Enhancement Mechanism (200-250 words):\n   a) Provide a detailed explanation of how your interface enhances the specified cognitive function.\n   b) Compare the potential advantages of your quantum-enhanced approach to traditional cognitive enhancement methods.\n   c) Speculate on potential side effects or unintended consequences of this enhancement.\n\n4. Ethical and Safety Considerations (200-250 words):\n   a) Discuss the ethical implications of enhancing human cognition through quantum-neural interfaces.\n   b) Analyze potential safety risks and propose safeguards or guidelines for the development and use of such technology.\n   c) Consider the societal impact of widespread adoption of quantum-enhanced cognition.\n\n5. Future Research Directions (150-200 words):\n   a) Propose two potential applications of your quantum-neural interface beyond the specified cognitive function.\n   b) Suggest an experiment to test the effectiveness and safety of your interface.\n   c) Discuss how this technology might impact the fields of neuroscience, quantum computing, or artificial intelligence.\n\nEnsure your response demonstrates a deep understanding of quantum physics principles, neuroscience, and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1100-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['quantum_principle']} and {t['cognitive_function']}",
            "The quantum-neural interface design is innovative yet scientifically plausible",
            "The explanation of how the interface enhances cognitive function is clear and well-reasoned",
            "The ethical and safety considerations are thoroughly analyzed",
            "The response shows strong interdisciplinary knowledge integration across quantum physics, neuroscience, and AI"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
