import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_factors = [
            {'factor': 'Rising sea levels', 'region': 'Coastal areas'},
            {'factor': 'Increased frequency of heatwaves', 'region': 'Urban centers'},
            {'factor': 'Shifting precipitation patterns', 'region': 'Agricultural regions'},
            {'factor': 'Melting permafrost', 'region': 'Arctic ecosystems'}
        ]
        return {str(i+1): factor for i, factor in enumerate(random.sample(climate_factors, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for modeling and mitigating the cascading effects of climate change, focusing on the climate factor '{t['factor']}' in {t['region']}. Your system should integrate complex systems theory and machine learning techniques to predict and address the interconnected impacts on ecosystems, economies, and societies.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling climate change cascades.
   b) Explain how your system incorporates complex systems theory and machine learning.
   c) Detail how the system models the interactions between environmental, economic, and social factors.
   d) Discuss any novel approaches in your design for handling the complexity and uncertainty of climate change impacts.

2. Data Integration and Processing (250-300 words):
   a) Identify the types of data your system would use (e.g., climate models, economic indicators, social metrics).
   b) Explain how your system would integrate and process diverse data sources.
   c) Describe any data preprocessing or augmentation techniques used to enhance model performance.
   d) Discuss how your system handles data uncertainty and gaps in climate science knowledge.

3. Predictive Modeling and Simulation (250-300 words):
   a) Explain the machine learning techniques your system uses for predictive modeling.
   b) Describe how your system simulates cascading effects across different domains (e.g., from environmental changes to economic and social impacts).
   c) Discuss how the system accounts for feedback loops and non-linear interactions in climate systems.
   d) Provide an example of how your system might model the cascading effects of {t['factor']} in {t['region']}.

4. Mitigation Strategy Generation (200-250 words):
   a) Describe how your AI system generates and evaluates potential mitigation strategies.
   b) Explain how the system balances short-term and long-term impacts in strategy development.
   c) Discuss how your system incorporates adaptive management principles for ongoing strategy refinement.

5. Visualization and Decision Support (150-200 words):
   a) Explain how your system presents complex climate cascade models to decision-makers.
   b) Describe any interactive features that allow users to explore different scenarios or mitigation strategies.
   c) Discuss how the system communicates uncertainty and confidence levels in its predictions and recommendations.

6. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues in using AI for climate change modeling and mitigation planning.
   b) Discuss how your system addresses issues of equity and environmental justice in its modeling and recommendations.
   c) Explain any limitations of your approach and areas where human expertise is still crucial.

7. Interdisciplinary Impact and Future Directions (150-200 words):
   a) Discuss how your AI system could contribute to advancing climate science and complex systems theory.
   b) Propose a novel research question that your system could help address in the field of climate change adaptation.
   c) Suggest potential applications of your system beyond climate change modeling.

Ensure your response demonstrates a deep understanding of climate science, complex systems theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing the multifaceted nature of climate change impacts.

Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, complex systems theory, and artificial intelligence.",
            "The AI system design is innovative yet scientifically plausible.",
            "The system effectively integrates complex systems theory and machine learning techniques.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "The proposed system adequately models and addresses the cascading effects of the specified climate factor in the given region.",
            "Ethical considerations and limitations are thoughtfully discussed.",
            "The interdisciplinary impact and future directions are insightfully explored."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
