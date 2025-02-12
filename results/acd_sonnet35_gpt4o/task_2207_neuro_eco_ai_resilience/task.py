import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = ['Coral Reef', 'Rainforest']
        climate_challenges = ['Ocean Acidification', 'Increasing Temperatures']
        tasks = [
            {
                'ecosystem': ecosystems[0],
                'climate_challenge': climate_challenges[0]
            },
            {
                'ecosystem': ecosystems[1],
                'climate_challenge': climate_challenges[1]
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by neuroplasticity to model and enhance the resilience of the {t['ecosystem']} ecosystem in the face of {t['climate_challenge']}. Your response should include:

1. Neuroplasticity-Inspired Architecture (250-300 words):
   a) Describe the key components of your AI system and how they mimic neuroplasticity principles.
   b) Explain how your system models the {t['ecosystem']} ecosystem and its response to {t['climate_challenge']}.
   c) Detail how your architecture incorporates learning and adaptation mechanisms.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Ecosystem Modeling (200-250 words):
   a) Explain how your system represents key species and their interactions in the {t['ecosystem']}.
   b) Describe how your model simulates the impact of {t['climate_challenge']} on the ecosystem.
   c) Discuss how your system captures the complexity and interconnectedness of the ecosystem.

3. Adaptive Mechanisms (200-250 words):
   a) Detail the specific neuroplasticity-inspired mechanisms your system uses to enhance ecosystem resilience.
   b) Explain how these mechanisms allow the ecosystem to adapt to {t['climate_challenge']}.
   c) Provide an example of how your system might respond to a sudden environmental change.

4. Learning and Prediction (150-200 words):
   a) Describe how your system learns from environmental data and ecosystem responses.
   b) Explain how it generates predictions about future ecosystem states under continued {t['climate_challenge']}.
   c) Discuss the limitations and uncertainties in your system's predictive capabilities.

5. Intervention Strategies (200-250 words):
   a) Explain how your system develops intervention strategies to enhance ecosystem resilience.
   b) Provide an example of a specific intervention your system might propose for the {t['ecosystem']}.
   c) Describe how your system evaluates the effectiveness and potential consequences of interventions.

6. Ethical Considerations (100-150 words):
   a) Discuss the ethical implications of using AI to guide ecosystem management.
   b) Address potential risks or unintended consequences of your system's interventions.
   c) Propose guidelines for responsible development and use of neuro-inspired AI in ecology.

7. Scalability and Future Directions (100-150 words):
   a) Discuss how your system could be scaled or adapted to other ecosystems and environmental challenges.
   b) Propose two specific research directions to further enhance your system's capabilities.

Ensure your response demonstrates a deep understanding of neuroplasticity, artificial intelligence, and ecology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroplasticity principles and their application to AI systems for modeling the {t['ecosystem']} ecosystem.",
            f"The proposed AI system effectively models the {t['ecosystem']} and its response to {t['climate_challenge']}, incorporating learning and adaptation mechanisms.",
            "The adaptive mechanisms and intervention strategies are innovative, plausible, and well-explained.",
            "The response addresses ethical considerations and proposes responsible guidelines for the use of AI in ecosystem management.",
            "The submission demonstrates strong interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
