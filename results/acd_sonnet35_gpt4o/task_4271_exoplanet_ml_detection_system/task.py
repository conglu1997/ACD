import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        detection_methods = [
            {"method": "transit photometry", "wavelength": "visible light", "target": "Earth-like planets"},
            {"method": "radial velocity", "wavelength": "infrared", "target": "gas giants"},
            {"method": "direct imaging", "wavelength": "near-infrared", "target": "young, hot planets"},
            {"method": "gravitational microlensing", "wavelength": "multiple", "target": "cold, low-mass planets"}
        ]
        return {
            "1": random.choice(detection_methods),
            "2": random.choice(detection_methods)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an advanced machine learning system for detecting and characterizing exoplanets using {t['method']} in the {t['wavelength']} spectrum, with a focus on identifying {t['target']}. Then, analyze its potential impact on our understanding of planetary formation and the search for extraterrestrial life. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your machine learning system for exoplanet detection and characterization.
   b) Explain how your system processes and analyzes {t['wavelength']} data from {t['method']}.
   c) Detail any novel machine learning techniques or algorithms you've incorporated to enhance detection of {t['target']}.
   d) Discuss how your system handles noise reduction and false positive elimination.

2. Data Processing and Feature Extraction (250-300 words):
   a) Explain the data preprocessing steps required for {t['method']} observations.
   b) Describe the key features your system extracts from the {t['wavelength']} data.
   c) Discuss any challenges specific to detecting {t['target']} and how your system addresses them.

3. Machine Learning Model (250-300 words):
   a) Describe the machine learning model(s) used in your system, explaining why they are suitable for this task.
   b) Explain how your model is trained, including the type and source of training data.
   c) Discuss how your model handles the unique challenges of exoplanet detection, such as class imbalance or rare event detection.

4. Performance Evaluation (200-250 words):
   a) Propose methods to evaluate the accuracy and reliability of your system.
   b) Discuss potential biases in your system and how you would mitigate them.
   c) Compare the expected performance of your system to current exoplanet detection methods.

5. Exoplanet Characterization (200-250 words):
   a) Explain how your system determines key characteristics of detected exoplanets (e.g., size, mass, composition, atmosphere).
   b) Discuss the limitations of your approach in characterizing {t['target']}.
   c) Propose improvements or additional data that could enhance characterization accuracy.

6. Impact on Planetary Formation Theories (150-200 words):
   a) Analyze how the data from your system might influence our understanding of planetary formation.
   b) Discuss any specific hypotheses about {t['target']} that your system could help test.

7. Implications for Extraterrestrial Life Search (150-200 words):
   a) Explore how your system could contribute to the search for potentially habitable exoplanets.
   b) Discuss the implications of detecting {t['target']} for the possibility of extraterrestrial life.

8. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of using AI for exoplanet detection and characterization.
   b) Propose future research directions or extensions of your system.

Ensure your response demonstrates a deep understanding of astrophysics, data science, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1650-2050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of astrophysics, data science, and machine learning, particularly in relation to {t['method']} and {t['target']} detection.",
            "The proposed machine learning system is innovative, logically consistent, and effectively addresses the challenges of exoplanet detection and characterization.",
            "The response adequately covers all required sections, providing detailed explanations and analysis for each topic.",
            "The discussion of the system's impact on planetary formation theories and the search for extraterrestrial life is insightful and well-reasoned.",
            "The response addresses ethical implications and proposes meaningful future research directions.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
