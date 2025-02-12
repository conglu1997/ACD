import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            {
                "function": "Working Memory",
                "description": "The cognitive system responsible for temporarily holding and manipulating information."
            },
            {
                "function": "Pattern Recognition",
                "description": "The cognitive ability to identify and categorize complex patterns in sensory input."
            }
        ]
        return {
            "1": random.choice(cognitive_functions),
            "2": random.choice(cognitive_functions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that uses quantum computing principles to simulate and potentially enhance the human cognitive function of {t['function']}. {t['description']}\n\nYour response should include the following sections:\n\n1. Quantum-Cognitive Model (250-300 words):\n   a) Describe the key components of your AI system and how they relate to {t['function']}.\n   b) Explain how specific quantum principles (e.g., superposition, entanglement) are integrated into your model.\n   c) Discuss how your model simulates or enhances {t['function']}.\n   d) Provide a detailed text-based visualization (e.g., ASCII art or structured text) of your quantum-cognitive model. This visualization is mandatory.\n\n2. Quantum Advantage (200-250 words):\n   a) Explain the specific quantum computing algorithms (e.g., Grover's algorithm, quantum Fourier transform) your system employs.\n   b) Discuss how these quantum elements provide an advantage over classical computing approaches for modeling {t['function']}.\n   c) Address any potential limitations or challenges in implementing quantum computing for this cognitive function.\n   d) Provide a concrete example or use case demonstrating the quantum advantage in your system.\n\n3. Cognitive Enhancement Potential (200-250 words):\n   a) Describe how your system could potentially enhance {t['function']} beyond normal human capabilities.\n   b) Propose a specific method to measure and quantify this enhancement, including metrics and experimental design.\n   c) Discuss the potential impact of such enhancement on human cognition and behavior, providing at least two specific examples.\n\n4. Ethical Implications (150-200 words):\n   a) Identify at least three ethical concerns raised by your quantum-cognitive AI system.\n   b) Analyze these concerns using a specific ethical framework (e.g., utilitarianism, deontology).\n   c) Propose detailed guidelines for the responsible development and use of quantum-cognitive AI technologies.\n\n5. Experimental Design (200-250 words):\n   a) Propose a comprehensive experiment to test the efficacy of your quantum-cognitive AI system in simulating or enhancing {t['function']}.\n   b) Describe the methodology in detail, including control groups, sample size, and specific measurement techniques.\n   c) Discuss potential confounding factors and how you would address them.\n   d) Outline expected results and their implications for your quantum-cognitive model.\n\nEnsure your response demonstrates a deep understanding of quantum computing, cognitive science, and AI principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response using clear headings for each section. Your entire response should be between 1000-1250 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of specific quantum computing principles (e.g., superposition, entanglement) and their application to cognitive modeling.",
            f"The proposed AI system clearly addresses the simulation or enhancement of {t['function']} using concrete examples and use cases.",
            "The quantum-cognitive model is innovative, well-explained, and scientifically plausible, with a detailed text-based visualization provided.",
            "The response effectively discusses specific quantum algorithms and their advantages over classical approaches for cognitive modeling.",
            "The cognitive enhancement potential is thoroughly explored with specific measurement methods and impact examples.",
            "At least three ethical implications are considered using a specific ethical framework, with detailed guidelines proposed.",
            "The experimental design is comprehensive, addressing methodology, confounding factors, and expected results.",
            "The response is creative while maintaining scientific accuracy and plausibility, using appropriate technical terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
