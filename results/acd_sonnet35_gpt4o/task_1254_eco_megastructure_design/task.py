import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                'primary_challenge': 'Climate change mitigation',
                'secondary_challenge': 'Food security',
                'population_size': '1 million',
                'location': 'Floating ocean platform'
            },
            {
                'primary_challenge': 'Biodiversity conservation',
                'secondary_challenge': 'Sustainable energy production',
                'population_size': '500,000',
                'location': 'Arctic tundra'
            },
            {
                'primary_challenge': 'Water scarcity',
                'secondary_challenge': 'Waste management',
                'population_size': '2 million',
                'location': 'Desert'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(challenges, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a self-sustaining megastructure ecosystem that addresses the primary challenge of {t['primary_challenge']} and the secondary challenge of {t['secondary_challenge']} while accommodating a population of {t['population_size']} in a {t['location']} setting. Your response should include:

1. Architectural Design (250-300 words):
   a) Describe the overall structure and key components of your megastructure.
   b) Explain how the design addresses the specific challenges of the given location.
   c) Discuss how your structure accommodates the specified population size.
   d) Include a brief description of a visual representation or diagram of your megastructure.

2. Sustainability Systems (200-250 words):
   a) Detail the key systems that make your megastructure self-sustaining.
   b) Explain how these systems address the primary and secondary challenges.
   c) Describe any novel technologies or approaches used in these systems.
   d) Discuss how these systems interact and support each other.

3. Social and Cultural Considerations (200-250 words):
   a) Describe the social structure and governance system of your megastructure community.
   b) Explain how your design promotes social cohesion and cultural diversity.
   c) Discuss potential challenges in adapting to life in the megastructure and how you address them.
   d) Propose a unique cultural practice or tradition that might emerge in this community.

4. Environmental Impact and Integration (200-250 words):
   a) Analyze the environmental impact of your megastructure on its surroundings.
   b) Explain how your design integrates with and potentially benefits the local ecosystem.
   c) Discuss any potential negative impacts and how you mitigate them.
   d) Describe how your structure might evolve or adapt to long-term environmental changes.

5. Economic Model (150-200 words):
   a) Propose an economic system for your megastructure community.
   b) Explain how this system supports the structure's self-sustainability.
   c) Discuss how it addresses potential economic disparities within the population.
   d) Describe any unique economic opportunities or challenges presented by your design.

6. Scalability and Replication (150-200 words):
   a) Discuss the potential for scaling up your megastructure design.
   b) Explain how your model could be adapted to different environments or challenges.
   c) Propose a strategy for replicating your design in other parts of the world.
   d) Discuss any limitations or prerequisites for implementing your design globally.

7. Ethical Considerations and Future Implications (150-200 words):
   a) Identify and discuss at least two ethical issues raised by your megastructure design.
   b) Analyze potential long-term societal impacts of widespread adoption of your model.
   c) Propose guidelines for responsible development and governance of such megastructures.
   d) Speculate on how your design might influence the future of human habitation and development.

Ensure your response demonstrates a deep understanding of architecture, environmental science, sociology, and advanced technology. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility and addressing the specified challenges.

Format your response using clear headings for each section. Your total response should be between 1300-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of architecture, environmental science, sociology, and advanced technology.",
            "The megastructure design effectively addresses the primary and secondary challenges specified in the task.",
            "The design is creative and innovative while maintaining scientific plausibility.",
            "The response adequately covers all seven required sections with appropriate detail and within the specified word limits.",
            "The sustainability systems described are comprehensive and integrate well with each other.",
            "Social and cultural considerations are thoughtfully addressed, including potential challenges and adaptations.",
            "The environmental impact analysis is thorough and considers both positive and negative effects.",
            "The proposed economic model supports the structure's self-sustainability and addresses potential disparities.",
            "Scalability and replication potential are discussed with consideration for different environments.",
            "Ethical considerations and future implications are thoughtfully explored.",
            "The response uses technical terminology appropriately and provides clear explanations for complex concepts.",
            "The overall response demonstrates strong interdisciplinary knowledge integration, creative problem-solving, systems thinking, and long-term impact analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
