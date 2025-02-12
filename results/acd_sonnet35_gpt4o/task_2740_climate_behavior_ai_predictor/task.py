import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        behaviors = [
            "reducing energy consumption",
            "adopting plant-based diets",
            "using sustainable transportation",
            "supporting renewable energy initiatives",
            "reducing single-use plastics"
        ]
        psychological_theories = [
            "Theory of Planned Behavior",
            "Social Cognitive Theory",
            "Transtheoretical Model",
            "Nudge Theory",
            "Value-Belief-Norm Theory"
        ]
        climate_factors = [
            "temperature anomalies",
            "extreme weather events",
            "sea level rise",
            "air quality index",
            "biodiversity loss metrics"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "behavior": random.choice(behaviors),
                "psychological_theory": random.choice(psychological_theories),
                "climate_factor": random.choice(climate_factors)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that predicts and influences climate-friendly behaviors by integrating climate science models, behavioral psychology theories, and machine learning algorithms. Your system should focus on the behavior of {t['behavior']}, incorporate the psychological theory of {t['psychological_theory']}, and consider the climate factor of {t['climate_factor']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system.
   b) Explain how it integrates climate science models, behavioral psychology theories, and machine learning algorithms.
   c) Detail how the system processes and analyzes data from various sources.
   d) Include a high-level diagram of your system architecture (describe it in words).
   e) Provide a brief pseudocode or code snippet illustrating a key component of your system.

2. Behavior Prediction Model (250-300 words):
   a) Explain how your system predicts the likelihood of individuals engaging in {t['behavior']}.
   b) Describe how you incorporate {t['psychological_theory']} into your prediction model.
   c) Discuss how {t['climate_factor']} is used as an input or influencing factor in your model.
   d) Provide a quantitative estimate of your model's predicted effectiveness in changing behavior.

3. Behavior Influence Strategies (200-250 words):
   a) Propose three strategies your system would use to encourage {t['behavior']}.
   b) Explain how these strategies are informed by {t['psychological_theory']}.
   c) Describe how your system would adapt its strategies based on changes in {t['climate_factor']}.

4. Data Sources and Privacy (150-200 words):
   a) Identify the types of data your system would need to function effectively.
   b) Discuss potential sources for this data, such as smart home devices, social media, or government databases.
   c) Address privacy concerns and propose ethical guidelines for data collection and use.

5. Evaluation Metrics (150-200 words):
   a) Propose 3-4 specific metrics to evaluate the performance of your AI system.
   b) Explain how each metric assesses the system's ability to predict and influence behavior.
   c) Describe how you would measure the system's impact on {t['climate_factor']}.
   d) Provide an example of a quantitative goal for one of your metrics.

6. Challenges and Limitations (150-200 words):
   a) Identify potential challenges in implementing your system.
   b) Discuss any limitations of your approach.
   c) Propose solutions or areas for future research to address these issues.

7. Societal Implications (150-200 words):
   a) Discuss the potential societal impacts of widespread use of your system.
   b) Address any ethical concerns related to behavior prediction and influence.
   c) Propose guidelines for responsible development and use of climate behavior AI systems.

Ensure your response demonstrates a deep understanding of climate science, behavioral psychology, and AI technologies. Be creative in your approach while maintaining scientific plausibility and ethical considerations. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should describe an AI system that predicts and influences the behavior of {t['behavior']}.",
            f"The system should incorporate {t['psychological_theory']} in its behavior prediction model.",
            f"The system should consider {t['climate_factor']} as an input or influencing factor.",
            "The response should include all seven required sections with appropriate content for each.",
            "The design should demonstrate integration of climate science, behavioral psychology, and AI technologies.",
            "The response should address ethical considerations and propose guidelines for responsible use.",
            "The response should be creative while maintaining scientific plausibility.",
            "The response should include a brief pseudocode or code snippet for a key component of the system.",
            "The response should provide quantitative estimates or predictions where appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
