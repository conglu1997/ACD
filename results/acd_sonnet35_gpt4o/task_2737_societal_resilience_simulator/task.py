import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        disruption_types = [
            "Natural disaster",
            "Economic crisis",
            "Pandemic",
            "Social unrest",
            "Technological disruption"
        ]
        societal_factors = [
            "Economic inequality",
            "Social cohesion",
            "Healthcare access",
            "Education level",
            "Environmental quality",
            "Technological infrastructure",
            "Governance effectiveness"
        ]
        community_types = [
            "Urban metropolis",
            "Rural agricultural region",
            "Coastal tourist destination",
            "Industrial manufacturing hub",
            "Tech-centric innovation cluster"
        ]
        return {
            "1": {
                "disruption": random.choice(disruption_types),
                "primary_factor": random.choice(societal_factors),
                "community": random.choice(community_types)
            },
            "2": {
                "disruption": random.choice(disruption_types),
                "primary_factor": random.choice(societal_factors),
                "community": random.choice(community_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational system that simulates societal resilience in the face of a {t['disruption']}, with a focus on the impact of {t['primary_factor']} in a {t['community']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your societal resilience simulation system.
   b) Explain how your system models the interactions between various societal factors.
   c) Detail how your system incorporates data from different domains (economic, social, environmental).
   d) Propose a novel feature that enhances the system's predictive capabilities.

2. Modeling Approach (200-250 words):
   a) Explain the mathematical or computational techniques used to model complex societal interactions.
   b) Describe how your system accounts for feedback loops and emergent behaviors in social systems.
   c) Discuss how uncertainty and variability are handled in your model.

3. Data Integration and Analysis (200-250 words):
   a) Outline the types of data your system would use and how it would be collected or generated.
   b) Explain how your system integrates and analyzes data from diverse sources.
   c) Describe any machine learning or AI techniques used for pattern recognition or prediction.

4. Simulation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system simulates the impact of the specified disruption.
   b) Explain how the system assesses and quantifies societal resilience.
   c) Describe how the simulation accounts for the specific characteristics of the given community type.

5. Predictive Insights and Applications (200-250 words):
   a) Describe two specific predictions or insights your system might generate about societal resilience.
   b) Explain how these insights could be used to enhance community adaptability and resilience.
   c) Discuss potential applications of your system in policy-making or urban planning.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss ethical implications of using such a system for societal modeling and decision-making.
   b) Address potential biases in your model and how they might be mitigated.
   c) Identify limitations of your approach and areas for future improvement.

Ensure your response demonstrates a deep understanding of complex systems modeling, social sciences, and data analysis. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and addressing real-world complexities.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specified disruption type: {t['disruption']}.",
            f"The system should focus on the impact of {t['primary_factor']} as a key societal factor.",
            f"The simulation must be tailored to the specific community type: {t['community']}.",
            "The response should include all six required sections: System Architecture, Modeling Approach, Data Integration and Analysis, Simulation Process, Predictive Insights and Applications, and Ethical Considerations and Limitations.",
            "The system design must demonstrate a deep understanding of complex systems modeling and its application to societal resilience.",
            "The response should show interdisciplinary knowledge integration, combining insights from social sciences, economics, and data science.",
            "The proposed system should include innovative features or approaches while maintaining scientific plausibility.",
            "The ethical considerations should be thoughtfully addressed, including potential biases and limitations of the approach.",
            "The response should be well-structured, clear, and demonstrate a high level of expertise in the subject matter."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
