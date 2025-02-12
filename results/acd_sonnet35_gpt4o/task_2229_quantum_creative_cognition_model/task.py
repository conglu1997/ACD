import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        creativity_domains = [
            "Visual Arts",
            "Music Composition",
            "Scientific Discovery",
            "Literary Creation",
            "Technological Innovation"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Interference"
        ]
        cognitive_processes = [
            "Divergent Thinking",
            "Conceptual Combination",
            "Analogical Reasoning",
            "Insight Problem Solving",
            "Cognitive Flexibility"
        ]
        return {
            "1": {
                "creativity_domain": random.choice(creativity_domains),
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "creativity_domain": random.choice(creativity_domains),
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired neural network architecture that models and enhances human creative cognition in the domain of {t['creativity_domain']}, focusing on the cognitive process of {t['cognitive_process']} and incorporating the quantum principle of {t['quantum_principle']}. Your response should include the following sections:\n\n1. Conceptual Framework (250-300 words):\n   a) Explain the key principles of the specified quantum concept and how it relates to the chosen cognitive process.\n   b) Describe how the selected cognitive process contributes to creativity in the given domain.\n   c) Discuss potential parallels between quantum phenomena and creative cognition.\n\n2. Neural Network Architecture (300-350 words):\n   a) Propose a detailed architecture for your quantum-inspired neural network, including its main components and their interactions.\n   b) Explain how your architecture incorporates the specified quantum principle.\n   c) Describe how your model simulates or enhances the chosen cognitive process.\n   d) Include a diagram or pseudocode to illustrate your architecture's structure.\n\n3. Creative Process Simulation (250-300 words):\n   a) Explain how your model simulates the creative process in the specified domain.\n   b) Describe the role of the quantum principle in this simulation.\n   c) Discuss how your model accounts for both divergent and convergent thinking in the creative process.\n\n4. Enhancement Mechanisms (200-250 words):\n   a) Propose specific mechanisms by which your model could enhance human creativity.\n   b) Explain how these mechanisms leverage the quantum-inspired architecture.\n   c) Discuss potential limitations or challenges in implementing these enhancements.\n\n5. Evaluation and Validation (200-250 words):\n   a) Propose methods to evaluate the creativity and novelty of your model's outputs.\n   b) Suggest experiments to compare your model's performance with human creativity in the specified domain.\n   c) Discuss how you would validate that your model genuinely enhances creativity rather than simply replicating existing patterns.\n\n6. Ethical and Societal Implications (150-200 words):\n   a) Discuss potential ethical concerns or societal impacts of enhancing human creativity through quantum-inspired AI.\n   b) Analyze how your approach might influence our understanding of human cognition and creativity.\n   c) Propose guidelines for responsible development and use of creativity-enhancing AI systems.\n\n7. Future Research Directions (100-150 words):\n   a) Suggest two novel research directions that could emerge from your quantum-inspired approach to modeling creativity.\n   b) Briefly describe potential applications in other domains or industries.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, neural network architectures, and cognitive neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1450-1800 words.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all seven required sections with appropriate content for each, focusing on {t['creativity_domain']}, {t['cognitive_process']}, and {t['quantum_principle']}.",
            "The conceptual framework effectively integrates principles from quantum computing, neuroscience, and creativity research.",
            "The proposed neural network architecture is innovative, well-explained, and incorporates the specified quantum principle in a meaningful way.",
            "The creative process simulation and enhancement mechanisms are plausible and demonstrate a deep understanding of both the chosen cognitive process and the quantum principle.",
            "The evaluation and validation methods proposed are rigorous and appropriate for assessing creativity and novelty.",
            "Ethical implications and guidelines for responsible AI use in creativity enhancement are thoughtfully discussed.",
            "The response demonstrates creativity and plausibility in the proposed quantum-inspired approach to modeling and enhancing human creativity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
