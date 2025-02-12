import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "ecological_challenge": "Ocean acidification",
                "quantum_principle": "Quantum sensing",
                "biological_component": "Engineered algae",
                "ai_application": "Predictive modeling"
            },
            {
                "ecological_challenge": "Microplastic pollution",
                "quantum_principle": "Quantum entanglement",
                "biological_component": "Synthetic bacteria",
                "ai_application": "Swarm intelligence"
            }
        ]
        return {str(i+1): random.choice(challenges) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-biological hybrid system integrated with AI for environmental monitoring and remediation, addressing the ecological challenge of {t['ecological_challenge']}. Your system should incorporate the quantum principle of {t['quantum_principle']}, utilize {t['biological_component']} as a biological component, and implement AI for {t['ai_application']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-biological-AI hybrid system.
   b) Explain how quantum principles are integrated with biological elements and AI.
   c) Discuss how your system specifically addresses the given ecological challenge.
   d) Include a high-level diagram or flowchart of your system architecture (describe it textually).

2. Quantum-Biological Interface (250-300 words):
   a) Explain how the specified quantum principle is utilized in your system.
   b) Describe how the biological component is engineered or adapted for this application.
   c) Discuss the mechanisms of interaction between the quantum and biological elements.

3. AI Integration and Function (200-250 words):
   a) Describe the AI architecture and its role in your system.
   b) Explain how the AI processes data from the quantum-biological components.
   c) Discuss any novel algorithms or approaches necessary for this integration.

4. Environmental Monitoring and Remediation (250-300 words):
   a) Detail how your system monitors the specified ecological challenge.
   b) Explain the remediation strategies employed by your system.
   c) Provide a hypothetical scenario demonstrating your system in action.

5. Challenges and Limitations (150-200 words):
   a) Identify potential technical challenges in implementing your system.
   b) Discuss any limitations in its effectiveness or applicability.
   c) Propose potential solutions or areas for future research.

6. Ethical and Ecological Implications (200-250 words):
   a) Analyze the potential ecological impact of deploying your system.
   b) Discuss ethical considerations related to using engineered biological components in the environment.
   c) Propose guidelines for responsible development and use of such technology.

Ensure your response demonstrates a deep understanding of quantum computing, synthetic biology, artificial intelligence, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific ecological challenge of {t['ecological_challenge']}.",
            f"The system design must incorporate the quantum principle of {t['quantum_principle']}.",
            f"The biological component {t['biological_component']} must be effectively utilized in the system.",
            f"The AI application for {t['ai_application']} must be clearly explained and integrated into the system.",
            "The response should demonstrate a deep understanding of quantum computing, synthetic biology, artificial intelligence, and environmental science.",
            "The proposed system should be innovative while maintaining scientific plausibility.",
            "The response should address all required sections with appropriate depth and clarity.",
            "The total response should be between 1350-1650 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
