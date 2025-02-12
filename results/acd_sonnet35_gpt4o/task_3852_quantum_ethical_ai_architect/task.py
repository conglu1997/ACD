import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "interference",
            "contextuality"
        ]
        ethical_dilemmas = [
            "trolley problem",
            "organ transplant dilemma",
            "AI rights and personhood",
            "privacy vs security trade-offs"
        ]
        cognitive_processes = [
            "moral reasoning",
            "ethical decision-making",
            "value judgment",
            "empathy simulation"
        ]
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "ethical_dilemma": random.choice(ethical_dilemmas),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "ethical_dilemma": random.choice(ethical_dilemmas),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired cognitive architecture for an AI system that models human moral reasoning and decision-making processes. Your architecture should incorporate the quantum principle of {t['quantum_principle']}, focus on the cognitive process of {t['cognitive_process']}, and be capable of addressing ethical dilemmas such as the {t['ethical_dilemma']}. Your response should include:\n\n1. Quantum-Inspired Cognitive Architecture (300-350 words):\n   a) Describe the key components of your cognitive architecture.\n   b) Explain how it incorporates the specified quantum principle into its design.\n   c) Detail how this architecture models the given cognitive process.\n   d) Provide a high-level schematic or description of the architecture's structure.\n\n2. Quantum-Classical Integration (200-250 words):\n   a) Discuss how your architecture bridges quantum and classical computing paradigms in the context of moral reasoning.\n   b) Explain any novel computational properties that emerge from this integration.\n   c) Address potential challenges in implementing this hybrid architecture and propose solutions.\n\n3. Ethical Decision-Making Simulation (250-300 words):\n   a) Describe how your architecture would approach the specified ethical dilemma.\n   b) Explain how quantum principles influence the decision-making process in this scenario.\n   c) Compare your quantum-inspired approach to traditional AI methods for ethical reasoning.\n\n4. Neuroscientific Plausibility (200-250 words):\n   a) Discuss how your architecture aligns with current understanding of human moral reasoning in neuroscience.\n   b) Identify any novel predictions or hypotheses about human cognition that arise from your model.\n   c) Propose an experiment to test the neuroscientific plausibility of your architecture.\n\n5. Ethical Implications (150-200 words):\n   a) Discuss potential ethical concerns arising from the development and use of quantum-inspired AI for moral reasoning.\n   b) Consider the implications of your system for concepts of machine consciousness and AI rights.\n   c) Propose guidelines for the responsible development and use of such systems.\n\n6. Future Developments and Applications (150-200 words):\n   a) Suggest potential expansions or modifications to your architecture to address other cognitive processes or ethical issues.\n   b) Discuss how advancements in quantum computing or neurotechnology might enhance your system in the future.\n   c) Propose a novel research question that arises from the intersection of quantum cognition, AI ethics, and neuroscience.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, cognitive science, neuroscience, and AI ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1550 words.\n\nInclude a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, cognitive science, neuroscience, and AI ethics.",
            f"The cognitive architecture effectively incorporates the quantum principle of {t['quantum_principle']}.",
            f"The system design is innovative and well-suited for modeling {t['cognitive_process']} and addressing ethical dilemmas like the {t['ethical_dilemma']}.",
            "The response addresses all required sections comprehensively and coherently.",
            "The proposed architecture effectively bridges quantum and classical paradigms in the context of moral reasoning.",
            "The ethical implications of the system are thoughtfully analyzed.",
            "The response is well-structured, clear, and within the specified word count.",
            "The response follows the specified format with numbered sections.",
            "The proposed future developments and applications are innovative and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
