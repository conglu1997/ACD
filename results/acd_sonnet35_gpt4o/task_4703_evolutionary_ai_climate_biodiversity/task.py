import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'ecosystem': 'Coral Reefs',
                'climate_factor': 'Ocean Acidification',
                'time_frame': '50 years'
            },
            {
                'ecosystem': 'Amazon Rainforest',
                'climate_factor': 'Increased Drought Frequency',
                'time_frame': '30 years'
            },
            {
                'ecosystem': 'Arctic Tundra',
                'climate_factor': 'Permafrost Thawing',
                'time_frame': '75 years'
            },
            {
                'ecosystem': 'Great Barrier Reef',
                'climate_factor': 'Rising Sea Temperatures',
                'time_frame': '25 years'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that combines evolutionary algorithms and climate models to predict and mitigate the effects of climate change on global biodiversity. Focus on the {t['ecosystem']} ecosystem, considering the impact of {t['climate_factor']} over a {t['time_frame']} period.

Evolutionary algorithms are optimization techniques inspired by biological evolution, using mechanisms such as reproduction, mutation, recombination, and selection to find optimal solutions to complex problems.

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how evolutionary algorithms are integrated with climate models.
   c) Detail how your system models biodiversity and ecosystem dynamics.
   d) Discuss any novel technologies or theoretical concepts employed in your design.

2. Evolutionary Algorithm Design (250-300 words):
   a) Explain how your evolutionary algorithm models species adaptation and ecosystem changes.
   b) Describe the fitness function(s) used to evaluate potential solutions.
   c) Discuss how your algorithm handles the complexity and interdependencies within the ecosystem.

3. Climate Model Integration (200-250 words):
   a) Describe how your system incorporates and processes climate data.
   b) Explain how the climate model interacts with the evolutionary algorithm.
   c) Discuss any challenges in integrating climate projections with biodiversity modeling.

4. Biodiversity Impact Prediction (250-300 words):
   a) Explain how your system predicts changes in biodiversity over the specified time frame.
   b) Describe the key indicators or metrics used to assess biodiversity impact.
   c) Provide a hypothetical example of a prediction made by your system for the given scenario.

5. Mitigation Strategies (200-250 words):
   a) Describe how your system generates and evaluates potential mitigation strategies.
   b) Explain how these strategies are optimized for both effectiveness and feasibility.
   c) Discuss any ethical considerations in implementing these mitigation strategies.

6. Validation and Uncertainty (150-200 words):
   a) Propose methods to validate your system's predictions and recommendations.
   b) Discuss how your system quantifies and communicates uncertainty in its outputs.
   c) Suggest approaches for continually improving the system's accuracy over time.

7. Broader Implications (150-200 words):
   a) Discuss the potential impact of your system on conservation efforts and policy-making.
   b) Explore how this technology might be applied to other complex global challenges.
   c) Consider any potential unintended consequences of relying on AI for biodiversity conservation.

8. Glossary of Key Terms (100-150 words):
   Provide a brief glossary defining 5-7 key terms used in your response. These should be central concepts in your AI system or the domains involved.

Ensure your response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1600-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and climate science as applied to the {t['ecosystem']} ecosystem.",
            f"The system effectively integrates evolutionary algorithms with climate models to address {t['climate_factor']}.",
            f"The proposed AI system provides plausible predictions and mitigation strategies for biodiversity changes over a {t['time_frame']} period.",
            "The response includes innovative yet scientifically plausible approaches to modeling and preserving biodiversity.",
            "The submission addresses ethical considerations and potential broader implications of the proposed system.",
            "The glossary of key terms accurately defines important concepts used in the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
