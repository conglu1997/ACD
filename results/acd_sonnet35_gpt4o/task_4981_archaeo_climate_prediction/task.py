import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ancient_civilizations = [
            {
                'name': 'Maya',
                'region': 'Mesoamerica',
                'period': '2000 BCE - 1500 CE',
                'known_challenges': ['drought', 'deforestation', 'political instability']
            },
            {
                'name': 'Indus Valley',
                'region': 'South Asia',
                'period': '3300 BCE - 1300 BCE',
                'known_challenges': ['climate change', 'tectonic events', 'changing river courses']
            }
        ]
        return {str(i+1): civ for i, civ in enumerate(ancient_civilizations)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze archaeological data and paleoclimate records to predict the fate of the {t['name']} civilization, then design a climate adaptation strategy for a modern analog. Your response should include:

1. Historical Analysis (250-300 words):
   a) Summarize key archaeological findings related to the {t['name']} civilization.
   b) Analyze paleoclimate data for the {t['region']} during the period {t['period']}.
   c) Discuss how climate changes may have interacted with known challenges: {', '.join(t['known_challenges'])}.

2. Predictive Modeling (250-300 words):
   a) Develop a model to predict the fate of the {t['name']} civilization based on available data.
   b) Explain your model's key variables and assumptions.
   c) Describe the predicted outcome and the level of confidence in your prediction.
   d) Discuss any limitations or uncertainties in your model.

3. Modern Analog (150-200 words):
   a) Identify a modern-day region or civilization facing similar climate-related challenges.
   b) Compare and contrast the ancient and modern contexts.
   c) Explain why this is an appropriate analog for your analysis.

4. Climate Adaptation Strategy (250-300 words):
   a) Propose a comprehensive climate adaptation strategy for the modern analog.
   b) Explain how your strategy addresses the challenges faced by both the ancient and modern civilizations.
   c) Discuss the potential effectiveness and feasibility of your proposed solutions.
   d) Consider potential unintended consequences of your adaptation strategy.

5. Interdisciplinary Insights (200-250 words):
   a) Discuss how this analysis contributes to our understanding of societal resilience and collapse.
   b) Explain how integrating archaeology and climatology can inform modern sustainable development practices.
   c) Propose a specific research question that emerges from this interdisciplinary analysis.

6. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using predictive models to analyze past civilizations.
   b) Address potential issues in applying these insights to modern societies.
   c) Propose guidelines for the responsible use of such interdisciplinary models in policy-making.

Ensure your response demonstrates a deep understanding of archaeology, climatology, and sustainable development. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a thorough analysis of the {t['name']} civilization and its climate challenges.",
            "A predictive model is developed and explained clearly, with discussion of its limitations.",
            "An appropriate modern analog is identified and compared to the ancient civilization.",
            "A comprehensive climate adaptation strategy is proposed for the modern analog.",
            "The response demonstrates integration of knowledge from archaeology, climatology, and sustainable development.",
            "Ethical considerations of the analysis and its applications are discussed.",
            "The analysis is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
