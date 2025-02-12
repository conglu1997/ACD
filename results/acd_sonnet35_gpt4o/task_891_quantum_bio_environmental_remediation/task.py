import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            "Heavy metal contamination in soil",
            "Microplastics in marine ecosystems",
            "Atmospheric carbon dioxide levels",
            "Pharmaceutical pollutants in water systems"
        ]
        quantum_principles = [
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum entanglement",
            "Superposition"
        ]
        biological_systems = [
            "Photosynthetic complexes",
            "Enzyme catalysis",
            "Magnetoreception in birds",
            "DNA repair mechanisms"
        ]
        
        tasks = {}
        for i in range(1, 3):
            issue = random.choice(environmental_issues)
            principle = random.choice(quantum_principles)
            system = random.choice(biological_systems)
            tasks[str(i)] = {"issue": issue, "principle": principle, "system": system}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired biological system for environmental remediation addressing the issue of {t['issue']}. Your system should be inspired by {t['system']} and incorporate the quantum principle of {t['principle']}. Provide your response in the following format:\n\n1. Theoretical Framework (200-250 words):\n   a) Explain the quantum principle and its relevance to the chosen biological system.\n   b) Describe how this principle could be harnessed for environmental remediation.\n   c) Discuss the potential advantages of a quantum-inspired approach over classical methods.\n\n2. System Design (250-300 words):\n   a) Propose a detailed design for your quantum-inspired biological system.\n   b) Explain how it incorporates the specified quantum principle and biological inspiration.\n   c) Describe the key components and mechanisms of your system.\n   d) Include at least one equation or formal representation of a critical process in your system.\n\n3. Environmental Application (200-250 words):\n   a) Explain how your system would address the given environmental issue.\n   b) Discuss the potential efficiency and effectiveness of your approach.\n   c) Identify any limitations or challenges in implementing your system.\n\n4. Experimental Validation (150-200 words):\n   a) Propose an experimental setup to test the effectiveness of your system.\n   b) Describe key measurements or observations that would validate your approach.\n   c) Discuss potential control experiments.\n\n5. Ethical and Societal Implications (150-200 words):\n   a) Analyze potential risks or unintended consequences of your system.\n   b) Discuss ethical considerations in deploying such a system in the environment.\n   c) Propose guidelines for responsible development and use of quantum-inspired biological remediation systems.\n\nEnsure your response demonstrates a deep understanding of quantum biology, environmental science, and engineering principles. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum principle and biological system",
            "The proposed system design is creative, detailed, and scientifically plausible",
            "The environmental application is well-explained and addresses the given issue effectively",
            "The experimental validation proposal is logical and comprehensive",
            "Ethical and societal implications are thoroughly considered",
            "The response shows strong interdisciplinary integration of quantum biology, environmental science, and engineering"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0