import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "DNA replication",
            "Protein folding",
            "Enzyme catalysis",
            "Photosynthesis",
            "Neural signaling"
        ]
        quantum_phenomena = [
            "Superposition",
            "Entanglement",
            "Tunneling",
            "Coherence",
            "Quantum walks"
        ]
        return {
            "1": {
                "biological_process": random.choice(biological_processes),
                "quantum_phenomenon": random.choice(quantum_phenomena)
            },
            "2": {
                "biological_process": random.choice(biological_processes),
                "quantum_phenomenon": random.choice(quantum_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical model for quantum information processing in biological systems, focusing on the role of {t['quantum_phenomenon']} in {t['biological_process']}. Your response should include:\n\n1. Theoretical Framework (300-350 words):\n   a) Explain the key principles of {t['quantum_phenomenon']} and how it might manifest in biological systems.\n   b) Describe current theories on quantum effects in biology, particularly in relation to {t['biological_process']}.\n   c) Discuss the challenges in observing and measuring quantum effects at the biological scale.\n\n2. Model Architecture (350-400 words):\n   a) Outline the key components of your quantum bioinformation model.\n   b) Explain how your model incorporates {t['quantum_phenomenon']} into the biological process of {t['biological_process']}.\n   c) Describe the mathematical formalism you would use to represent quantum information in this biological context.\n   d) Provide a simple, original equation or diagram illustrating a core concept of your model.\n\n3. Information Processing Mechanism (250-300 words):\n   a) Describe how quantum information is encoded, processed, and transferred in your model.\n   b) Explain how this quantum mechanism might enhance or alter the classical understanding of {t['biological_process']}.\n   c) Discuss any potential quantum advantages or unique features of your proposed mechanism.\n\n4. Experimental Design (250-300 words):\n   a) Propose an experiment to test your model's predictions about quantum effects in {t['biological_process']}.\n   b) Describe the equipment and techniques that would be required to conduct this experiment.\n   c) Discuss potential challenges and how they might be overcome.\n\n5. Implications and Applications (200-250 words):\n   a) Discuss the potential implications of your model for our understanding of biology and quantum physics.\n   b) Suggest two potential applications of your model in fields such as medicine, biotechnology, or quantum computing.\n   c) Explore any ethical considerations related to manipulating quantum effects in biological systems.\n\n6. Limitations and Future Directions (150-200 words):\n   a) Identify potential limitations or criticisms of your model.\n   b) Suggest how these limitations might be addressed in future research.\n   c) Propose two potential extensions or refinements of your model.\n\nEnsure your response demonstrates a deep understanding of quantum physics, molecular biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1500-1800 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_phenomenon']} and its potential role in {t['biological_process']}.",
            "The proposed model is innovative yet scientifically plausible, integrating concepts from quantum physics, biology, and information theory.",
            "The response includes a clear explanation of how quantum information is processed in the biological context, with appropriate mathematical formalism.",
            "The experimental design is well-thought-out and addresses the challenges of observing quantum effects in biological systems.",
            "The response discusses potential implications and applications of the model, showing an understanding of its broader impact.",
            "The limitations and future directions are critically addressed, demonstrating scientific rigor.",
            "The response is well-structured, following the given format, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
