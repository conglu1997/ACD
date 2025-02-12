import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            'Technology',
            'Geopolitics',
            'Economics',
            'Social Movements',
            'Environmental Changes'
        ]
        time_periods = [
            '50 years',
            '100 years',
            '200 years'
        ]
        tasks = [
            {
                'domain': random.choice(domains),
                'time_period': random.choice(time_periods)
            },
            {
                'domain': random.choice(domains),
                'time_period': random.choice(time_periods)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes historical trends in the domain of {t['domain']} to predict potential future scenarios {t['time_period']} from now. Then, apply your system to a specific case study. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for analyzing historical trends and predicting future scenarios.
   b) Explain how your system integrates data from various sources and time periods.
   c) Detail the algorithms or methods used for pattern recognition and predictive modeling.
   d) Discuss how your system handles uncertainty and conflicting data.

2. Historical Analysis Framework (200-250 words):
   a) Explain how your system identifies and analyzes significant trends in the given domain.
   b) Describe the parameters and variables your system uses to evaluate historical events and their impact.
   c) Discuss how your system accounts for the interconnectedness of historical events across different domains.

3. Predictive Modeling (200-250 words):
   a) Detail how your system extrapolates historical trends to generate future scenarios.
   b) Explain the methods used to assess the probability and potential impact of predicted events.
   c) Describe how your system handles long-term predictions and accounts for potential paradigm shifts.

4. Case Study Application (250-300 words):
   a) Apply your AI system to a specific case study within the given domain.
   b) Provide a brief overview of the historical data your system would analyze.
   c) Present 2-3 potential future scenarios predicted by your system, including their likelihood and potential impact.
   d) Explain how these predictions could inform decision-making in the present.

5. Visualization and Reporting (150-200 words):
   a) Describe how your system would visualize historical trends and future predictions.
   b) Explain what types of reports or data representations your system would produce to communicate its findings effectively.
   c) Discuss how these visualizations could aid in understanding complex historical patterns and potential futures.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues related to using AI for historical analysis and future prediction.
   b) Discuss the limitations of your system and potential biases in its analysis or predictions.
   c) Propose guidelines for the responsible use of AI-generated future scenarios in decision-making processes.

7. Future Improvements (100-150 words):
   a) Suggest two potential enhancements to your AI system that could improve its accuracy or usefulness.
   b) Briefly describe how these improvements could advance our understanding of historical trends and future possibilities.

Ensure your response demonstrates a deep understanding of historical analysis, predictive modeling, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical analysis, predictive modeling, and artificial intelligence.",
            "The AI system design is innovative, plausible, and well-explained, integrating concepts from multiple disciplines.",
            "The case study application is detailed, relevant, and demonstrates the system's capability to generate insightful future scenarios.",
            "The response addresses ethical considerations and limitations of AI-driven historical analysis and future prediction.",
            "The proposed visualizations and improvements show a clear understanding of the challenges in communicating complex historical and predictive data.",
            "The response maintains a balance between creativity and scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
