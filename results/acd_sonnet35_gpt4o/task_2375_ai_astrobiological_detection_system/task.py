import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanet_types = [
            "Super-Earth",
            "Hot Jupiter",
            "Ocean world",
            "Ice giant"
        ]
        biosignatures = [
            "Atmospheric gases (e.g., oxygen, methane)",
            "Surface reflectance patterns",
            "Temporal variations in planetary properties",
            "Technosignatures"
        ]
        ai_techniques = [
            "Deep learning",
            "Quantum machine learning",
            "Evolutionary algorithms",
            "Bayesian inference"
        ]
        ethical_concerns = [
            "False positive/negative implications",
            "Impact on extraterrestrial life",
            "Resource allocation for space exploration",
            "Philosophical implications of life detection"
        ]
        return {
            "1": {
                "exoplanet_type": random.choice(exoplanet_types),
                "biosignature": random.choice(biosignatures),
                "ai_technique": random.choice(ai_techniques),
                "ethical_concern": random.choice(ethical_concerns)
            },
            "2": {
                "exoplanet_type": random.choice(exoplanet_types),
                "biosignature": random.choice(biosignatures),
                "ai_technique": random.choice(ai_techniques),
                "ethical_concern": random.choice(ethical_concerns)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered system for detecting and analyzing potential biosignatures on exoplanets, then evaluate its implications for astrobiology and space exploration. Your task should address the following components:

1. System Design (250-300 words):
   a) Describe the key components and architecture of your AI-powered biosignature detection system.
   b) Explain how your system would detect and analyze the {t['biosignature']} on a {t['exoplanet_type']}.
   c) Detail how your system incorporates {t['ai_technique']} and why this technique is particularly suited for this task.
   d) Provide a high-level diagram or pseudocode illustrating a key algorithm in your system.

2. Scientific Analysis (200-250 words):
   a) Discuss the challenges in detecting biosignatures on a {t['exoplanet_type']} and how your AI system addresses them.
   b) Explain how your system distinguishes between biotic and abiotic sources of the detected biosignature.
   c) Describe how your system would handle potential false positives or negatives.

3. Astrobiological Implications (200-250 words):
   a) Analyze how your AI system could advance our understanding of potential life on {t['exoplanet_type']}s.
   b) Discuss how the detection of {t['biosignature']} might influence theories about the origin and distribution of life in the universe.
   c) Explain how your system could be adapted to search for different types of biosignatures or on other exoplanet types.

4. Ethical Considerations (200-250 words):
   a) Evaluate the ethical implications of your AI biosignature detection system, focusing on {t['ethical_concern']}.
   b) Discuss potential unintended consequences of deploying such a system for space exploration.
   c) Propose guidelines or safeguards to ensure responsible use of AI in astrobiology.

5. Interdisciplinary Integration (150-200 words):
   a) Explain how your system integrates knowledge from astronomy, biology, chemistry, and artificial intelligence.
   b) Discuss potential challenges in combining these diverse fields and how your design addresses them.
   c) Propose a novel research question that emerges from this interdisciplinary approach.

Ensure your response demonstrates a deep understanding of astrobiology, exoplanet science, artificial intelligence, and ethical reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the detection and analysis of {t['biosignature']} on a {t['exoplanet_type']}.",
            f"The AI system design must incorporate {t['ai_technique']} and explain its suitability for the task.",
            f"The ethical analysis must focus on {t['ethical_concern']}.",
            "The response must include all five required sections: System Design, Scientific Analysis, Astrobiological Implications, Ethical Considerations, and Interdisciplinary Integration.",
            "The proposed AI system must be innovative and demonstrate a clear integration of astrobiology, exoplanet science, and artificial intelligence.",
            "The response should show a deep understanding of the challenges in detecting biosignatures on exoplanets and propose plausible solutions.",
            "The astrobiological implications should be well-reasoned and consider the broader impact on our understanding of life in the universe.",
            "The ethical considerations should be thoughtful and propose concrete guidelines or safeguards.",
            "The interdisciplinary integration should clearly explain how diverse fields are combined and propose a novel research question."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
