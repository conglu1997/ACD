import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "city_type": "coastal metropolis",
                "initial_population": 5000000,
                "climate_challenge": "sea level rise",
                "economic_focus": "tourism and tech industry"
            },
            {
                "city_type": "inland industrial center",
                "initial_population": 2000000,
                "climate_challenge": "extreme heat waves",
                "economic_focus": "manufacturing and logistics"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and manage a sustainable urban ecosystem for a {t['city_type']} with an initial population of {t['initial_population']}, focusing on balancing economic growth, environmental conservation, and social equity over a simulated 50-year period. Your city faces the climate challenge of {t['climate_challenge']} and has an economic focus on {t['economic_focus']}. Your task has the following components:

1. Initial Urban Design (250-300 words):
   a) Describe your city's layout and key infrastructure components.
   b) Explain how your initial design addresses the specific climate challenge and economic focus.
   c) Discuss how you've incorporated principles of sustainability and resilience.

2. 50-Year Development Plan (300-350 words):
   a) Outline a decade-by-decade strategy for sustainable growth and adaptation.
   b) Explain how you'll balance economic development with environmental conservation.
   c) Describe your approach to ensuring social equity as the city develops.
   d) Discuss how you'll address changing demographics and technological advancements.

3. Resource Management (200-250 words):
   a) Describe your strategy for managing key resources (e.g., energy, water, waste).
   b) Explain how you'll transition to renewable energy sources over time.
   c) Discuss your approach to circular economy principles and waste reduction.

4. Environmental Impact and Mitigation (200-250 words):
   a) Analyze the potential environmental impacts of your urban development.
   b) Describe specific measures to mitigate these impacts and enhance biodiversity.
   c) Explain how you'll monitor and adapt to changing environmental conditions.

5. Social and Economic Policies (200-250 words):
   a) Outline key policies to promote social equity and economic opportunity.
   b) Describe your approach to housing, education, and healthcare.
   c) Explain how you'll manage potential conflicts between economic growth and social/environmental goals.

6. Resilience and Adaptation (150-200 words):
   a) Describe how your city will adapt to and mitigate the effects of {t['climate_challenge']}.
   b) Explain your strategy for handling potential crises (e.g., natural disasters, economic shocks).
   c) Discuss how you'll maintain flexibility in your long-term plan to address unforeseen challenges.

7. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of your urban development decisions.
   b) Explain how you've balanced the needs of current and future generations.
   c) Describe any potential unintended consequences of your plan and how you'll address them.

Ensure your response demonstrates a deep understanding of urban planning, environmental science, economics, and social dynamics. Use appropriate terminology and provide clear explanations. Be innovative in your approach while maintaining plausibility. Your total response should be between 1450-1800 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of urban planning, environmental science, economics, and social dynamics.",
            "The urban design and development plan effectively addresses the specific climate challenge and economic focus of the given scenario.",
            "The 50-year plan shows a clear strategy for balancing economic growth, environmental conservation, and social equity.",
            "The resource management approach incorporates sustainable practices and circular economy principles.",
            "Environmental impacts are thoroughly analyzed, and effective mitigation strategies are proposed.",
            "Social and economic policies promote equity and opportunity while addressing potential conflicts with other goals.",
            "The plan demonstrates adaptability and resilience in the face of the specified climate challenge and potential crises.",
            "Ethical considerations are thoughtfully addressed, including intergenerational equity and potential unintended consequences.",
            "The response is innovative while maintaining plausibility and scientific rigor.",
            "The submission adheres to the specified word count range and formatting guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
