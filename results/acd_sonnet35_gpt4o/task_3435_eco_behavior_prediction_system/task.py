import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            'climate change',
            'biodiversity loss',
            'water scarcity',
            'air pollution'
        ]
        data_sources = [
            'social media',
            'IoT sensors',
            'satellite imagery',
            'consumer purchase data'
        ]
        psychological_theories = [
            'Theory of Planned Behavior',
            'Social Cognitive Theory',
            'Value-Belief-Norm Theory',
            'Cognitive Dissonance Theory'
        ]
        intervention_methods = [
            'nudging',
            'gamification',
            'social norm messaging',
            'personalized feedback'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'environmental_issue': random.choice(environmental_issues),
                'data_source': random.choice(data_sources),
                'psychological_theory': random.choice(psychological_theories),
                'intervention_method': random.choice(intervention_methods)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that integrates environmental science, big data analytics, and social psychology to predict and influence pro-environmental behaviors on a large scale. Your system should focus on the environmental issue of {t['environmental_issue']}, primarily use {t['data_source']} as a data source, incorporate {t['psychological_theory']} in its behavioral model, and employ {t['intervention_method']} as its main intervention method.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the main components of your system and how they interact.
   b) Explain how your system integrates environmental science, data analytics, and social psychology.
   c) Detail the data collection, processing, and analysis pipeline.
   d) Discuss how your system ensures data privacy and security.

2. Predictive Model (250-300 words):
   a) Describe the machine learning or statistical models used to predict environmental behaviors.
   b) Explain how you incorporate {t['psychological_theory']} into your predictive model.
   c) Discuss how your model accounts for individual differences and contextual factors.
   d) Propose a method for validating and improving your model's accuracy over time.

3. Intervention Strategy (250-300 words):
   a) Detail how your system uses {t['intervention_method']} to influence pro-environmental behaviors.
   b) Explain how interventions are personalized based on individual user data and predictions.
   c) Describe how you measure the effectiveness of interventions.
   d) Discuss potential unintended consequences of your intervention strategy and how to mitigate them.

4. Environmental Impact Assessment (200-250 words):
   a) Propose a method for measuring the real-world impact of your system on {t['environmental_issue']}.
   b) Discuss potential challenges in attributing environmental changes to your system's interventions.
   c) Suggest how your system could adapt to changing environmental conditions or goals.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues related to data use, privacy, and behavioral influence.
   b) Discuss how your system balances individual autonomy with collective environmental benefits.
   c) Propose guidelines for the responsible development and use of behavior prediction and influence systems.
   d) Suggest a governance structure for overseeing the ethical operation of your system.

6. Scalability and Future Directions (150-200 words):
   a) Explain how your system could be scaled up to address multiple environmental issues simultaneously.
   b) Discuss potential challenges in adapting your system to different cultural or geographic contexts.
   c) Propose two novel features or extensions that could enhance your system's capabilities in the future.

Ensure your response demonstrates a deep understanding of environmental science, data analytics, and social psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively addresses the environmental issue of {t['environmental_issue']}.",
            f"The system appropriately utilizes {t['data_source']} as a primary data source.",
            f"The behavioral model convincingly incorporates {t['psychological_theory']}.",
            f"The intervention strategy effectively employs {t['intervention_method']}.",
            "The response demonstrates a deep understanding of environmental science, data analytics, and social psychology.",
            "The system design is innovative while maintaining scientific plausibility.",
            "The ethical considerations are thoroughly addressed and well-reasoned.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
