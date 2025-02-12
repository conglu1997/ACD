import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_principles = [
            "Utilitarianism",
            "Deontology",
            "Virtue Ethics",
            "Care Ethics"
        ]
        
        quantum_properties = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Coherence"
        ]
        
        neural_mechanisms = [
            "Synaptic Plasticity",
            "Neural Oscillations",
            "Predictive Coding",
            "Neuroplasticity"
        ]
        
        ethical_dilemmas = [
            "Trolley Problem",
            "Lying to Protect Someone",
            "Resource Allocation in Healthcare",
            "AI Decision-Making in Autonomous Vehicles"
        ]
        
        return {
            "1": {
                "ethical_principle": random.choice(ethical_principles),
                "quantum_property": random.choice(quantum_properties),
                "neural_mechanism": random.choice(neural_mechanisms),
                "ethical_dilemma": random.choice(ethical_dilemmas)
            },
            "2": {
                "ethical_principle": random.choice(ethical_principles),
                "quantum_property": random.choice(quantum_properties),
                "neural_mechanism": random.choice(neural_mechanisms),
                "ethical_dilemma": random.choice(ethical_dilemmas)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical quantum-neural interface system for ethical decision-making, incorporating {t['ethical_principle']} as the primary ethical framework, {t['quantum_property']} as the key quantum computing property, and {t['neural_mechanism']} as the central neural mechanism. Then, use your system to analyze and propose a solution for the ethical dilemma of {t['ethical_dilemma']}. Your response should include:\n\n" \
               f"1. System Architecture (300-350 words):\n" \
               f"   a) Describe the main components of your quantum-neural interface system.\n" \
               f"   b) Explain how {t['quantum_property']} is integrated into the system's decision-making process.\n" \
               f"   c) Detail how {t['neural_mechanism']} is modeled and utilized in your system.\n" \
               f"   d) Discuss how {t['ethical_principle']} is encoded and applied in the decision-making process.\n" \
               f"   e) Include a diagram of your system architecture using ASCII art or Unicode characters (max 20 lines).\n\n" \
               f"2. Quantum-Neural Computation (250-300 words):\n" \
               f"   a) Explain the theoretical basis for combining quantum computing with neural processing in ethical decision-making.\n" \
               f"   b) Describe how ethical principles are represented in your quantum-neural system.\n" \
               f"   c) Provide a step-by-step example of how a simple ethical decision would be processed by your system.\n\n" \
               f"3. Ethical Dilemma Analysis (250-300 words):\n" \
               f"   a) Briefly describe the ethical dilemma of {t['ethical_dilemma']}.\n" \
               f"   b) Explain how your system would approach analyzing this dilemma.\n" \
               f"   c) Discuss any challenges or limitations your system might face in addressing this particular dilemma.\n\n" \
               f"4. Proposed Solution (200-250 words):\n" \
               f"   a) Present the solution or decision proposed by your quantum-neural interface system for the given ethical dilemma.\n" \
               f"   b) Explain the reasoning behind this solution, referencing the system's architecture and computational process.\n" \
               f"   c) Discuss how this solution aligns with or deviates from traditional approaches to the dilemma.\n\n" \
               f"5. Implications and Limitations (200-250 words):\n" \
               f"   a) Discuss the potential implications of using such a system for ethical decision-making in real-world scenarios.\n" \
               f"   b) Analyze the limitations and potential risks of your approach.\n" \
               f"   c) Propose future research directions to address these limitations or expand the system's capabilities.\n\n" \
               f"Ensure your response demonstrates a deep understanding of quantum computing principles, neuroscience, and ethical philosophy. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section. Your total response should be between 1200-1450 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing, neuroscience, and ethical philosophy.",
            "The proposed quantum-neural interface system is innovative and coherently integrates the specified quantum property, neural mechanism, and ethical principle.",
            "The system architecture is well-explained and includes a clear diagram.",
            "The quantum-neural computation process is logically described and applied to ethical decision-making.",
            "The analysis of the given ethical dilemma is thorough and uses the proposed system effectively.",
            "The proposed solution is well-reasoned and clearly derived from the system's architecture and computational process.",
            "The response addresses implications, limitations, and future research directions for the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
