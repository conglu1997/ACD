import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_mechanism": "quantum coherence",
                "plant_type": "C3 plants (e.g., rice, wheat)",
                "environmental_challenge": "increasing global temperatures"
            },
            {
                "quantum_mechanism": "quantum entanglement",
                "plant_type": "C4 plants (e.g., corn, sugarcane)",
                "environmental_challenge": "water scarcity"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical framework for quantum-enhanced photosynthesis using {t['quantum_mechanism']} in {t['plant_type']}, and analyze its potential impact on global food security in the context of {t['environmental_challenge']}. Your response should include:\n\n1. Quantum Mechanism Design (250-300 words):\n   a) Explain the chosen quantum mechanism and its potential role in photosynthesis.\n   b) Describe how this mechanism could enhance the efficiency of photosynthesis.\n   c) Propose a theoretical model for integrating this quantum mechanism into the photosynthetic process.\n\n2. Biological Implementation (200-250 words):\n   a) Describe how the quantum-enhanced process would be implemented in the specified plant type.\n   b) Discuss any necessary genetic or structural modifications to the plant.\n   c) Address potential challenges in implementing this enhancement in living organisms.\n\n3. Efficiency Analysis (200-250 words):\n   a) Estimate the potential increase in photosynthetic efficiency.\n   b) Discuss how this increased efficiency might affect plant growth and crop yield.\n   c) Compare the theoretical efficiency of your quantum-enhanced process to traditional photosynthesis.\n\n4. Environmental Adaptation (200-250 words):\n   a) Explain how your quantum-enhanced photosynthesis could help plants adapt to the specified environmental challenge.\n   b) Discuss any potential drawbacks or unintended consequences of this enhancement in the given environmental context.\n\n5. Global Food Security Impact (200-250 words):\n   a) Analyze the potential impact of your quantum-enhanced photosynthesis on global food production.\n   b) Discuss how this technology could affect food distribution and accessibility.\n   c) Address any potential socioeconomic implications of this technology.\n\n6. Ethical Considerations (150-200 words):\n   a) Discuss the ethical implications of developing and implementing quantum-enhanced photosynthesis.\n   b) Address concerns related to biodiversity, ecosystem balance, and genetic modification.\n   c) Propose guidelines for the responsible development and use of this technology.\n\n7. Conclusion (100-150 words):\n   Summarize the key findings and implications of your proposed quantum-enhanced photosynthesis framework, highlighting its potential impact on global food security and areas for future research.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, plant biology, and global food systems. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nCite relevant scientific literature to support your claims and proposals throughout your response.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics and its potential applications in biology.",
            "The proposed quantum-enhanced photosynthesis model is innovative, scientifically plausible, and well-explained.",
            "The biological implementation is thoughtfully considered, addressing potential challenges and necessary modifications.",
            "The efficiency analysis provides reasonable estimates and comparisons based on scientific principles.",
            "The environmental adaptation section effectively addresses the specified challenge and considers potential consequences.",
            "The global food security impact analysis is comprehensive, considering production, distribution, and socioeconomic factors.",
            "Ethical considerations are thoroughly discussed, with responsible guidelines proposed.",
            "The response effectively integrates knowledge from quantum physics, biology, environmental science, and ethics.",
            "Relevant scientific literature is cited to support claims and proposals.",
            "The conclusion effectively summarizes key findings and implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
