import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            {'challenge': 'Water management', 'description': 'Efficient collection, distribution, and recycling of water resources'},
            {'challenge': 'Energy efficiency', 'description': 'Reducing energy consumption and increasing renewable energy use'},
            {'challenge': 'Waste reduction', 'description': 'Minimizing waste production and improving recycling systems'},
            {'challenge': 'Air quality improvement', 'description': 'Reducing air pollution and enhancing air purification'}
        ]
        biological_systems = [
            {'system': 'Plant vascular systems', 'description': 'Networks for resource distribution in plants'},
            {'system': 'Termite mounds', 'description': 'Natural ventilation and temperature regulation'},
            {'system': 'Mycorrhizal networks', 'description': 'Underground fungal networks for nutrient sharing'},
            {'system': 'Lotus leaf surface', 'description': 'Self-cleaning and water-repellent properties'}
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'urban_challenge': random.choice(urban_challenges),
                'biological_system': random.choice(biological_systems)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an urban solution inspired by biomimicry to address the challenge of {t['urban_challenge']['challenge']} ({t['urban_challenge']['description']}) using principles derived from the biological system of {t['biological_system']['system']} ({t['biological_system']['description']}). Your response should include:

1. Biological System Analysis (200-250 words):
   a) Describe the key features and functions of the {t['biological_system']['system']}.
   b) Explain how this biological system efficiently solves problems or manages resources.
   c) Identify the core principles or mechanisms that could be applied to urban design.

2. Urban Challenge Analysis (200-250 words):
   a) Analyze the specific urban challenge of {t['urban_challenge']['challenge']}.
   b) Discuss current approaches to this challenge and their limitations.
   c) Explain why a biomimetic approach could be beneficial for addressing this challenge.

3. Biomimetic Solution Design (300-350 words):
   a) Propose a detailed urban design solution that applies principles from the {t['biological_system']['system']} to address {t['urban_challenge']['challenge']}.
   b) Explain how your solution mimics or is inspired by the biological system.
   c) Describe the key components and functioning of your proposed solution.
   d) Discuss how your solution improves upon current approaches to the urban challenge.

4. Implementation and Scalability (200-250 words):
   a) Outline a plan for implementing your biomimetic solution in a real urban environment.
   b) Discuss potential challenges in implementation and how they might be overcome.
   c) Explain how your solution could be scaled up or adapted for different urban contexts.

5. Environmental Impact Assessment (150-200 words):
   a) Analyze the potential environmental impacts (positive and negative) of your proposed solution.
   b) Compare the ecological footprint of your solution to conventional approaches.
   c) Suggest ways to mitigate any potential negative environmental effects.

6. Interdisciplinary Collaboration (150-200 words):
   a) Identify the key disciplines and experts needed to develop and implement your solution.
   b) Explain how these different fields would need to collaborate.
   c) Discuss potential challenges in interdisciplinary work and how to address them.

Ensure your response demonstrates a deep understanding of both the biological system and the urban challenge. Be creative in your biomimetic approach while maintaining scientific plausibility and addressing practical considerations of urban design. Use appropriate terminology from biology, urban planning, and environmental science.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['biological_system']['system']} and its potential applications to urban design.",
            f"The proposed solution effectively addresses the urban challenge of {t['urban_challenge']['challenge']}.",
            "The biomimetic approach is creative, well-explained, and scientifically plausible.",
            "The implementation plan and scalability discussion are practical and well-considered.",
            "The environmental impact assessment is thorough and balanced.",
            "The interdisciplinary collaboration section identifies relevant fields and addresses potential challenges.",
            "The response demonstrates integration of knowledge from biology, urban planning, and environmental science.",
            "The proposed solution is innovative and improves upon current approaches to the urban challenge.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
