import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_events = [
            'Heatwave',
            'Flood',
            'Drought',
            'Wildfire',
            'Hurricane'
        ]
        psychological_theories = [
            'Theory of Planned Behavior',
            'Social Cognitive Theory',
            'Protection Motivation Theory',
            'Value-Belief-Norm Theory',
            'Construal Level Theory'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'climate_event': random.choice(climate_events),
                'psychological_theory': random.choice(psychological_theories)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a predictive model that integrates climate data, social media trends, and psychological theories to forecast human behavior in response to climate change events. Focus on the climate event of {t['climate_event']} and incorporate the {t['psychological_theory']} in your model. Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the key components of your predictive model and how they interact.
   b) Explain how your model integrates climate data, social media trends, and psychological theories.
   c) Detail how your model specifically incorporates {t['psychological_theory']} in predicting behavior during a {t['climate_event']}.
   d) Propose a novel feature that enhances your model's predictive accuracy.

2. Data Integration and Analysis (250-300 words):
   a) Describe the types of climate data your model would use and how it would be processed.
   b) Explain your approach to analyzing social media trends related to climate change and {t['climate_event']}.
   c) Discuss how you would quantify psychological factors based on {t['psychological_theory']}.
   d) Propose a method for combining these diverse data sources in your predictive model.

3. Behavior Prediction Process (200-250 words):
   a) Outline the step-by-step process your model uses to generate behavior predictions.
   b) Explain how your model accounts for individual differences and cultural factors.
   c) Describe how your model handles uncertainty and conflicting data inputs.

4. Model Validation and Accuracy (200-250 words):
   a) Propose methods for validating your model's predictions against real-world behavior.
   b) Discuss potential challenges in measuring the accuracy of your model.
   c) Suggest approaches for continuously improving your model's predictive power.

5. Ethical Considerations and Safeguards (200-250 words):
   a) Identify potential ethical issues arising from the use of your predictive model.
   b) Discuss privacy concerns related to the use of social media data and propose safeguards.
   c) Explore potential misuses of your model and suggest preventive measures.
   d) Propose guidelines for the responsible development and application of climate behavior prediction models.

6. Practical Applications and Implications (150-200 words):
   a) Suggest potential applications of your model in climate change mitigation and adaptation strategies.
   b) Discuss how your model could inform public policy and disaster preparedness.
   c) Explore potential impacts on climate change communication and public engagement.

Ensure your response demonstrates a deep understanding of climate science, social psychology, and data analytics. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and ethical considerations.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, social psychology, and data analytics.",
            f"The model effectively incorporates {t['psychological_theory']} in predicting behavior during a {t['climate_event']}.",
            "The proposed model presents a novel and plausible approach to integrating diverse data sources for behavior prediction.",
            "The ethical considerations and safeguards are thoroughly addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
