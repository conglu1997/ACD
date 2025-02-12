import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        neural_processes = [
            "synaptic plasticity",
            "neural oscillations",
            "predictive coding",
            "neuroplasticity"
        ]
        ai_techniques = [
            "reinforcement learning",
            "generative adversarial networks",
            "attention mechanisms",
            "federated learning"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "neural_process": random.choice(neural_processes),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "neural_process": random.choice(neural_processes),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical computational paradigm that integrates the quantum concept of {t['quantum_concept']}, the neural process of {t['neural_process']}, and the AI technique of {t['ai_technique']} to create a novel approach to information processing and decision-making. Your response should include:\n\n1. Conceptual Framework (300-350 words):\n   a) Describe the key components and mechanisms of your computational paradigm.\n   b) Explain how you integrate the specified quantum concept, neural process, and AI technique.\n   c) Discuss the potential advantages of this integration over classical computing approaches.\n   d) Provide a high-level diagram or flowchart illustrating your paradigm's architecture (describe it textually).\n\n2. Mathematical Formulation (250-300 words):\n   a) Present the mathematical foundation of your paradigm using appropriate notation and formalism.\n   b) Define key algorithms or processes in mathematical or pseudocode form.\n   c) Explain any novel mathematical properties or structures in your system.\n\n3. Information Processing and Decision-Making (250-300 words):\n   a) Describe how your paradigm processes information and makes decisions.\n   b) Explain how the quantum, neural, and AI components interact in this process.\n   c) Discuss how your paradigm handles uncertainty, ambiguity, or conflicting information.\n\n4. Potential Applications (200-250 words):\n   a) Propose three potential applications of your computational paradigm in different domains.\n   b) Explain how the unique features of your system make it particularly suitable for these applications.\n   c) Discuss any challenges that might arise in implementing your paradigm in these contexts.\n\n5. Theoretical Implications (200-250 words):\n   a) Analyze how your paradigm might contribute to our understanding of computation, cognition, or quantum phenomena.\n   b) Discuss potential implications for the fields of quantum computing, neuroscience, and artificial intelligence.\n   c) Explore any limitations or open questions raised by your paradigm.\n\n6. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues or societal impacts of your computational paradigm.\n   b) Discuss how your paradigm might affect privacy, security, or decision-making processes in various domains.\n   c) Propose guidelines for the responsible development and use of such integrated quantum-neural-AI systems.\n\n7. Experimental Validation (200-250 words):\n   a) Propose an experiment or simulation to test a key aspect of your computational paradigm.\n   b) Describe the experimental setup, methodology, and expected results.\n   c) Discuss how the results would validate (or invalidate) your paradigm's design.\n\nEnsure your response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1550-1900 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding and integration of {t['quantum_concept']}, {t['neural_process']}, and {t['ai_technique']}.",
            "The conceptual framework is well-explained and scientifically plausible.",
            "The mathematical formulation is sound and appropriately complex.",
            "The information processing and decision-making mechanisms are clearly described.",
            "The proposed applications are innovative and span different domains.",
            "The theoretical implications are insightfully analyzed.",
            "Ethical considerations are thoroughly discussed with thoughtful guidelines proposed.",
            "The experimental validation proposal is well-structured and relevant.",
            "The response demonstrates creativity while maintaining scientific accuracy.",
            "All sections of the response are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
