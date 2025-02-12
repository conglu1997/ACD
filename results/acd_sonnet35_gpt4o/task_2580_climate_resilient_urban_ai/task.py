import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_challenges = [
            "sea level rise",
            "extreme heat waves",
            "increased precipitation and flooding",
            "prolonged droughts"
        ]
        urban_elements = [
            "transportation systems",
            "energy infrastructure",
            "water management",
            "building design"
        ]
        return {
            "1": {
                "climate_challenge": random.choice(climate_challenges),
                "urban_element": random.choice(urban_elements)
            },
            "2": {
                "climate_challenge": random.choice(climate_challenges),
                "urban_element": random.choice(urban_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that optimizes urban infrastructure for climate resilience, focusing on addressing {t['climate_challenge']} through innovations in {t['urban_element']}. Your system should incorporate principles from urban planning, climate science, and machine learning. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system for climate-resilient urban optimization.
   b) Explain how your system integrates urban planning principles, climate science data, and machine learning algorithms.
   c) Detail any novel computational approaches or modeling techniques you would employ.

2. Data Integration and Processing (200-250 words):
   a) Specify the types of data your system would use (e.g., climate projections, urban infrastructure data, socioeconomic information).
   b) Explain how your system would process and integrate these diverse data sources.
   c) Discuss any challenges in data acquisition or integration and how you'd address them.

3. Predictive Modeling and Optimization (250-300 words):
   a) Describe your approach to modeling the impacts of {t['climate_challenge']} on {t['urban_element']}.
   b) Explain how your AI system would generate and evaluate potential adaptation strategies.
   c) Detail the optimization algorithms used to balance multiple objectives (e.g., resilience, cost, social equity).

4. Adaptive Learning and Uncertainty Management (200-250 words):
   a) Explain how your system would adapt its models and recommendations as new data becomes available.
   b) Describe your approach to managing uncertainties in climate projections and urban development scenarios.
   c) Discuss how the system would handle potential conflicts between short-term and long-term optimization goals.

5. Interdisciplinary Validation and Collaboration (150-200 words):
   a) Propose methods for validating your system's recommendations across different disciplines.
   b) Describe how your AI system could facilitate collaboration between urban planners, climate scientists, and policymakers.
   c) Discuss potential challenges in interdisciplinary communication and how your system might address them.

6. Ethical Considerations and Social Impact (150-200 words):
   a) Identify potential ethical issues in using AI for urban climate adaptation planning.
   b) Discuss how your system would address equity concerns and avoid exacerbating existing urban inequalities.
   c) Propose guidelines for responsible development and deployment of such AI systems in urban planning contexts.

7. Future Directions and Scalability (100-150 words):
   a) Suggest two potential extensions or modifications to your system for future research.
   b) Discuss how your approach could be scaled or adapted to different urban contexts globally.

Ensure your response demonstrates a deep understanding of urban planning, climate science, and artificial intelligence. Be innovative in your approach while maintaining scientific and practical plausibility. Use technical terminology appropriately and provide explanations where necessary. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a sophisticated understanding of {t['climate_challenge']} and its impact on urban {t['urban_element']}.",
            "The proposed AI system architecture is innovative and plausibly capable of integrating urban planning, climate science, and machine learning principles.",
            "The approach to data integration, predictive modeling, and optimization is well-reasoned and technically sound.",
            "The response addresses ethical considerations and social impacts thoughtfully.",
            "The proposed system demonstrates potential for real-world applicability and scalability in urban climate resilience planning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
