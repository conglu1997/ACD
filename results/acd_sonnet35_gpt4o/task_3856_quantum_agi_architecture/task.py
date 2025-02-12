import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Quantum superposition",
            "Quantum entanglement",
            "Quantum tunneling",
            "Quantum annealing"
        ]
        cognitive_capabilities = [
            "Analogical reasoning",
            "Causal inference",
            "Concept formation",
            "Meta-learning"
        ]
        application_domains = [
            "Scientific discovery",
            "Complex system optimization",
            "Natural language understanding",
            "Ethical decision-making"
        ]
        
        tasks = {}
        for i in range(1, 3):
            principle = random.choice(quantum_principles)
            capability = random.choice(cognitive_capabilities)
            domain = random.choice(application_domains)
            tasks[str(i)] = {"principle": principle, "capability": capability, "domain": domain}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-enhanced artificial general intelligence (AGI) architecture that leverages the quantum principle of {t['principle']} to achieve advanced {t['capability']}. Then, analyze its potential application in the domain of {t['domain']}. Your response should include the following sections:\n\n1. Quantum AGI Architecture (300-350 words):\n   a) Describe the key components of your quantum-enhanced AGI system.\n   b) Explain how {t['principle']} is integrated into the AGI architecture.\n   c) Detail how this integration enhances the AGI's {t['capability']}.\n   d) Include a high-level diagram of your architecture (describe it textually).\n\n2. Quantum-Classical Interface (250-300 words):\n   a) Explain how your system translates between quantum and classical information.\n   b) Describe any novel quantum algorithms or approaches used in your design.\n   c) Discuss how quantum and classical processing are coordinated in your architecture.\n\n3. Cognitive Modeling (250-300 words):\n   a) Detail how your quantum AGI models and implements {t['capability']}.\n   b) Compare this approach to classical AGI methods for the same capability.\n   c) Discuss potential advantages and challenges of your quantum-enhanced approach.\n\n4. Application Analysis (200-250 words):\n   a) Analyze how your quantum AGI could be applied in the domain of {t['domain']}.\n   b) Describe a specific use case and explain how it would work in practice.\n   c) Discuss potential benefits and limitations of using quantum AGI in this domain.\n\n5. Ethical and Safety Considerations (200-250 words):\n   a) Identify potential ethical issues related to quantum-enhanced AGI.\n   b) Discuss safety concerns specific to your architecture and application.\n   c) Propose guidelines for responsible development and use of quantum AGI systems.\n\n6. Future Directions (150-200 words):\n   a) Suggest potential improvements or extensions to your quantum AGI architecture.\n   b) Propose a research agenda for advancing quantum-enhanced AGI systems.\n   c) Speculate on the long-term implications of successful quantum AGI development.\n\nEnsure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and artificial general intelligence concepts.",
            "The proposed architecture creatively integrates the specified quantum principle with AGI design.",
            "The explanation of how the quantum principle enhances the specified cognitive capability is clear and plausible.",
            "The application analysis for the given domain is thorough and insightful.",
            "Ethical and safety considerations are comprehensively addressed.",
            "The response shows originality and innovation while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0