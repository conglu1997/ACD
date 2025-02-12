import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                "process": "value-based decision making",
                "quantum_concept": "superposition",
                "brain_region": "orbitofrontal cortex",
                "example_scenario": "choosing between job offers"
            },
            {
                "process": "risk assessment",
                "quantum_concept": "entanglement",
                "brain_region": "amygdala",
                "example_scenario": "evaluating investment options"
            }
        ]
        return {
            "1": random.choice(cognitive_processes),
            "2": random.choice(cognitive_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Design a quantum-inspired neural network architecture for modeling the human cognitive process of {t['process']}. "
            f"Your design should incorporate the quantum concept of {t['quantum_concept']} and focus on the neural activity in the {t['brain_region']}. "
            f"Consider the example scenario of {t['example_scenario']} when explaining your model. "
            "Your response should include:\n\n"
            "1. Architecture Overview (250-300 words):\n"
            "   a) Describe the key components of your quantum-inspired neural network.\n"
            "   b) Explain how these components interact to model the specified cognitive process.\n"
            "   c) Discuss how you incorporate the given quantum concept into your neural network design.\n"
            "   d) Include a high-level diagram or pseudocode representation of your architecture.\n\n"
            "2. Quantum-Neural Integration (200-250 words):\n"
            "   a) Detail how your architecture integrates quantum principles with traditional neural network concepts.\n"
            "   b) Explain how the specified quantum concept enhances the modeling of the cognitive process.\n"
            "   c) Discuss any novel quantum-inspired neurons or layers in your design.\n\n"
            "3. Cognitive Process Modeling (200-250 words):\n"
            "   a) Describe how your architecture models the specified cognitive process.\n"
            "   b) Explain how your design accounts for the neural activity in the given brain region.\n"
            "   c) Discuss how quantum effects might influence or explain aspects of this cognitive process.\n"
            "   d) Provide a specific example of how your architecture would process information in the given example scenario.\n\n"
            "4. Learning and Adaptation (150-200 words):\n"
            "   a) Explain how your quantum-inspired network learns and adapts.\n"
            "   b) Describe any quantum-inspired learning algorithms or optimization techniques.\n"
            "   c) Discuss how your approach differs from classical neural network training.\n\n"
            "5. Potential Applications and Implications (150-200 words):\n"
            "   a) Propose two potential applications of your quantum cognitive architecture.\n"
            "   b) Discuss the implications of your model for our understanding of human cognition.\n"
            "   c) Explain how your architecture might inform the development of more advanced AI systems.\n\n"
            "6. Limitations and Future Directions (150-200 words):\n"
            "   a) Identify potential limitations or challenges in implementing your architecture.\n"
            "   b) Suggest areas for future research or improvements in quantum cognitive modeling.\n"
            "   c) Discuss ethical considerations related to quantum-inspired cognitive AI systems.\n\n"
            "Ensure your response demonstrates a deep understanding of quantum computing principles, neural network architectures, and cognitive neuroscience. "
            "Use appropriate technical terminology and provide clear explanations for complex concepts. "
            "Be innovative in your approach while maintaining scientific plausibility.\n\n"
            "Format your response with clear headings for each section. Your total response should be between 1100-1400 words."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_concept']} and how it can be applied to neural networks in the context of {t['process']}.",
            f"The architecture effectively integrates quantum principles with neural network concepts to model {t['process']} in the {t['brain_region']}.",
            f"The design includes a specific example of how the architecture would process information in the {t['example_scenario']} scenario.",
            "The response includes innovative ideas for quantum-inspired neurons, layers, or learning algorithms.",
            "The potential applications and implications of the architecture are well-reasoned and plausible.",
            "The limitations and future directions discussed show a realistic understanding of the challenges in this field.",
            "The overall response demonstrates creativity and interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
