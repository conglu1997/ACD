class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "population": 50000,
                "area": 5,  # square kilometers
                "climate": "arid",
                "energy_source": "solar",
                "social_focus": "intergenerational interaction"
            },
            "2": {
                "population": 100000,
                "area": 8,  # square kilometers
                "climate": "tropical",
                "energy_source": "fusion",
                "social_focus": "cultural diversity"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a futuristic city district for the year 2150 that maximizes sustainability, social cohesion, and technological integration while adhering to the following constraints:

- Population: {t['population']} people
- Area: {t['area']} square kilometers
- Climate: {t['climate']}
- Primary energy source: {t['energy_source']}
- Social focus: {t['social_focus']}

Your response should include:

1. District Layout (200-250 words):
   Describe the overall layout of your district, including major zones, transportation systems, and key infrastructure. Explain how your design promotes sustainability and social interaction.

2. Housing Solution (150-200 words):
   Detail your approach to housing, considering density, design, and integration with other district elements. Explain how your housing solution addresses sustainability and social needs.

3. Energy and Resource Management (150-200 words):
   Describe your strategies for energy production, distribution, and conservation. Include your approach to water management and waste reduction.

4. Social and Cultural Integration (150-200 words):
   Explain how your district design promotes the specified social focus. Describe specific features or programs that enhance community interaction and cultural expression.

5. Technological Innovation (150-200 words):
   Describe at least two innovative technologies integrated into your district design. Explain how these technologies contribute to sustainability, quality of life, or social cohesion.

6. Environmental Adaptation (100-150 words):
   Explain how your design is tailored to the specified climate, including strategies for climate resilience and environmental protection.

7. Challenges and Solutions (100-150 words):
   Identify two potential challenges in implementing your design and propose solutions to address them.

Ensure your response demonstrates a deep understanding of urban planning, environmental science, sociology, and futuristic technology. Be creative in your approach while maintaining plausibility and addressing all specified constraints.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design effectively addresses all specified constraints (population, area, climate, energy source, and social focus).",
            "The response demonstrates a strong understanding of urban planning, environmental science, sociology, and futuristic technology.",
            "The district layout and features are innovative, well-integrated, and promote sustainability and social cohesion.",
            "The proposed solutions for housing, energy, and resource management are detailed and appropriate for the given constraints.",
            "The design includes plausible and creative technological innovations that enhance the district's functionality.",
            "The response adequately addresses potential challenges and proposes reasonable solutions.",
            "The overall design is cohesive, demonstrating systems thinking and balancing multiple objectives effectively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
