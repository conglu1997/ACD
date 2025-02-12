import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        protein_types = [
            "Globular protein",
            "Membrane protein",
            "Fibrous protein",
            "Intrinsically disordered protein"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum annealing",
            "Quantum walks"
        ]
        ml_techniques = [
            "Deep neural networks",
            "Reinforcement learning",
            "Generative adversarial networks",
            "Variational autoencoders"
        ]
        return {
            "1": {
                "protein_type": random.choice(protein_types),
                "quantum_concept": random.choice(quantum_concepts),
                "ml_technique": random.choice(ml_techniques)
            },
            "2": {
                "protein_type": random.choice(protein_types),
                "quantum_concept": random.choice(quantum_concepts),
                "ml_technique": random.choice(ml_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze a quantum-inspired algorithm for predicting the folding of a {t['protein_type']}, incorporating the quantum concept of {t['quantum_concept']} and the machine learning technique of {t['ml_technique']}. Your response should include:\n\n1. Theoretical Framework (250-300 words):\n   a) Explain the key challenges in predicting the folding of the specified protein type.\n   b) Describe how the given quantum concept can be applied to protein folding prediction.\n   c) Discuss the potential advantages of using a quantum-inspired approach for this problem.\n\n2. Algorithm Design (300-350 words):\n   a) Outline your quantum-inspired algorithm for protein folding prediction.\n   b) Explain how it incorporates the specified quantum concept and machine learning technique.\n   c) Describe the key components and their roles in the folding prediction process.\n   d) Include at least one equation or formal representation of a critical component in your algorithm.\n\n3. Implementation Strategy (200-250 words):\n   a) Discuss how your algorithm would be implemented on classical hardware.\n   b) Explain any data preprocessing or encoding required for your approach.\n   c) Address potential scalability issues and how they might be overcome.\n\n4. Performance Analysis (200-250 words):\n   a) Propose methods to evaluate the performance of your quantum-inspired algorithm.\n   b) Discuss how you would compare its performance to classical protein folding prediction methods.\n   c) Analyze potential limitations or challenges in your approach.\n\n5. Biological Implications (150-200 words):\n   a) Discuss how your algorithm might contribute to our understanding of protein folding mechanisms.\n   b) Explore potential applications in drug discovery or personalized medicine.\n   c) Speculate on how improved protein folding prediction might impact future biotechnology.\n\n6. Quantum Computing Perspective (150-200 words):\n   a) Analyze how your quantum-inspired algorithm could be adapted for future quantum hardware.\n   b) Discuss potential advantages and challenges of running your algorithm on a quantum computer.\n   c) Speculate on the future of quantum computing in computational biology.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, protein biology, and machine learning techniques. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary. Your total response should be between 1250-1550 words.\n\nFormat your response with clear headings for each section and use subheadings where appropriate."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing principles, protein biology, and machine learning techniques.",
            "The proposed quantum-inspired algorithm effectively integrates the specified quantum concept and machine learning technique for protein folding prediction.",
            "The implementation strategy and performance analysis are well-thought-out and address potential challenges.",
            "The discussion of biological implications and future quantum computing applications is insightful and scientifically plausible.",
            "The response is well-structured, adhering to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
