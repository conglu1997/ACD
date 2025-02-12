import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ecosystem": "Coral Reef",
                "environmental_challenge": "Ocean Acidification",
                "region": "Great Barrier Reef, Australia",
                "timeframe": "2023-2050"
            },
            {
                "ecosystem": "Tropical Rainforest",
                "environmental_challenge": "Deforestation",
                "region": "Amazon Basin, South America",
                "timeframe": "2023-2050"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a comprehensive AI-driven environmental monitoring and policy recommendation system for the {t['ecosystem']} ecosystem, focusing on the challenge of {t['environmental_challenge']} in the {t['region']} for the period {t['timeframe']}. Your system should integrate real-time data analysis with predictive modeling to inform adaptive environmental policies. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI-driven environmental monitoring and policy recommendation system.
   b) Explain how your system integrates data collection, analysis, and policy recommendation components.
   c) Detail how the system incorporates real-time data and predictive modeling.
   d) Discuss how your system ensures adaptability to changing environmental conditions.

2. Data Collection and Analysis (250-300 words):
   a) Specify the types of data your system will collect and analyze.
   b) Describe the technologies and methodologies used for data collection.
   c) Explain your approach to data preprocessing, integration, and quality assurance.
   d) Discuss how your system handles big data challenges and ensures real-time processing capabilities.

3. Predictive Modeling (250-300 words):
   a) Describe the predictive modeling techniques your system employs.
   b) Explain how these models forecast future environmental trends and policy impacts.
   c) Discuss how your system handles uncertainty and validates model predictions.
   d) Describe how the system integrates multiple models to provide comprehensive insights.

4. Policy Recommendation Engine (250-300 words):
   a) Explain how your system translates data insights into policy recommendations.
   b) Describe the criteria your system uses to evaluate and prioritize policy options.
   c) Discuss how the system accounts for socio-economic factors and stakeholder interests.
   d) Explain how your system ensures transparency and interpretability in its recommendations.

5. Implementation and Scalability (200-250 words):
   a) Outline the key steps for implementing your system in the specified region.
   b) Discuss potential challenges in deployment and propose solutions.
   c) Explain how your system could be scaled or adapted to other ecosystems or environmental challenges.

6. Ethical Considerations and Governance (200-250 words):
   a) Identify potential ethical issues related to your system's data collection and policy recommendations.
   b) Propose governance structures to ensure responsible use of the system.
   c) Discuss how your system balances environmental protection with other societal needs.

7. Evaluation and Continuous Improvement (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system.
   b) Describe how your system incorporates feedback and learns from outcomes.
   c) Suggest approaches for continuous improvement and adaptation of the system.

Ensure your response demonstrates a deep understanding of environmental science, data analytics, machine learning, and policy-making processes. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical feasibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            "The proposed system demonstrates integration of environmental science, data analytics, and policy-making",
            "The solution is innovative yet scientifically and practically feasible",
            "The response shows a deep understanding of the specific ecosystem and environmental challenge",
            "The system design incorporates real-time data analysis and predictive modeling effectively",
            "The response adequately addresses ethical considerations and governance issues",
            "The proposed evaluation and improvement methods are well-thought-out and practical"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
