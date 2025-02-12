import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        cognitive_abilities = [
            "memory formation",
            "decision making",
            "pattern recognition"
        ]
        complex_problems = [
            "climate change mitigation",
            "pandemic prediction and response",
            "sustainable energy distribution"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "cognitive_ability": random.choice(cognitive_abilities),
                "complex_problem": random.choice(complex_problems)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "cognitive_ability": random.choice(cognitive_abilities),
                "complex_problem": random.choice(complex_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system inspired by {t['quantum_effect']} in biological systems, then apply it to enhance human {t['cognitive_ability']} and solve the complex problem of {t['complex_problem']}. Your response should include:\n\n" + \
               "1. Quantum Bio-AI System Design (300-350 words):\n" + \
               "   a) Describe the key components of your AI system and how they mimic or utilize {t['quantum_effect']}.\n" + \
               "   b) Explain how your system interfaces with human cognition to enhance {t['cognitive_ability']}.\n" + \
               "   c) Provide a high-level diagram or pseudocode illustrating a key process in your system.\n" + \
               "   d) Include at least one specific, novel algorithm or technique in your design.\n\n" + \
               "2. Quantum-Biological Mechanism (250-300 words):\n" + \
               "   a) Explain the current scientific understanding of {t['quantum_effect']} in biological systems.\n" + \
               "   b) Describe how your AI system replicates or leverages this quantum effect.\n" + \
               "   c) Discuss any challenges in implementing this quantum-biological mechanism in an AI system.\n" + \
               "   d) Provide a specific example of how this mechanism operates in your system.\n\n" + \
               "3. Cognitive Enhancement Analysis (200-250 words):\n" + \
               "   a) Analyze how your system enhances human {t['cognitive_ability']}.\n" + \
               "   b) Discuss potential limitations or side effects of this cognitive enhancement.\n" + \
               "   c) Compare your approach to non-quantum methods of cognitive enhancement.\n" + \
               "   d) Provide a hypothetical case study demonstrating the enhancement in action.\n\n" + \
               "4. Complex Problem Application (250-300 words):\n" + \
               "   a) Explain how your Quantum Bio-AI system, combined with enhanced human cognition, addresses {t['complex_problem']}.\n" + \
               "   b) Provide a specific scenario demonstrating the system's problem-solving capabilities.\n" + \
               "   c) Discuss potential challenges and limitations in applying your system to this problem.\n" + \
               "   d) Propose a method to measure the effectiveness of your solution.\n\n" + \
               "5. Ethical Considerations and Future Directions (200-250 words):\n" + \
               "   a) Discuss ethical implications of using quantum-inspired AI for cognitive enhancement.\n" + \
               "   b) Address potential societal impacts of applying such technology to solve complex global problems.\n" + \
               "   c) Propose two potential future research directions in quantum biocognitive AI.\n" + \
               "   d) Suggest guidelines for responsible development and use of this technology.\n\n" + \
               "Ensure your response demonstrates a deep understanding of quantum physics, biology, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\n" + \
               "Format your response with clear headings for each section. Adhere strictly to the word limits for each section. Your total response should be between 1200-1450 words. Provide specific examples, novel ideas, and detailed explanations throughout your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate word counts.",
            "The Quantum Bio-AI system design is well-explained, clearly incorporates the specified quantum effect, and includes a novel algorithm or technique.",
            "The quantum-biological mechanism is accurately described, plausibly implemented in the AI system, and illustrated with a specific example.",
            "The cognitive enhancement analysis is thorough, considers both benefits and limitations, and includes a hypothetical case study.",
            "The application to the complex problem is well-reasoned, demonstrates innovative problem-solving, and includes a proposed method for measuring effectiveness.",
            "Ethical considerations are thoughtfully addressed, future research directions are insightful, and guidelines for responsible development are proposed.",
            "The overall response demonstrates a deep understanding of quantum physics, biology, neuroscience, and AI, with specific examples and novel ideas throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
