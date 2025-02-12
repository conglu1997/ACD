import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "superposition"
        ]
        biological_processes = [
            "photosynthesis",
            "magnetoreception",
            "olfaction",
            "enzyme catalysis"
        ]
        exoplanet_types = [
            "super-Earth",
            "ocean world",
            "desert planet",
            "gas giant moon"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "exoplanet_type": random.choice(exoplanet_types)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes),
                "exoplanet_type": random.choice(exoplanet_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired biosignature detection system for exoplanet exploration, incorporating principles of quantum biology and information theory. Your system should focus on detecting signs of life on a {t['exoplanet_type']}, utilizing the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']}. Your task has the following components:

1. Theoretical Framework (250-300 words):
   a) Explain how {t['quantum_effect']} could play a role in {t['biological_process']} in potential alien life forms.
   b) Describe how this quantum biological process could create detectable biosignatures on a {t['exoplanet_type']}.
   c) Discuss how principles of quantum information theory could be applied to analyze these biosignatures.

2. Detection System Design (250-300 words):
   a) Propose a novel quantum-inspired sensor or detection method for identifying the biosignatures described in part 1.
   b) Explain how your system incorporates principles of quantum measurement and information processing.
   c) Describe how your system would differentiate between quantum biological signals and non-biological quantum phenomena.

3. Data Analysis Protocol (200-250 words):
   a) Outline a step-by-step protocol for analyzing the data collected by your detection system.
   b) Explain how your protocol accounts for potential sources of error or interference.
   c) Describe how you would quantify the confidence level of a positive biosignature detection.

4. Exoplanet Scenario (200-250 words):
   a) Create a hypothetical scenario where your system detects a potential biosignature on the {t['exoplanet_type']}.
   b) Describe the characteristics of the detected signal and how it relates to {t['quantum_effect']} in {t['biological_process']}.
   c) Explain how your system would confirm or reject the hypothesis of a true biosignature.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of your quantum biosignature detection system for exobiology and SETI.
   b) Propose two potential advancements or modifications to your system for future missions.
   c) Address any ethical considerations related to the search for and potential discovery of alien life.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and information theory. Use appropriate technical terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum effect and its potential role in the given biological process.",
            "The proposed detection system design is innovative and incorporates principles of quantum measurement and information processing.",
            "The data analysis protocol is well-structured and accounts for potential sources of error or interference.",
            "The exoplanet scenario is plausible and clearly illustrates how the detection system would function.",
            "The discussion of implications and future directions shows a broad understanding of the field and its challenges.",
            "The overall response is well-structured, coherent, and demonstrates interdisciplinary knowledge and creative problem-solving.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
