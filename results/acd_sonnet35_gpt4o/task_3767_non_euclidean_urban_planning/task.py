import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'geometry_type': 'Hyperbolic',
                'urban_challenge': 'Traffic congestion',
                'city_feature': 'Road network'
            },
            {
                'geometry_type': 'Spherical',
                'urban_challenge': 'Green space optimization',
                'city_feature': 'Parks and recreational areas'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an urban planning system based on {t['geometry_type']} geometry and apply it to address the urban challenge of {t['urban_challenge']} by reimagining the city's {t['city_feature']}. Your response should include the following sections:

1. Geometric Framework (200-250 words):
   a) Explain the key principles of {t['geometry_type']} geometry and how they differ from Euclidean geometry.
   b) Describe how these principles can be applied to urban planning, particularly for {t['city_feature']}.
   c) Provide a visual description of how space would be perceived in this geometric system.

2. Urban Planning System Design (250-300 words):
   a) Outline the core components of your urban planning system based on {t['geometry_type']} geometry.
   b) Explain how your system incorporates the unique properties of this geometry into urban design principles.
   c) Describe any novel tools or methods your system would use for city planning and development.

3. Application to {t['urban_challenge']} (250-300 words):
   a) Analyze how your {t['geometry_type']}-based system could address {t['urban_challenge']}.
   b) Provide a specific example of how {t['city_feature']} would be designed or modified using your system.
   c) Compare the potential benefits and drawbacks of your approach to traditional Euclidean-based urban planning.

4. Mathematical Modeling (250-300 words):
   a) Present a mathematical model that represents a key aspect of your urban planning system.
   b) Include at least one equation or formula that incorporates principles of {t['geometry_type']} geometry.
   c) Explain the variables, constants, and relationships in your model.
   d) Describe how this model could be used to make predictions or optimize city design.

5. Practical Implementation (200-250 words):
   a) Discuss the challenges of implementing your non-Euclidean urban planning system in the real world.
   b) Propose methods for translating designs from your geometric system into constructable plans.
   c) Suggest technologies or tools that could aid in the visualization and implementation of your system.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how your {t['geometry_type']}-based urban planning system might impact other fields (e.g., psychology, economics, or environmental science).
   b) Discuss potential societal or cultural implications of living in a city designed with non-Euclidean principles.

Ensure your response demonstrates a deep understanding of both {t['geometry_type']} geometry and urban planning principles. Use appropriate mathematical and urban planning terminology, and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section, numbered as above. Begin each section on a new line. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear and accurate understanding of {t['geometry_type']} geometry and its principles.",
            f"The urban planning system effectively and creatively incorporates {t['geometry_type']} geometric principles into its design.",
            f"The proposed solution addresses the challenge of {t['urban_challenge']} in an innovative and plausible manner, specifically focusing on {t['city_feature']}.",
            f"The mathematical model presented is relevant, correctly applies {t['geometry_type']} geometric concepts to urban planning, and includes at least one appropriate equation or formula.",
            "The response considers practical implementation challenges and proposes realistic solutions, including specific technologies or tools.",
            "The interdisciplinary implications are thoughtfully explored and logically derived from the proposed system.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary thinking while adhering to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
