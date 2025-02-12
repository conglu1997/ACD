class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "planet_type": "Super-Earth",
                "star_type": "M-dwarf",
                "target_molecule": "Methane"
            },
            "2": {
                "planet_type": "Ocean world",
                "star_type": "G-type (Sun-like)",
                "target_molecule": "Oxygen"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered spectral analysis system to detect potential biosignatures on exoplanets, focusing on a {t['planet_type']} orbiting a {t['star_type']} star, with {t['target_molecule']} as a key target molecule. Your response should include:

        1. System Architecture (300-350 words):
           a) Describe the key components of your AI-powered spectral analysis system.
           b) Explain how it integrates principles from astrobiology, spectroscopy, and machine learning.
           c) Detail how your system accounts for the specific characteristics of the {t['planet_type']} and {t['star_type']} star.
           d) Provide a diagram or pseudocode representation of a key component in your system.

        2. Biosignature Detection Methodology (250-300 words):
           a) Explain your approach to detecting {t['target_molecule']} and other potential biosignatures.
           b) Describe how your system distinguishes between biotic and abiotic sources of the target molecule.
           c) Discuss how your system handles potential false positives and negatives.
           d) Propose a novel method for improving the accuracy of biosignature detection.

        3. Machine Learning Integration (250-300 words):
           a) Describe the specific machine learning techniques used in your system.
           b) Explain how these techniques enhance the detection and analysis of biosignatures.
           c) Discuss your approach to training the AI model, including data sources and preprocessing.
           d) Address potential biases or limitations in your machine learning approach.

        4. Speculative Astrobiological Analysis (200-250 words):
           a) Based on your system's capabilities, propose a hypothetical scenario of life on the {t['planet_type']}.
           b) Discuss how the presence of {t['target_molecule']} and other detected molecules could support this scenario.
           c) Explain how the {t['star_type']} star's characteristics might influence potential life forms.

        5. Comparative Planetology (200-250 words):
           a) Compare your approach to studying the {t['planet_type']} with methods used to study potentially habitable worlds in our solar system.
           b) Discuss how your system could be adapted to analyze different types of exoplanets.
           c) Propose a method to validate your system's predictions using solar system bodies as proxies.

        6. Ethical Considerations and SETI Implications (150-200 words):
           a) Discuss the potential impact of detecting biosignatures on an exoplanet.
           b) Address ethical considerations in announcing potential discovery of extraterrestrial life.
           c) Explain how your system could contribute to SETI (Search for Extraterrestrial Intelligence) efforts.

        Ensure your response demonstrates a deep understanding of astrobiology, spectroscopy, and machine learning. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

        Format your response with clear headings for each section. Your total response should be between 1350-1650 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            "The system architecture demonstrates a coherent integration of astrobiology, spectroscopy, and machine learning principles.",
            "The biosignature detection methodology is scientifically plausible and addresses the specific planet type, star type, and target molecule.",
            "The machine learning integration is well-explained and appropriate for the task.",
            "The speculative astrobiological analysis is creative yet grounded in scientific principles.",
            "The comparative planetology section provides insightful connections to solar system studies.",
            "Ethical considerations and SETI implications are thoughtfully addressed.",
            "The overall response shows interdisciplinary knowledge, creative problem-solving, and scientific reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
