import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_variables = ['temperature', 'precipitation', 'sea level', 'atmospheric CO2']
        time_scales = ['decadal', 'centennial']
        regions = ['Arctic', 'Amazon rainforest', 'Great Barrier Reef', 'Sahel']
        complexity_principles = ['emergence', 'nonlinear dynamics', 'feedback loops', 'self-organization']
        
        tasks = {
            "1": {
                "climate_variable": random.choice(climate_variables),
                "time_scale": random.choice(time_scales),
                "region": random.choice(regions),
                "complexity_principle": random.choice(complexity_principles)
            },
            "2": {
                "climate_variable": random.choice(climate_variables),
                "time_scale": random.choice(time_scales),
                "region": random.choice(regions),
                "complexity_principle": random.choice(complexity_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models complex climate interactions and predicts long-term environmental changes for {t['climate_variable']} on a {t['time_scale']} scale in the {t['region']}, with a focus on the complexity principle of {t['complexity_principle']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI climate modeling system.
   b) Explain how your system incorporates principles from climate science, complex systems theory, and machine learning.
   c) Detail how your model represents and simulates {t['climate_variable']} changes in the {t['region']}.
   d) Explain how your model utilizes the complexity principle of {t['complexity_principle']}.

2. Data Integration and Processing (200-250 words):
   a) Describe the types of data your system would use and how it would acquire them.
   b) Explain how your system preprocesses and integrates diverse data sources.
   c) Discuss any novel approaches to handling the high dimensionality and heterogeneity of climate data.

3. Predictive Modeling (200-250 words):
   a) Explain the core algorithms or techniques your AI uses for {t['time_scale']} predictions of {t['climate_variable']}.
   b) Describe how your model accounts for uncertainties and variability in climate systems.
   c) Discuss how your approach differs from traditional climate models.

4. Complexity Analysis (200-250 words):
   a) Explain how your model captures the {t['complexity_principle']} in the context of {t['climate_variable']} in the {t['region']}.
   b) Describe any emergent properties or behaviors your model predicts.
   c) Discuss the challenges and opportunities of modeling complex climate systems using AI.

5. Validation and Uncertainty Quantification (150-200 words):
   a) Propose methods to validate your model's predictions against historical data and other models.
   b) Describe how your system quantifies and communicates uncertainties in its predictions.
   c) Discuss the limitations of your approach and potential areas for improvement.

6. Ethical Considerations and Implications (150-200 words):
   a) Discuss potential ethical implications of using AI for climate prediction and decision-making.
   b) Address issues such as model bias, data privacy, and the potential for misuse of climate predictions.
   c) Propose guidelines for the responsible development and use of AI in climate science.

Ensure your response demonstrates a deep understanding of climate science, complex systems theory, and artificial intelligence. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system for modeling {t['climate_variable']} on a {t['time_scale']} scale in the {t['region']}",
            f"The system architecture incorporates principles from climate science, complex systems theory, and machine learning",
            f"The model effectively utilizes the complexity principle of {t['complexity_principle']}",
            "The response includes a comprehensive discussion of data integration and processing for climate modeling",
            f"The predictive modeling approach is well-explained and suitable for {t['time_scale']} predictions",
            f"The complexity analysis effectively captures {t['complexity_principle']} in the context of {t['climate_variable']} in the {t['region']}",
            "The response includes appropriate methods for model validation and uncertainty quantification",
            "Ethical considerations and implications of using AI for climate prediction are thoroughly discussed",
            "The response demonstrates a deep understanding of climate science, complex systems theory, and artificial intelligence",
            "The ideas presented are innovative while maintaining scientific plausibility",
            "The response is well-structured with clear headings for each section",
            "The total response falls within the specified word count range of 1150-1450 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
