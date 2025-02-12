import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cell_types = [
            {
                "type": "Neurons",
                "feature": "Synaptic plasticity",
                "quantum_aspect": "Quantum tunneling in ion channels"
            },
            {
                "type": "Stem cells",
                "feature": "Pluripotency",
                "quantum_aspect": "Quantum coherence in DNA"
            },
            {
                "type": "Bacteria",
                "feature": "Quorum sensing",
                "quantum_aspect": "Quantum entanglement in cellular communication"
            },
            {
                "type": "Plant cells",
                "feature": "Photosynthesis",
                "quantum_aspect": "Quantum coherence in energy transfer"
            }
        ]
        return {str(i+1): cell for i, cell in enumerate(random.sample(cell_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical quantum-biological computing system that integrates {t['type']} with quantum processors, focusing on the cellular feature of {t['feature']} and the quantum aspect of {t['quantum_aspect']}. Then, analyze its potential applications and ethical implications. Your response should include the following sections:\n\n1. System Architecture (300-350 words):\n   a) Describe the overall structure of your quantum-biological computing system.\n   b) Explain how it integrates living {t['type']} with quantum processors.\n   c) Detail how the system leverages {t['feature']} and {t['quantum_aspect']}.\n   d) Discuss any novel interfaces or technologies required for this integration.\n\n2. Computational Paradigm (250-300 words):\n   a) Explain the computational model of your system.\n   b) Describe how information is processed and stored using both biological and quantum components.\n   c) Discuss how {t['feature']} contributes to the system's computational capabilities.\n   d) Explain how {t['quantum_aspect']} enhances or enables new computational processes.\n\n3. Potential Applications (200-250 words):\n   a) Propose three potential applications of your quantum-biological computing system.\n   b) Explain how each application leverages the unique features of your system.\n   c) Discuss the potential advantages over current classical or quantum computing systems.\n\n4. Technical Challenges (200-250 words):\n   a) Identify key technical challenges in implementing your system.\n   b) Propose potential solutions or research directions to address these challenges.\n   c) Discuss any limitations of your system and how they might be overcome.\n\n5. Ethical Implications (250-300 words):\n   a) Analyze potential ethical issues arising from the integration of living cells with quantum computing.\n   b) Discuss the implications for concepts of consciousness, free will, and the definition of life.\n   c) Explore potential misuses of this technology and propose safeguards.\n   d) Discuss the broader societal impacts of such a system, including issues of access and inequality.\n\n6. Future Directions (150-200 words):\n   a) Propose two potential extensions or improvements to your system.\n   b) Speculate on how this technology might evolve over the next 50 years.\n   c) Discuss how advances in this field might impact our understanding of biology, computation, and consciousness.\n\nEnsure your response demonstrates a deep understanding of quantum computing, biology, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nYour total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture effectively integrates {t['type']} with quantum processors, leveraging {t['feature']} and {t['quantum_aspect']}.",
            "The computational paradigm clearly explains how biological and quantum components process and store information.",
            "The proposed applications are innovative and leverage the unique features of the quantum-biological system.",
            "Technical challenges are identified and addressed with plausible solutions or research directions.",
            "The ethical implications analysis is thorough and considers multiple perspectives.",
            "The response demonstrates a deep understanding of quantum computing, biology, and ethics.",
            "The proposed future directions are insightful and scientifically plausible.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
