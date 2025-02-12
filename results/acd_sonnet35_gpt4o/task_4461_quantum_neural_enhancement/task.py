import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_abilities = [
            "Memory consolidation and retrieval",
            "Pattern recognition and abstract reasoning",
            "Multitasking and cognitive flexibility",
            "Emotional regulation and empathy",
            "Language acquisition and processing"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum annealing"
        ]
        return {
            "1": {
                "cognitive_ability": random.choice(cognitive_abilities),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "cognitive_ability": random.choice(cognitive_abilities),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical quantum neural network model that could potentially enhance human {t['cognitive_ability']}, incorporating the quantum principle of {t['quantum_principle']}. Your response should include the following sections:\n\n1. Quantum Neural Network Architecture (300-350 words):\n   a) Describe the overall structure of your quantum neural network model.\n   b) Explain how it integrates classical neural network principles with quantum computing concepts.\n   c) Detail how the specified quantum principle is incorporated into the model.\n   d) Discuss how this architecture could theoretically interface with the human brain.\n   e) Include a diagram or schematic representation of your model (describe it textually).\n\n2. Enhancement Mechanism (250-300 words):\n   a) Explain the theoretical mechanism by which your model enhances the specified cognitive ability.\n   b) Describe how quantum effects contribute to this enhancement.\n   c) Discuss potential advantages over classical neural network approaches.\n   d) Provide a hypothetical example of how this enhancement might manifest in human cognition.\n\n3. Implementation Challenges (200-250 words):\n   a) Identify at least three key technical challenges in realizing this quantum neural network model.\n   b) Discuss biological compatibility issues and potential solutions.\n   c) Address any quantum coherence and decoherence concerns in the context of the brain.\n\n4. Ethical and Societal Implications (200-250 words):\n   a) Analyze at least three potential ethical issues arising from enhancing human cognitive abilities.\n   b) Discuss societal impacts, including potential inequality and accessibility concerns.\n   c) Propose specific guidelines for responsible development and use of such technology.\n\n5. Experimental Validation (150-200 words):\n   a) Propose a detailed method to test and validate your model's effects on human cognition.\n   b) Describe at least three key metrics and experimental design considerations.\n   c) Discuss potential risks and specific safety measures in human trials.\n\n6. Future Research Directions (150-200 words):\n   a) Suggest two specific potential extensions or improvements to your model.\n   b) Propose a detailed research question that could further explore the intersection of quantum computing, neuroscience, and AI.\n   c) Speculate on at least three potential long-term implications for human evolution and society.\n\n7. Case Study (200-250 words):\n   Provide a hypothetical case study demonstrating the application of your quantum neural network model in enhancing {t['cognitive_ability']} for a specific individual or group. Include potential outcomes and challenges.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence.",
            "The quantum neural network model is innovative, scientifically plausible, and clearly incorporates the specified quantum principle.",
            "The enhancement mechanism is well-explained and logically connected to the specified cognitive ability.",
            "At least three implementation challenges are identified and thoroughly addressed.",
            "At least three ethical issues are analyzed, and specific guidelines for responsible development are proposed.",
            "The experimental validation method is detailed, with at least three key metrics and specific safety measures discussed.",
            "Future research directions are insightful, with two specific extensions and a detailed research question proposed.",
            "The case study effectively demonstrates the application of the model to the specified cognitive ability.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts.",
            "The response meets the specified word count requirements (1450-1800 words) and includes all required sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
