import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_challenges = [
            'carbon capture and storage',
            'renewable energy optimization',
            'climate modeling and prediction',
            'ecosystem restoration'
        ]
        quantum_principles = [
            'superposition',
            'entanglement',
            'quantum tunneling'
        ]
        bio_components = [
            'engineered photosynthesis',
            'synthetic carbon fixation pathways',
            'biomolecular computers'
        ]
        ai_techniques = [
            'reinforcement learning',
            'generative adversarial networks',
            'federated learning'
        ]
        
        return {
            "1": {
                "climate_challenge": random.choice(climate_challenges),
                "quantum_principle": random.choice(quantum_principles),
                "bio_component": random.choice(bio_components),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "climate_challenge": random.choice(climate_challenges),
                "quantum_principle": random.choice(quantum_principles),
                "bio_component": random.choice(bio_components),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical system that integrates quantum computing, synthetic biology, and artificial intelligence to address the climate change challenge of {t['climate_challenge']}. Your system should incorporate the quantum principle of {t['quantum_principle']}, utilize {t['bio_component']} as a key biological component, and employ {t['ai_technique']} as its primary AI technique. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your integrated quantum-bio-AI system.
   b) Explain how your system incorporates the specified quantum principle, biological component, and AI technique.
   c) Detail how these components work together to address the given climate challenge.
   d) Provide a diagram or detailed description of your system's structure.

2. Quantum-Biological Interface (250-300 words):
   a) Explain the mechanisms by which quantum effects are harnessed in the biological component.
   b) Describe how information is transferred between the quantum and biological systems.
   c) Address potential issues of decoherence and propose solutions.

3. AI Integration and Control (250-300 words):
   a) Describe how the AI system manages and optimizes the quantum and biological components.
   b) Explain how the AI technique is applied to improve the system's performance in addressing the climate challenge.
   c) Discuss any novel computational approaches required for this integration.

4. Climate Impact Analysis (200-250 words):
   a) Predict the potential impact of your system on the specified climate challenge.
   b) Compare its theoretical performance to current technologies or approaches.
   c) Discuss any potential secondary environmental effects or unintended consequences.

5. Experimental Design (300-350 words):
   a) Propose an experiment to test the effectiveness of your system in addressing the climate challenge.
   b) Describe the methodology, including any novel measurement techniques required.
   c) Predict potential outcomes and their implications.
   d) Discuss any ethical considerations or safety protocols for testing such a system.

6. Scalability and Implementation (200-250 words):
   a) Discuss the potential for scaling up your system for global implementation.
   b) Identify key technological, economic, or political barriers to widespread adoption.
   c) Propose strategies to overcome these barriers.

7. Interdisciplinary Implications (200-250 words):
   a) Discuss the potential impact of your system on the fields of quantum computing, synthetic biology, AI, and climate science.
   b) Propose two potential spin-off applications in other scientific or technological domains.
   c) Address any philosophical or societal implications of using such advanced integrated systems to address global challenges.

Ensure your response demonstrates a deep understanding of quantum mechanics, synthetic biology, artificial intelligence, and climate science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1700-2050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, synthetic biology, artificial intelligence, and climate science.",
            "The proposed system integrates quantum computing, synthetic biology, and AI in a novel and plausible way to address the specified climate challenge.",
            "The explanation of the quantum-biological interface and AI integration is scientifically sound and innovative.",
            "The experimental design and climate impact analysis are well-thought-out and demonstrate critical thinking.",
            "The response addresses scalability, implementation challenges, and interdisciplinary implications comprehensively.",
            "The writing is clear, well-structured, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
