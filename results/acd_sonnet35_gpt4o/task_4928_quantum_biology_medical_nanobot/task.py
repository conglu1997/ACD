import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        cellular_targets = [
            "mitochondria",
            "cell membrane",
            "DNA repair"
        ]
        medical_applications = [
            "cancer treatment",
            "neurodegenerative disease therapy",
            "anti-aging interventions"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "cellular_target": random.choice(cellular_targets),
                "medical_application": random.choice(medical_applications)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "cellular_target": random.choice(cellular_targets),
                "medical_application": random.choice(medical_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum biology-inspired medical nanobot system for targeted cellular repair, focusing on the quantum effect of {t['quantum_effect']}, the cellular target of {t['cellular_target']}, and its application in {t['medical_application']}. Then, analyze its potential applications and ethical implications. Your response should include:

1. Nanobot System Design (300-350 words):
   a) Describe the key components of your quantum biology-inspired nanobot system.
   b) Explain how your system utilizes {t['quantum_effect']} for cellular repair.
   c) Detail the mechanism by which the nanobots target and interact with {t['cellular_target']}.
   d) Discuss how your system navigates and operates within the human body.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how your system bridges quantum effects and biological processes.
   b) Describe the challenges in maintaining quantum effects at the biological scale and how your design addresses them.
   c) Discuss how your system accounts for the complex, dynamic nature of living systems.

3. Medical Application Analysis (250-300 words):
   a) Detail how your nanobot system could be applied to {t['medical_application']}.
   b) Explain the potential advantages of your quantum biology-inspired approach over conventional treatments.
   c) Discuss possible limitations or risks of your system in this medical context.

4. Broader Implications (200-250 words):
   a) Identify three potential applications of your system beyond the specified medical use.
   b) Discuss how widespread adoption of your system could affect medical practice and human health.
   c) Analyze potential challenges in scaling up production and deployment of your nanobot system.

5. Ethical Considerations (200-250 words):
   a) Identify three potential ethical concerns raised by your quantum biology-inspired nanobot system.
   b) Discuss the balance between potential medical benefits and risks to individual patients and society.
   c) Propose guidelines for the responsible development and use of your system.

6. Future Developments (150-200 words):
   a) Suggest two potential enhancements to your system that could increase its effectiveness or scope.
   b) Discuss how your system could contribute to our understanding of quantum effects in biological systems.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and medical science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']}, {t['cellular_target']}, and {t['medical_application']}.",
            "The nanobot system design is innovative and scientifically plausible.",
            "The quantum-biological interface is well-explained and addresses key challenges.",
            "The medical application analysis is thorough and considers both advantages and limitations.",
            "The ethical considerations are thoughtfully discussed with appropriate guidelines proposed.",
            "The response is well-structured, adheres to the word count, and uses technical terminology appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
