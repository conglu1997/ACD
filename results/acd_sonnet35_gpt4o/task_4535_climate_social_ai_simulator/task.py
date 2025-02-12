import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'climate_event': 'Sea level rise',
                'social_factor': 'Economic inequality',
                'timeframe': '2050'
            },
            {
                'climate_event': 'Extreme heat waves',
                'social_factor': 'Political polarization',
                'timeframe': '2040'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and predicts the complex interactions between climate change and human social behavior, focusing on the climate event of {t['climate_event']}, the social factor of {t['social_factor']}, and a timeframe extending to {t['timeframe']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for climate-social simulation.
   b) Explain how it integrates climate models with social behavior models.
   c) Detail the data sources and types your system would use.
   d) Discuss how your system handles uncertainty and complexity in both climate and social systems.

2. Climate-Social Interface (250-300 words):
   a) Explain how your system models the impact of {t['climate_event']} on social behavior.
   b) Describe how it accounts for {t['social_factor']} in its predictions.
   c) Discuss any feedback loops between climate changes and social responses in your model.

3. Prediction Mechanism (250-300 words):
   a) Detail the AI/ML techniques your system uses to generate predictions.
   b) Explain how your system validates its predictions against historical data.
   c) Describe how it handles long-term predictions up to {t['timeframe']}.
   d) Provide an example prediction your system might make, with reasoning.

4. Ethical Considerations (200-250 words):
   a) Discuss potential ethical issues in using AI to predict social responses to climate change.
   b) Address concerns about data privacy, algorithmic bias, and the potential for misuse of predictions.
   c) Propose guidelines for the responsible development and use of such systems.

5. Applications and Implications (200-250 words):
   a) Suggest potential applications of your system in policy-making, urban planning, or disaster preparedness.
   b) Discuss how your system might influence public understanding of climate change and its social impacts.
   c) Consider potential unintended consequences of deploying such a system.

6. Limitations and Future Work (150-200 words):
   a) Acknowledge the limitations of your approach.
   b) Suggest areas for improvement or expansion of your system.
   c) Propose a future research direction that could enhance the system's capabilities or address its limitations.

Ensure your response demonstrates a deep understanding of climate science, social psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of climate science, social psychology, and artificial intelligence, particularly in relation to {t['climate_event']} and {t['social_factor']}.",
            "The AI system architecture is well-designed, integrating climate models with social behavior models effectively.",
            f"The prediction mechanism is clearly explained and accounts for long-term predictions up to {t['timeframe']}.",
            "Ethical considerations are thoroughly addressed, including data privacy and potential misuse of predictions.",
            "Potential applications and implications of the system are thoughtfully discussed.",
            "Limitations are acknowledged and future research directions are proposed.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
