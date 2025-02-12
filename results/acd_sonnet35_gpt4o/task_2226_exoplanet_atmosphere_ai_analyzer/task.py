import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "planet_type": "super-Earth",
                "star_type": "M-dwarf",
                "atmospheric_component": "methane"
            },
            {
                "planet_type": "hot Jupiter",
                "star_type": "G-type",
                "atmospheric_component": "water vapor"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and predicts exoplanetary atmospheres using spectroscopic data, focusing on a {t['planet_type']} orbiting a {t['star_type']} star. Your system should be particularly adept at detecting and analyzing {t['atmospheric_component']}. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for exoplanetary atmosphere analysis.
   b) Explain how your model incorporates principles from astrophysics, spectroscopy, and machine learning.
   c) Detail how you represent and analyze spectroscopic data to infer atmospheric composition.
   d) Explain how your system accounts for the specific challenges of the given planet and star type.

2. Atmospheric Analysis (200-250 words):
   a) Describe how your model detects and quantifies the presence of {t['atmospheric_component']}.
   b) Explain how your system differentiates between atmospheric signals and stellar contamination.
   c) Discuss any novel predictions your model makes about atmospheric chemistry or dynamics.

3. Evolutionary Modeling (200-250 words):
   a) Explain how your system models the long-term evolution of the exoplanet's atmosphere.
   b) Describe how you account for factors such as stellar radiation, planetary mass, and atmospheric escape.
   c) Provide an example scenario of atmospheric changes over time for the given planet type.

4. Machine Learning Implementation (150-200 words):
   a) Describe the specific machine learning techniques used in your system.
   b) Explain how you would train and validate your model using limited exoplanetary data.
   c) Discuss potential biases in your model and how you would address them.

5. Experimental Design (150-200 words):
   a) Propose an observation strategy to test a key prediction of your model.
   b) Describe the methodology and expected outcomes.
   c) Discuss potential challenges in verifying your model's predictions.

6. Implications and Future Work (150-200 words):
   a) Discuss the implications of your system for exoplanetary science and the search for habitable worlds.
   b) Explore how your model might impact our understanding of planetary formation and evolution.
   c) Suggest future improvements or extensions to your system.

Ensure your response demonstrates a deep understanding of astrophysics, spectroscopy, and machine learning. Be innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide clear explanations for complex concepts.

Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of astrophysics, spectroscopy, and machine learning principles.",
            f"The proposed AI system effectively incorporates analysis of {t['atmospheric_component']} and accounts for the specific challenges of {t['planet_type']} planets orbiting {t['star_type']} stars.",
            "The atmospheric analysis and evolutionary modeling components are well-reasoned and scientifically plausible.",
            "The machine learning implementation is appropriate and addresses challenges specific to exoplanetary data analysis.",
            "The experimental design and future work sections demonstrate critical thinking and awareness of current challenges in exoplanetary science.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
