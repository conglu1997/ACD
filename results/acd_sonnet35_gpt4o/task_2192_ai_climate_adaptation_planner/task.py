import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_challenges = [
            {
                "challenge": "Sea level rise",
                "region": "Coastal cities",
                "time_frame": "50 years"
            },
            {
                "challenge": "Extreme heat waves",
                "region": "Urban areas in arid climates",
                "time_frame": "30 years"
            }
        ]
        return {
            "1": climate_challenges[0],
            "2": climate_challenges[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for climate prediction and adaptation planning, focusing on the challenge of {t['challenge']} in {t['region']} over the next {t['time_frame']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for climate prediction and adaptation planning.
   b) Explain how your system integrates climate models, machine learning algorithms, and policy analysis tools.
   c) Discuss how your system handles uncertainty and incorporates feedback loops between predictions and adaptation strategies.

2. Data Integration and Processing (200-250 words):
   a) Identify the types of data your system would use for climate prediction and adaptation planning.
   b) Explain how your system would integrate and process data from diverse sources (e.g., satellite imagery, weather stations, socioeconomic indicators).
   c) Describe how your system would handle data quality issues, missing data, and conflicting information.

3. Machine Learning Approach (200-250 words):
   a) Propose a specific machine learning approach for predicting {t['challenge']} in {t['region']}.
   b) Explain how your approach would improve upon traditional climate modeling techniques.
   c) Discuss how your system would adapt its predictions over time as new data becomes available.

4. Adaptation Strategy Generation (200-250 words):
   a) Describe how your AI system would generate adaptation strategies for {t['challenge']} in {t['region']}.
   b) Explain how the system would evaluate and prioritize different adaptation options.
   c) Discuss how your system would account for socioeconomic factors and potential unintended consequences of adaptation strategies.

5. Ethical Considerations and Stakeholder Engagement (150-200 words):
   a) Discuss potential ethical issues in using AI for climate adaptation planning.
   b) Propose methods for incorporating local knowledge and stakeholder input into your system.
   c) Explain how your system would address potential biases in data or algorithms that could lead to inequitable adaptation strategies.

6. Implementation and Scalability (150-200 words):
   a) Outline a plan for implementing your AI system in {t['region']}.
   b) Discuss how your system could be scaled or adapted to address other climate challenges or regions.
   c) Identify potential barriers to implementation and propose solutions.

7. Evaluation and Monitoring (100-150 words):
   a) Propose metrics for evaluating the performance and impact of your AI system.
   b) Describe how you would monitor and validate the system's predictions and adaptation strategies over time.
   c) Suggest a method for continually improving the system based on its performance and changing conditions.

Ensure your response demonstrates a deep understanding of climate science, artificial intelligence, and policy planning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of climate science, particularly related to {t['challenge']} in {t['region']}.",
            "The proposed AI system integrates climate models, machine learning, and policy analysis in a novel and plausible way.",
            "The approach to data integration and processing is comprehensive and addresses real-world challenges.",
            "The machine learning approach is well-explained and offers clear advantages over traditional methods.",
            "The system for generating and evaluating adaptation strategies is well-thought-out and considers multiple factors.",
            "Ethical considerations and stakeholder engagement are thoroughly addressed.",
            "The implementation plan and scalability discussion are realistic and consider potential barriers.",
            "The evaluation and monitoring approach is well-designed and allows for continual improvement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
