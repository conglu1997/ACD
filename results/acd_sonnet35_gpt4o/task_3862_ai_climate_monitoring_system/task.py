import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Arctic tundra",
            "Amazon rainforest",
            "Coral reef ecosystem",
            "Urban metropolis"
        ]
        climate_phenomena = [
            "Permafrost thawing",
            "Deforestation",
            "Ocean acidification",
            "Urban heat island effect"
        ]
        ai_techniques = [
            "Deep learning",
            "Reinforcement learning",
            "Federated learning",
            "Explainable AI"
        ]
        return {
            "1": {
                "environment": random.choice(environments),
                "phenomenon": random.choice(climate_phenomena),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "environment": random.choice(environments),
                "phenomenon": random.choice(climate_phenomena),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered climate monitoring system for the {t['environment']} that focuses on predicting and mitigating {t['phenomenon']} using {t['ai_technique']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI climate monitoring system.
   b) Explain how you integrate {t['ai_technique']} into your system design.
   c) Detail the data sources and sensors your system would use to monitor {t['phenomenon']}.
   d) Discuss how your system addresses the unique challenges of the {t['environment']}.

2. Data Processing and Analysis (250-300 words):
   a) Explain how your system collects and preprocesses data from various sources.
   b) Describe the AI algorithms and models used to analyze the data and predict {t['phenomenon']}.
   c) Discuss how you handle potential issues such as data quality, missing data, or sensor failures.

3. Prediction and Mitigation Strategies (250-300 words):
   a) Outline how your system predicts future trends related to {t['phenomenon']}.
   b) Propose mitigation strategies that your system could recommend or implement.
   c) Explain how {t['ai_technique']} enhances the prediction and mitigation capabilities of your system.

4. System Evaluation and Validation (200-250 words):
   a) Propose metrics to evaluate the performance and reliability of your AI climate monitoring system.
   b) Describe how you would validate the system's predictions and recommendations.
   c) Discuss potential limitations of your approach and how they might be addressed.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Identify potential ethical issues in developing and deploying your AI climate monitoring system.
   b) Discuss the broader societal implications of using AI for environmental monitoring and management.
   c) Propose guidelines for responsible development and use of AI in climate science.

Ensure your response demonstrates a deep understanding of artificial intelligence, climate science, and environmental systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI, climate science, and environmental systems.",
            "The system architecture is well-designed and integrates the specified AI technique effectively.",
            "The data processing and analysis approach is comprehensive and addresses potential challenges.",
            "The prediction and mitigation strategies are innovative and leverage the AI technique appropriately.",
            "The system evaluation and validation methods are well-thought-out and address potential limitations.",
            "Ethical considerations and societal impacts are thoroughly discussed.",
            "The response is within the specified word count range (1200-1450 words) and includes a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
