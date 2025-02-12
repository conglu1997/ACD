import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_effect": "Quantum entanglement in radical pair mechanisms",
                "biological_system": "Cryptochrome proteins in magnetoreception",
                "disease": "Neurodegenerative disorders",
                "example_data": "Coherence lifetime in cryptochrome: 1 microsecond at physiological temperatures"
            },
            {
                "quantum_effect": "Quantum tunneling in proton transfer",
                "biological_system": "DNA mutation and repair mechanisms",
                "disease": "Cancer",
                "example_data": "Proton tunneling rate in DNA base pairs: 1 × 10^6 to 1 × 10^8 s^-1"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 45 minutes to complete this task. Design an AI system that simulates complex quantum effects in intricate biological systems and predicts their impact on medical treatments, then use it to propose a novel therapy for a complex disease with quantitative predictions. Focus on the quantum effect of {t['quantum_effect']} in the biological system of {t['biological_system']}, and apply your findings to develop a potential treatment for {t['disease']}. Use the following example data in your simulation: {t['example_data']}.

Your response should include the following sections:

1. Quantum-Biological AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating complex quantum effects in intricate biological systems.
   b) Explain how your system integrates advanced quantum physics principles with sophisticated biological processes.
   c) Detail how the AI handles the complexity and scale differences between quantum and biological phenomena.
   d) Include a high-level diagram or flowchart of your AI system architecture.

2. Quantum-Biological Simulation (250-300 words):
   a) Explain how your AI system simulates the specified quantum effect in the given biological system.
   b) Describe the methods used to predict the impact of quantum effects on cellular processes.
   c) Provide an example of a simulated quantum-biological interaction, using the provided example data and including quantitative predictions.

3. Medical Application Methodology (250-300 words):
   a) Outline how your AI system extrapolates from quantum-biological simulations to medical treatments.
   b) Explain how it accounts for the complexity of the specified disease in its predictions.
   c) Describe any novel algorithms or techniques used for translating quantum effects into potential therapies.

4. Proposed Novel Therapy (200-250 words):
   a) Present a detailed description of a novel therapy for the specified disease based on your AI's predictions.
   b) Explain how this therapy leverages the simulated quantum effects in biological systems.
   c) Provide quantitative predictions for the efficacy of your proposed therapy, including expected physiological changes and potential timeframes.
   d) Discuss potential advantages of this approach over conventional treatments.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues in applying complex quantum-biological principles to medical treatments.
   b) Discuss the limitations of your AI system and the reliability of its quantitative predictions.
   c) Propose comprehensive guidelines for the responsible development and testing of quantum-based medical therapies.

6. Future Implications and Research Directions (150-200 words):
   a) Explain how your AI system and its findings could impact multiple fields of medical research.
   b) Suggest two potential research projects that could stem from your work, including expected outcomes and challenges.
   c) Discuss how this approach might revolutionize our understanding of disease mechanisms and treatment strategies.

Ensure your response demonstrates a deep understanding of advanced quantum physics, complex biological systems, and cutting-edge medical science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and providing quantitative predictions where possible.

Format your response with clear headings for each section, numbered as above. Include the high-level diagram or flowchart of your AI system architecture as mentioned in section 1. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} and its potential role in {t['biological_system']}, including correct use and extension of the provided example data: {t['example_data']}.",
            f"The proposed therapy for {t['disease']} is innovative, scientifically plausible, and clearly leverages the simulated quantum effects, with quantitative predictions for its efficacy.",
            "The AI system architecture is well-designed, with a clear explanation of how it integrates advanced quantum and complex biological principles.",
            "The ethical considerations are thoroughly addressed, including comprehensive guidelines for responsible development and testing of quantum-based medical therapies.",
            "The response demonstrates exceptional creativity and interdisciplinary knowledge integration throughout, with clear connections made between advanced quantum physics, complex biological systems, and cutting-edge medical science.",
            "The response follows the required format, including all specified sections and word counts, and includes a high-level diagram or flowchart of the AI system architecture.",
            "The response provides quantitative predictions and demonstrates advanced quantitative reasoning throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
