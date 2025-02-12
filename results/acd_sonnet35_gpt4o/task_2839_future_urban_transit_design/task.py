import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'city_type': 'Coastal megacity',
                'environmental_challenge': 'Rising sea levels',
                'social_focus': 'Equity and accessibility'
            },
            {
                'city_type': 'Inland metropolis',
                'environmental_challenge': 'Extreme heat waves',
                'social_focus': 'Aging population'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a futuristic urban transportation system for a {t['city_type']} that addresses the environmental challenge of {t['environmental_challenge']} while focusing on the social aspect of {t['social_focus']}. Your response should include:

1. System Overview (250-300 words):
   a) Describe the key components and technologies of your transportation system.
   b) Explain how it integrates with existing infrastructure and addresses current urban challenges.
   c) Discuss how your system anticipates and adapts to future needs and technologies.

2. Environmental Impact and Adaptation (200-250 words):
   a) Explain how your system addresses the specified environmental challenge.
   b) Discuss the system's overall environmental impact, including energy use and emissions.
   c) Describe how the system could adapt to other potential environmental changes.

3. Social Implications (200-250 words):
   a) Analyze how your system addresses the specified social focus.
   b) Discuss potential impacts on urban demographics, employment, and social interactions.
   c) Explain how your system ensures equitable access and use across different social groups.

4. Implementation and Transition (150-200 words):
   a) Propose a phased approach for implementing your system over the next 20 years.
   b) Discuss potential challenges in adoption and how they might be overcome.
   c) Explain how existing transportation systems would be integrated or phased out.

5. Economic Analysis (150-200 words):
   a) Provide a high-level cost estimate for implementing your system.
   b) Discuss potential funding sources and economic models to support the system.
   c) Analyze the long-term economic impacts on the city and its residents.

6. Potential Risks and Mitigation (100-150 words):
   a) Identify at least two major risks or drawbacks of your proposed system.
   b) Suggest strategies to mitigate these risks.

7. Future Adaptations (100-150 words):
   a) Propose two potential future expansions or modifications to your system.
   b) Explain how these adaptations could address emerging urban challenges.

Ensure your response demonstrates a deep understanding of urban planning, transportation engineering, environmental science, and social dynamics. Be innovative in your approach while considering practical constraints and long-term sustainability.

Format your response with clear headings for each section (e.g., '1. System Overview', '2. Environmental Impact and Adaptation', etc.). Your total response should be between 1150-1500 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of urban planning, transportation engineering, and environmental science as applied to a {t['city_type']}",
            f"The proposed system effectively addresses the environmental challenge of {t['environmental_challenge']}",
            f"The social implications, particularly regarding {t['social_focus']}, are thoroughly analyzed",
            "The implementation plan and economic analysis are realistic and well-thought-out",
            "The response shows creativity and innovation while maintaining feasibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
