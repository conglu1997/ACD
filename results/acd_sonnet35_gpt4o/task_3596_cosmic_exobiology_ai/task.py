import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        celestial_bodies = [
            {
                "name": "Europa (Jupiter's moon)",
                "environment": "Subsurface ocean with potential hydrothermal activity",
                "key_challenge": "High pressure and low temperature"
            },
            {
                "name": "Titan (Saturn's moon)",
                "environment": "Methane lakes and hydrocarbon-rich atmosphere",
                "key_challenge": "Extremely low temperature and non-water-based biochemistry"
            }
        ]
        return {str(i+1): body for i, body in enumerate(random.sample(celestial_bodies, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to model and predict potential forms of life that could exist in extreme cosmic environments, then analyze its predictions for {t['name']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling exotic life forms.
   b) Explain how your system integrates data from astrophysics, biochemistry, and evolutionary biology.
   c) Detail any novel machine learning approaches or algorithms you've incorporated.
   d) Discuss how your system handles uncertainties and makes predictions about unknown biochemical processes.

2. Environmental Analysis (200-250 words):
   a) Analyze the key characteristics of {t['name']}'s environment: {t['environment']}.
   b) Discuss how these characteristics would influence potential life forms.
   c) Identify the primary challenge for life in this environment: {t['key_challenge']}.

3. Life Form Prediction (250-300 words):
   a) Describe a potential life form your AI system predicts could exist on {t['name']}.
   b) Explain its key biological features and how they address the environmental challenges.
   c) Discuss its predicted biochemistry, energy acquisition, and reproduction methods.

4. Comparative Xenobiology (200-250 words):
   a) Compare your predicted life form to known Earth-based extremophiles.
   b) Discuss how it challenges or extends our current understanding of the requirements for life.
   c) Propose a framework for classifying and comparing exotic life forms across different cosmic environments.

5. Experimental Validation (200-250 words):
   a) Design a hypothetical experiment or mission to detect and study the predicted life form on {t['name']}.
   b) Explain how you would validate your AI system's predictions.
   c) Discuss potential biosignatures that could indicate the presence of your predicted life form.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the potential impact of discovering exotic life forms on our understanding of life and our place in the universe.
   b) Address ethical considerations in the search for and study of extraterrestrial life.
   c) Explore how AI-driven xenobiology might influence future space exploration and astrobiology research.

7. Limitations and Future Directions (150-200 words):
   a) Identify key limitations of your AI system and approach.
   b) Propose future research directions to improve exotic life modeling and prediction.
   c) Suggest how this technology might be applied to other areas of science or space exploration.

Ensure your response demonstrates a deep understanding of astrophysics, biochemistry, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and length.",
            f"The AI system design effectively addresses the modeling of potential life forms on {t['name']}.",
            "The response demonstrates a deep understanding of astrophysics, biochemistry, evolutionary biology, and artificial intelligence.",
            "The proposed AI system architecture is innovative, well-explained, and scientifically plausible.",
            "The predicted life form is creative yet grounded in scientific principles, addressing the specific environmental challenges of the celestial body.",
            "The response shows careful consideration of experimental validation, ethical implications, and future research directions.",
            "The writing is clear, well-organized, and uses appropriate technical terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
