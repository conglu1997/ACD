import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "city_type": "Coastal metropolis",
                "population": 5000000,
                "area": 1500,  # km^2
                "terrain": "Flat with a large bay",
                "peak_commute": 750000,  # people per hour
                "avg_trip_distance": 15  # km
            },
            {
                "city_type": "Mountain valley town",
                "population": 500000,
                "area": 200,  # km^2
                "terrain": "Steep slopes and narrow valleys",
                "peak_commute": 100000,  # people per hour
                "avg_trip_distance": 8  # km
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an innovative urban transportation system for a {t['city_type']} with a population of {t['population']} and an area of {t['area']} km^2. The city's terrain is described as: {t['terrain']}. Your task is to create a novel transportation network that optimizes efficiency, sustainability, and accessibility.

Additional city data:
- Peak commute demand: {t['peak_commute']} people per hour
- Average trip distance: {t['avg_trip_distance']} km

Your response should include the following sections:

1. System Overview (200-250 words):
   a) Describe the key components of your transportation system.
   b) Explain how these components work together to move people and goods.
   c) Discuss how your system addresses the unique challenges posed by the city's terrain and population density.

2. Network Design (250-300 words):
   a) Provide a mathematical model or algorithm for optimizing the layout of your transportation network.
   b) Explain how your model balances factors such as coverage area, travel time, and infrastructure costs.
   c) Describe how your network design adapts to the city's specific geography and population distribution.

3. Efficiency Analysis (200-250 words):
   a) Calculate the theoretical maximum capacity of your system (passengers per hour).
   b) Estimate the average travel time between any two points in the city.
   c) Propose a method for reducing congestion during peak hours.
   d) Compare your system's capacity to the given peak commute demand.

4. Sustainability Features (150-200 words):
   a) Describe the energy sources and propulsion methods used in your system.
   b) Calculate the estimated carbon footprint per passenger-kilometer.
   c) Propose innovative ways to further reduce the environmental impact of your system.

5. Accessibility and Social Impact (150-200 words):
   a) Explain how your system ensures equitable access for all residents, including those with disabilities or in underserved areas.
   b) Discuss the potential social and economic impacts of your transportation system on the city.

6. Future Scalability (100-150 words):
   a) Describe how your system could be expanded or adapted as the city grows.
   b) Propose a method for integrating emerging technologies into your system in the future.

Ensure your response demonstrates a deep understanding of urban planning, mathematical optimization, and sustainable design principles. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and engineering plausibility.

Your total response should be between 1050-1350 words. Use clear headings for each section of your response, numbered exactly as above. Include relevant calculations and quantitative analysis where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts",
            "The transportation system design is innovative and addresses the unique challenges of the given city",
            "The response demonstrates a strong understanding of mathematical optimization and urban planning principles",
            "The efficiency analysis includes realistic calculations and estimates, comparing system capacity to peak commute demand",
            "The sustainability features are well-thought-out and include quantitative assessments of carbon footprint",
            "The accessibility and social impact considerations are comprehensive and insightful",
            "The response shows creativity while maintaining scientific and engineering plausibility",
            "The network design section includes a clear mathematical model or algorithm for optimization",
            "The response uses appropriate technical terminology and provides clear explanations"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
