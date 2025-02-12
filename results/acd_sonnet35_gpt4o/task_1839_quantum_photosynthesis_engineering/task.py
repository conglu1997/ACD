import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            {
                'name': 'Proxima Centauri b',
                'star_type': 'Red dwarf',
                'light_intensity': '0.65 times Earth'
            },
            {
                'name': 'TRAPPIST-1e',
                'star_type': 'Ultra-cool dwarf',
                'light_intensity': '0.604 times Earth'
            },
            {
                'name': 'K2-18b',
                'star_type': 'Red dwarf',
                'light_intensity': '0.27 times Earth'
            }
        ]
        return {str(i+1): planet for i, planet in enumerate(random.sample(exoplanets, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-enhanced photosynthetic system for plants on the low-light exoplanet {t['name']}, which orbits a {t['star_type']} star and receives {t['light_intensity']} of the light intensity Earth receives. Then, analyze its potential impact on the planet's ecosystem and propose a method to artificially replicate this system. Your response should include:

1. Quantum-Enhanced Photosynthesis Design (300-350 words):
   a) Describe the key components of your quantum-enhanced photosynthetic system.
   b) Explain how quantum effects (e.g., quantum coherence, tunneling) are utilized to improve light harvesting efficiency.
   c) Detail how your system is adapted to the specific light conditions of the exoplanet.
   d) Provide a diagram or schematic representation of your system (use ASCII art or a clear textual description).
   e) Compare your system to a known quantum effect in Earth-based photosynthesis (e.g., quantum coherence in light-harvesting complexes).

2. Efficiency Analysis (200-250 words):
   a) Estimate the improved efficiency of your quantum-enhanced system compared to Earth-based photosynthesis.
   b) Explain the calculations or reasoning behind your efficiency estimate.
   c) Discuss any trade-offs, limitations, or potential drawbacks of your system.

3. Ecosystem Impact (250-300 words):
   a) Predict how your quantum-enhanced photosynthetic system might affect plant life on the exoplanet.
   b) Discuss potential cascading effects on other organisms in the ecosystem.
   c) Speculate on long-term evolutionary implications for life on the planet.

4. Artificial Replication (250-300 words):
   a) Propose a method to artificially replicate your quantum-enhanced photosynthetic system in a laboratory setting.
   b) Describe the key technologies or techniques required for this replication.
   c) Discuss potential challenges in the replication process and how they might be overcome.

5. Experimental Verification (200-250 words):
   a) Propose an experiment to test and verify the quantum nature of your designed system.
   b) Explain what results would confirm the quantum effects and how they would be measured.
   c) Discuss potential difficulties in conducting this experiment and how they might be addressed.

6. Practical Applications (200-250 words):
   a) Suggest two potential applications of your quantum-enhanced photosynthetic system on Earth.
   b) Explain how these applications could address current challenges in agriculture or energy production.
   c) Discuss any ethical considerations or potential risks related to implementing this technology.

Ensure your response demonstrates a deep understanding of quantum physics, photosynthesis, and exoplanet environments. Use scientific terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section.

Your total response should be between 1400-1700 words. Please use numbered headings for each section and lettered subheadings where applicable.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, photosynthesis, and exoplanet environments.",
            "The quantum-enhanced photosynthetic system design is creative, original, and scientifically plausible.",
            "The efficiency analysis includes a reasonable estimate, clear explanation, and discussion of limitations.",
            "The ecosystem impact analysis is thorough and considers multiple levels of effects.",
            "The artificial replication method is well-thought-out and addresses potential challenges.",
            "The experimental verification proposal is scientifically sound and addresses potential difficulties.",
            "The practical applications are innovative, relevant to current global challenges, and consider ethical implications.",
            "The response includes all required sections with appropriate detail and word count.",
            "Scientific terminology is used appropriately and explanations are provided where necessary.",
            "The response includes a diagram or schematic representation of the photosynthetic system.",
            "The design demonstrates interdisciplinary knowledge synthesis and creative scientific reasoning.",
            f"The response specifically addresses the conditions of the exoplanet {t['name']} with its {t['star_type']} star and {t['light_intensity']} light intensity.",
            "The response compares the proposed system with a known quantum effect in Earth-based photosynthesis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
