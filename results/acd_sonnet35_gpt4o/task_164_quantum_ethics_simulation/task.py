import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ethical_dilemma": "Trolley problem",
                "quantum_principle": "Superposition",
                "cognitive_aspect": "Decision-making under uncertainty"
            },
            {
                "ethical_dilemma": "Prisoner's dilemma",
                "quantum_principle": "Entanglement",
                "cognitive_aspect": "Theory of mind and strategic thinking"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing simulation of ethical decision-making processes based on the following scenario:\n\nEthical dilemma: {t['ethical_dilemma']}\nQuantum principle to incorporate: {t['quantum_principle']}\nCognitive aspect to model: {t['cognitive_aspect']}\n\nYour task is to:\n\n1. Conceptual Design (200-250 words):\n   Describe your quantum ethics simulation model, explaining how it integrates the given ethical dilemma, quantum principle, and cognitive aspect. Include:\n   a) The basic structure of your quantum circuit or algorithm\n   b) How ethical choices are represented in quantum states\n   c) How the cognitive aspect is modeled using quantum operations\n\n2. Quantum-Ethical Mapping (150-200 words):\n   Explain how specific elements of the ethical dilemma are mapped to quantum states or operations. Provide at least two concrete examples of this mapping.\n\n3. Simulation Process (150-200 words):\n   Describe the step-by-step process of running your simulation, including:\n   a) Initialization of quantum states\n   b) Application of quantum gates or operations\n   c) Measurement and interpretation of results\n\n4. Ethical Implications (200-250 words):\n   Analyze the potential implications of your quantum ethics simulation for:\n   a) Understanding human moral decision-making\n   b) Developing ethical AI systems\n   c) Philosophical debates about free will and determinism\n\n5. Limitations and Future Directions (100-150 words):\n   Discuss at least two limitations of your model and propose directions for future research or improvements.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, ethical philosophy, and cognitive science. Be creative in your approach while grounding your ideas in established theories and principles.\n\nOrganize your answer using clear headings for each section. Your total response should be between 800-1000 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear and accurate understanding of the given quantum principle and how it can be applied to model ethical decision-making.",
            "The conceptual design of the quantum ethics simulation is innovative, logically consistent, and effectively integrates the ethical dilemma, quantum principle, and cognitive aspect.",
            "The quantum-ethical mapping provides concrete and plausible examples of how ethical concepts are represented in quantum states or operations.",
            "The simulation process is described in a clear, step-by-step manner that shows a good understanding of quantum computing principles.",
            "The analysis of ethical implications is thoughtful and considers multiple perspectives, demonstrating an understanding of both quantum mechanics and moral philosophy.",
            "The limitations and future directions section shows critical thinking about the model's constraints and potential improvements.",
            "The overall response is well-organized, creative, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
