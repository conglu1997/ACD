import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_biology_phenomena = [
            {
                "name": "Photosynthetic energy transfer",
                "description": "The process by which plants and some bacteria efficiently transfer energy from light-harvesting complexes to reaction centers"
            },
            {
                "name": "Avian magnetoreception",
                "description": "The ability of some birds to sense the Earth's magnetic field for navigation, potentially using quantum coherence in cryptochrome proteins"
            },
            {
                "name": "Enzyme catalysis",
                "description": "The role of quantum tunneling in enzyme-catalyzed reactions, particularly in hydrogen transfer processes"
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(random.sample(quantum_biology_phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates quantum effects in biological processes, focusing on {t['name']}. Then, apply this system to design novel experiments in the field of quantum biology. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI quantum biology simulator.
   b) Explain how your system integrates quantum mechanics principles with biological processes.
   c) Detail how the system models {t['name']}.
   d) Discuss any novel algorithms or approaches used in your simulation.
   e) Provide a simple diagram or pseudocode (10-15 lines) illustrating a key aspect of your system architecture.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how your system bridges the gap between quantum and classical descriptions of biological systems.
   b) Describe how it handles the transition from quantum to classical behavior in {t['name']}.
   c) Discuss how your system accounts for environmental noise and decoherence in biological contexts.

3. Simulation Process (250-300 words):
   a) Provide a step-by-step description of how your AI system simulates {t['name']}.
   b) Explain how it generates predictions about quantum effects in this biological process.
   c) Discuss any challenges or unique features of simulating this particular phenomenon.

4. Experimental Design (300-350 words):
   a) Propose a novel experiment to test predictions made by your AI system about {t['name']}.
   b) Describe the experimental setup, including any specialized equipment or techniques required.
   c) Explain how your experiment could distinguish between quantum and classical effects in the biological process.
   d) Discuss potential outcomes and their implications for our understanding of quantum biology.

5. Data Analysis and Interpretation (200-250 words):
   a) Describe how your AI system would analyze and interpret data from the proposed experiment.
   b) Explain how it would handle uncertainties and potential artifacts in experimental data.
   c) Discuss how your system could generate new hypotheses based on experimental results.

6. Ethical Implications and Future Directions (200-250 words):
   a) Discuss ethical considerations related to simulating and experimenting on quantum effects in biological systems.
   b) Address potential implications of your research for fields such as medicine, biotechnology, or quantum computing.
   c) Propose guidelines for responsible development and use of AI systems in quantum biology research.
   d) Suggest two future research directions that could build on your work.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and scientific methodology. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section, numbered 1-6 as outlined above. Your total response should be between 1500-1800 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an AI system that credibly simulates quantum effects in {t['name']}.",
            "The system architecture should integrate quantum mechanics principles with biological processes in a plausible manner.",
            "The proposed experiment should be novel and specifically designed to test predictions about the given quantum biology phenomenon.",
            "The response should demonstrate a high level of interdisciplinary knowledge in quantum mechanics, biology, and AI.",
            "The ethical implications and future directions should be thoughtfully addressed.",
            "The overall response should be creative and innovative while maintaining scientific plausibility and rigor.",
            "The response should include a simple diagram or pseudocode illustrating a key aspect of the system architecture.",
            "The total word count should be between 1500-1800 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
