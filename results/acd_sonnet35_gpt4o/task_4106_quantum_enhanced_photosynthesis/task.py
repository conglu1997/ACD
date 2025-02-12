import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = ['quantum coherence', 'quantum entanglement', 'quantum tunneling']
        plant_types = ['algae', 'higher plants', 'artificial leaf']
        applications = ['biofuel production', 'atmospheric carbon capture', 'food production']
        
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "plant_type": random.choice(plant_types),
                "application": random.choice(applications)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "plant_type": random.choice(plant_types),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-enhanced photosynthesis system leveraging {t['quantum_effect']} in {t['plant_type']}, aimed at improving {t['application']}. Then, analyze its potential implications for energy production and biological systems. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components and functioning of your quantum-enhanced photosynthesis system.
   b) Explain how it leverages {t['quantum_effect']} to enhance photosynthetic efficiency.
   c) Discuss the theoretical basis for how quantum effects could influence photosynthetic processes in {t['plant_type']}.
   d) Address potential challenges in implementing quantum effects in biological systems and propose solutions.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how your system integrates quantum phenomena with biological processes.
   b) Describe the mechanisms by which quantum effects enhance energy transfer or carbon fixation.
   c) Discuss how your system maintains quantum effects in a warm, wet biological environment.
   d) Propose a method for measuring and verifying quantum effects in your biological system.

3. Energy Production Analysis (200-250 words):
   a) Quantitatively estimate the potential increase in photosynthetic efficiency achieved by your system.
   b) Analyze how this increased efficiency could impact {t['application']}.
   c) Compare the energy production potential of your system to current technologies in the field.
   d) Discuss any potential limitations or trade-offs in your approach.

4. Biological and Ecological Implications (200-250 words):
   a) Explore how your quantum-enhanced system might affect the biology of {t['plant_type']}.
   b) Discuss potential impacts on ecosystem dynamics if your system were widely implemented.
   c) Consider possible evolutionary implications of introducing quantum-enhanced photosynthesis.
   d) Address any potential risks or unintended consequences of your system.

5. Experimental Proposal (150-200 words):
   a) Design a hypothetical experiment to test a key aspect of your quantum-enhanced photosynthesis system.
   b) Describe the experimental setup, including any novel equipment or techniques required.
   c) Explain how you would analyze the results and what outcomes would support or refute your approach.

6. Future Research Directions (150-200 words):
   a) Suggest 2-3 follow-up research questions or experiments based on your proposal.
   b) Discuss how advances in this field might influence other areas of science and technology.
   c) Speculate on potential long-term implications for energy production, agriculture, and our understanding of quantum biology.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and their potential intersections. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} and how it can be applied to enhance photosynthesis in {t['plant_type']}.",
            f"The proposed system presents a plausible mechanism for integrating quantum effects with biological processes in {t['plant_type']}.",
            f"The energy production analysis provides a quantitative estimate of efficiency increase and thoroughly discusses its impact on {t['application']}.",
            "The response addresses biological and ecological implications comprehensively, including potential risks and evolutionary consequences.",
            "The experimental proposal is well-designed and appropriate for testing the key aspects of the quantum-enhanced photosynthesis system.",
            "The future research directions are insightful and demonstrate an understanding of the field's potential impact on science and technology.",
            "The response is creative and speculative while maintaining scientific plausibility and rigor throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
