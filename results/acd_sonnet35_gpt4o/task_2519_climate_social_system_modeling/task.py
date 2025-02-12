import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "climate_factor": "Sea level rise",
                "social_factor": "Urban migration",
                "economic_factor": "Coastal property values"
            },
            {
                "climate_factor": "Increased frequency of heatwaves",
                "social_factor": "Public health behaviors",
                "economic_factor": "Energy consumption patterns"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a complex system model that integrates climate science, social psychology, and economics to predict and mitigate the effects of climate change on human behavior and societal structures. Focus on the following scenario:\n\nClimate factor: {t['climate_factor']}\nSocial factor: {t['social_factor']}\nEconomic factor: {t['economic_factor']}\n\nYour response should include:\n\n1. Model Architecture (250-300 words):\n   a) Describe the key components of your complex system model.\n   b) Explain how you integrate climate science, social psychology, and economics in your design.\n   c) Detail how your model incorporates feedback loops and non-linear interactions between components.\n   d) Include a high-level diagram or flowchart of your model architecture (describe this textually).\n\n2. Data Integration and Analysis (200-250 words):\n   a) Explain how your model would integrate and analyze data from different disciplines.\n   b) Describe any novel algorithms or techniques you've developed for interdisciplinary data synthesis.\n   c) Discuss how your model handles uncertainties and variabilities in the data.\n\n3. Predictive Capabilities (200-250 words):\n   a) Outline the specific predictions your model can make about the given scenario.\n   b) Explain how your model accounts for both short-term and long-term effects.\n   c) Describe how your model handles potential tipping points or critical thresholds in the system.\n\n4. Mitigation Strategies (200-250 words):\n   a) Propose three potential mitigation strategies based on your model's predictions.\n   b) Explain how each strategy addresses the interconnected climate, social, and economic factors.\n   c) Discuss potential unintended consequences of each mitigation strategy.\n\n5. Model Validation and Improvement (150-200 words):\n   a) Suggest methods to validate your model's predictions and effectiveness.\n   b) Describe how you would incorporate new data or feedback to improve the model over time.\n   c) Discuss any limitations of your current design and how they might be addressed.\n\n6. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues related to using your model for decision-making.\n   b) Discuss how your model addresses issues of equity and environmental justice.\n   c) Propose guidelines for the responsible use of your model in policy-making.\n\nEnsure your response demonstrates a deep understanding of climate science, social psychology, economics, and complex systems theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1150-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, social psychology, economics, and complex systems theory.",
            "The model architecture effectively integrates multiple disciplines and incorporates feedback loops and non-linear interactions.",
            "The predictive capabilities and mitigation strategies are well-reasoned and address the specific scenario provided.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "Ethical considerations and guidelines for responsible use are thoughtfully addressed.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
