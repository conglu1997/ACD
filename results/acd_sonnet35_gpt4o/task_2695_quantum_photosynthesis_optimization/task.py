import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "system": "chlorophyll-based",
                "environment": "terrestrial",
                "coherence_time": 100,  # femtoseconds
                "energy_gap": 0.2  # eV
            },
            "2": {
                "system": "bacteriochlorophyll-based",
                "environment": "aquatic",
                "coherence_time": 300,  # femtoseconds
                "energy_gap": 0.1  # eV
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired artificial photosynthesis system that leverages quantum coherence effects observed in natural photosynthesis to optimize energy transfer efficiency. Your system should be based on a {t['system']} model and designed for a {t['environment']} environment. The observed quantum coherence time is {t['coherence_time']} femtoseconds, and the energy gap between excitonic states is {t['energy_gap']} eV. Include the following in your response:

1. Quantum Mechanism Description (250-300 words):
   a) Explain the quantum coherence effects observed in natural photosynthesis.
   b) Describe how these effects contribute to the efficiency of energy transfer.
   c) Discuss any challenges in replicating these quantum effects in artificial systems.
   d) Calculate the coherence length given the coherence time and explain its significance.

2. System Architecture (300-350 words):
   a) Outline the key components of your artificial photosynthesis system.
   b) Explain how each component contributes to the overall quantum-inspired design.
   c) Describe how your system incorporates and enhances the quantum coherence effects.
   d) Include a diagram or detailed description of your system's architecture.
   e) Provide a mathematical expression for the energy transfer rate in your system.

3. Efficiency Analysis (200-250 words):
   a) Estimate the theoretical maximum efficiency of your system using the given energy gap.
   b) Compare this to the efficiency of natural photosynthesis and current artificial systems.
   c) Explain how quantum effects contribute to any efficiency gains in your design.
   d) Calculate the Förster energy transfer rate and compare it to your system's rate.

4. Environmental Adaptation (200-250 words):
   a) Describe how your system is optimized for the given environment ({t['environment']}).
   b) Discuss any specific challenges or advantages of this environment for quantum-inspired photosynthesis.
   c) Explain how your design addresses these environmental factors.
   d) Estimate the impact of environmental factors on the coherence time and efficiency.

5. Fabrication and Scalability (200-250 words):
   a) Propose methods for fabricating the key components of your system.
   b) Discuss challenges in maintaining quantum coherence in a scalable design.
   c) Suggest approaches to overcome these challenges.
   d) Estimate the scalability limits of your design in terms of system size and efficiency.

6. Potential Applications (150-200 words):
   a) Describe two potential applications of your quantum-inspired artificial photosynthesis system.
   b) Explain how these applications could impact energy production or environmental sustainability.
   c) Provide quantitative estimates of the potential impact for each application.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of developing and deploying this technology.
   b) Propose guidelines for responsible development and use of quantum-inspired biological systems.
   c) Suggest two directions for future research to enhance or extend your system.

Ensure your response demonstrates a deep understanding of quantum mechanics, photochemistry, and biological energy transfer processes. Be innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide clear explanations for complex concepts.

Format your response with clear headings for each section, and include all calculations and mathematical expressions. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum coherence effects in photosynthesis, including correct calculations of coherence length and energy transfer rates.",
            "The proposed system architecture is innovative, scientifically plausible, and includes a mathematical expression for energy transfer rate.",
            "The efficiency analysis is well-reasoned, compares the system to natural and current artificial systems, and includes calculations of Förster energy transfer rate.",
            "The design is appropriately adapted to the given environment, with quantitative estimates of environmental impacts on coherence time and efficiency.",
            "Fabrication and scalability challenges are addressed with reasonable solutions and quantitative estimates of scalability limits.",
            "Potential applications are relevant, well-explained, and include quantitative estimates of potential impact.",
            "Ethical considerations are thoughtfully discussed with proposed guidelines for responsible development.",
            "The response adheres to the specified format and word count, including all required calculations and mathematical expressions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
