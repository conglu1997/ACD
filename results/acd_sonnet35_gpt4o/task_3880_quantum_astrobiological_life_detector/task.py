import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            {"name": "Kepler-442b", "type": "Super-Earth", "atmosphere": "Nitrogen-rich"},
            {"name": "TRAPPIST-1e", "type": "Earth-sized", "atmosphere": "Possibly water-rich"},
            {"name": "K2-18b", "type": "Mini-Neptune", "atmosphere": "Hydrogen-rich"},
            {"name": "Proxima Centauri b", "type": "Terrestrial", "atmosphere": "Unknown composition"}
        ]
        return {str(i+1): planet for i, planet in enumerate(random.sample(exoplanets, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system integrated with advanced AI to detect and analyze potential biosignatures in the atmosphere of {t['name']}, a {t['type']} exoplanet with a {t['atmosphere']} atmosphere. Then, propose a novel method for classifying the likelihood of life based on this analysis. Your response should include:

1. Quantum-AI System Architecture (300-350 words):
   a) Describe the overall structure of your quantum-AI hybrid system for exoplanetary atmosphere analysis.
   b) Explain how quantum computing principles are integrated with AI algorithms in your design.
   c) Detail how your system would process and analyze spectroscopic data from {t['name']}'s atmosphere.
   d) Propose a novel quantum algorithm or AI technique specifically designed for biosignature detection.

2. Biosignature Detection Methodology (250-300 words):
   a) Explain how your system would identify potential biosignatures in a {t['atmosphere']} atmosphere.
   b) Describe the quantum states or AI models used to represent atmospheric components and potential biomarkers.
   c) Discuss how your system accounts for potential false positives or abiotic mimics of biosignatures.

3. Data Analysis and Interpretation (250-300 words):
   a) Propose a method for quantifying the uncertainty in biosignature detection using quantum principles.
   b) Explain how your AI component would interpret the quantum-processed spectral data.
   c) Describe how your system would handle the vast amount of data from exoplanetary observations.

4. Novel Life Classification System (200-250 words):
   a) Propose a new method or scale for classifying the likelihood of life on {t['name']} based on your system's analysis.
   b) Explain how this classification system incorporates both quantum and classical probabilities.
   c) Discuss how your system would account for potential forms of life different from Earth-based biology.

5. Theoretical Performance and Limitations (200-250 words):
   a) Estimate the theoretical performance of your quantum-AI system compared to classical methods.
   b) Discuss potential limitations of your approach and how they might be addressed.
   c) Propose a method for validating your system's accuracy without direct observation of the exoplanet.

6. Implications and Future Directions (150-200 words):
   a) Discuss the potential impact of your system on the field of astrobiology and SETI.
   b) Propose two potential technological advancements that could enhance your system's capabilities.
   c) Suggest ethical considerations for the use of advanced AI in the search for extraterrestrial life.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, astrophysics, and astrobiology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, artificial intelligence, astrophysics, and astrobiology",
            "The proposed system integrates quantum computing and AI in a novel and plausible way",
            "The biosignature detection methodology is well-explained and accounts for the specific atmospheric composition of the given exoplanet",
            "The novel life classification system is creative and scientifically grounded",
            "The response addresses potential limitations and ethical considerations",
            "The answer is well-structured, clear, and within the specified word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
