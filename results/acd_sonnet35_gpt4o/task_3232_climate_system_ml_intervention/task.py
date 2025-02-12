import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_components = [
            "Ocean circulation",
            "Atmospheric composition",
            "Cryosphere dynamics",
            "Terrestrial carbon cycle"
        ]
        intervention_types = [
            "Geoengineering",
            "Ecosystem restoration",
            "Emissions reduction",
            "Adaptive infrastructure"
        ]
        return {
            "1": {
                "climate_component": random.choice(climate_components),
                "intervention_type": random.choice(intervention_types)
            },
            "2": {
                "climate_component": random.choice(climate_components),
                "intervention_type": random.choice(intervention_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a machine learning system that models complex climate feedback loops and proposes targeted interventions to mitigate climate change, focusing on the climate component of {t['climate_component']} and the intervention type of {t['intervention_type']}. Then, analyze its potential impact and ethical implications. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your machine learning system for modeling climate feedback loops and proposing interventions.
   b) Explain how your system incorporates data from various sources to model {t['climate_component']}.
   c) Detail the algorithms or techniques used to identify potential {t['intervention_type']} interventions.
   d) Discuss how your system handles uncertainty and complexity in climate modeling.
   e) Include a high-level diagram or pseudocode snippet illustrating a key aspect of your system.

2. Climate Feedback Loop Modeling (250-300 words):
   a) Explain how your system models the complex feedback loops involving {t['climate_component']}.
   b) Describe the key variables and interactions considered in your model.
   c) Discuss how your system accounts for non-linear relationships and tipping points in the climate system.
   d) Provide an example of a specific feedback loop modeled by your system.

3. Intervention Proposal Process (250-300 words):
   a) Detail the step-by-step process your system uses to generate {t['intervention_type']} intervention proposals.
   b) Explain how the system evaluates the potential effectiveness and feasibility of proposed interventions.
   c) Describe how your system prioritizes interventions based on their potential impact and associated risks.
   d) Provide an example of a specific intervention your system might propose for {t['climate_component']}.

4. Impact Analysis (200-250 words):
   a) Analyze the potential short-term and long-term impacts of implementing the proposed interventions.
   b) Discuss any potential unintended consequences or cascading effects on other parts of the climate system.
   c) Explain how your system models the global impact of localized interventions.

5. Ethical Implications (200-250 words):
   a) Identify and discuss the key ethical considerations related to using AI for climate intervention planning.
   b) Address issues of global equity, intergenerational justice, and potential conflicts of interest.
   c) Propose guidelines for the responsible development and use of such systems in climate policy-making.

6. Validation and Uncertainty (150-200 words):
   a) Describe methods to validate your system's models and intervention proposals.
   b) Explain how your system communicates uncertainty and confidence levels in its predictions and recommendations.
   c) Discuss the limitations of your approach and potential areas for improvement.

Ensure your response demonstrates a deep understanding of climate science, complex systems theory, machine learning, and environmental ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of climate science, complex systems theory, and machine learning.",
            f"The system effectively models the climate component of {t['climate_component']} and proposes relevant {t['intervention_type']} interventions.",
            "The explanation of climate feedback loop modeling is thorough and scientifically sound.",
            "The intervention proposal process is well-defined and considers multiple factors.",
            "The impact analysis and ethical implications are thoughtfully addressed.",
            "The response is well-structured, coherent, and demonstrates creative problem-solving within the constraints of scientific plausibility and ethical responsibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
