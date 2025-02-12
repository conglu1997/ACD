import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "exoplanet": "Kepler-186f",
                "atmospheric_composition": "Nitrogen-rich with traces of methane and oxygen",
                "quantum_technique": "Quantum Fourier Transform",
                "ethical_dilemma": "Potential interference with alien evolution"
            },
            {
                "exoplanet": "TRAPPIST-1e",
                "atmospheric_composition": "CO2-dominated with water vapor",
                "quantum_technique": "Quantum Principal Component Analysis",
                "ethical_dilemma": "Responsibility of contact initiation"
            },
            {
                "exoplanet": "Proxima Centauri b",
                "atmospheric_composition": "Thin atmosphere with hydrogen and helium",
                "quantum_technique": "Quantum Support Vector Machine",
                "ethical_dilemma": "Balancing scientific curiosity with non-interference"
            },
            {
                "exoplanet": "K2-18b",
                "atmospheric_composition": "Hydrogen-rich with water vapor and methane",
                "quantum_technique": "Quantum Neural Network",
                "ethical_dilemma": "Ethical implications of AI-driven first contact"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system for detecting and analyzing potential biosignatures in exoplanet atmospheres, focusing on {t['exoplanet']} with its {t['atmospheric_composition']}. Your system should incorporate the quantum technique of {t['quantum_technique']}. Then, apply your system to a hypothetical scenario of first contact, addressing the ethical dilemma of {t['ethical_dilemma']}. Your response should include the following sections:

1. Quantum-AI System Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced AI system for biosignature detection.
   b) Explain how {t['quantum_technique']} is integrated into your system and its role in analyzing exoplanet atmospheres.
   c) Detail how your system processes and interprets atmospheric data to identify potential biosignatures.
   d) Discuss any novel approaches your system brings to the field of astrobiology.

2. Exoplanet Analysis (250-300 words):
   a) Apply your system to analyze the atmosphere of {t['exoplanet']}.
   b) Describe how your system interprets the {t['atmospheric_composition']} in the context of potential biosignatures.
   c) Discuss the likelihood of life based on your system's analysis and explain the reasoning.
   d) Address any limitations or uncertainties in your system's analysis.

3. First Contact Scenario (250-300 words):
   a) Describe a hypothetical first contact scenario based on your system's detection of biosignatures.
   b) Explain how your AI system would assist in communication or understanding of the potential alien life.
   c) Discuss how the quantum aspects of your system might provide unique advantages in this scenario.

4. Ethical Considerations (200-250 words):
   a) Address the ethical dilemma of {t['ethical_dilemma']} in the context of your first contact scenario.
   b) Discuss the potential risks and benefits of using your quantum-AI system in first contact situations.
   c) Propose guidelines for the ethical use of advanced AI and quantum technologies in astrobiology and extraterrestrial contact.

5. Scientific and Societal Implications (200-250 words):
   a) Analyze the potential impact of your system on the field of astrobiology and the search for extraterrestrial life.
   b) Discuss how the integration of quantum computing and AI might transform our approach to space exploration and exoplanet research.
   c) Explore the broader societal implications of potentially discovering and contacting alien life.

6. Future Developments (150-200 words):
   a) Propose two potential enhancements or extensions to your quantum-AI astrobiological system.
   b) Suggest a novel research direction that combines insights from your system with another scientific discipline.
   c) Speculate on how your system might evolve with future advancements in quantum computing and AI.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, astrobiology, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, d) where applicable. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, AI, and astrobiology, particularly in relation to {t['exoplanet']} and its {t['atmospheric_composition']}.",
            f"The proposed system effectively incorporates {t['quantum_technique']} for biosignature detection and analysis, with a clear explanation of its role.",
            "The first contact scenario is plausible, creative, and directly relates to the system's capabilities and the exoplanet's characteristics.",
            f"The ethical dilemma of {t['ethical_dilemma']} is thoughtfully addressed with specific examples and proposed guidelines.",
            "The response discusses concrete scientific and societal implications of the proposed system and potential alien contact.",
            "The proposed future developments are innovative, feasible, and build upon the core concepts of the system.",
            "The response is well-structured, following the specified format, including numbered sections, subheadings, and word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
