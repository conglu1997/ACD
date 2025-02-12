import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            'water management',
            'energy efficiency',
            'waste reduction',
            'air quality improvement',
            'sustainable transportation',
            'urban heat island mitigation',
            'biodiversity conservation',
            'food production',
            'noise pollution reduction',
            'disaster resilience'
        ]
        
        natural_inspirations = [
            'plant structures',
            'animal behaviors',
            'ecosystem processes',
            'microbial communities',
            'geological formations'
        ]
        
        task1 = {
            'challenge': random.choice(urban_challenges),
            'inspiration': random.choice(natural_inspirations)
        }
        
        task2 = {
            'challenge': random.choice(urban_challenges),
            'inspiration': random.choice(natural_inspirations)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic solution for the urban planning challenge of {t['challenge']}, drawing inspiration from {t['inspiration']}. Your task is to:

1. Natural System Analysis (200-250 words):
   a) Describe the key features and mechanisms of the {t['inspiration']} that are relevant to addressing {t['challenge']}.
   b) Explain how these natural systems or processes efficiently solve similar problems in nature.

2. Biomimetic Solution Design (250-300 words):
   a) Propose an innovative urban planning solution that mimics or draws inspiration from the identified natural systems.
   b) Describe the key components and mechanisms of your biomimetic design.
   c) Explain how your solution addresses the specific urban challenge of {t['challenge']}.
   d) Discuss how your design improves upon current urban planning approaches to this challenge.

3. Implementation and Scalability (200-250 words):
   a) Outline the steps needed to implement your biomimetic solution in an urban environment.
   b) Discuss potential challenges in adapting the natural system to an urban context and how to overcome them.
   c) Explain how your solution could be scaled up or replicated in different urban settings.

4. Environmental Impact and Sustainability (150-200 words):
   a) Analyze the potential environmental benefits of your biomimetic solution.
   b) Discuss any possible negative environmental impacts and how to mitigate them.
   c) Explain how your solution contributes to long-term urban sustainability.

5. Social and Economic Considerations (150-200 words):
   a) Discuss the potential social impacts of implementing your biomimetic solution.
   b) Analyze the economic feasibility of your design, including potential costs and benefits.
   c) Propose strategies to ensure community acceptance and engagement with your solution.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your biomimetic solution integrates knowledge from biology, engineering, urban planning, and environmental science.
   b) Discuss how this interdisciplinary approach enhances the effectiveness of your solution.
   c) Suggest potential areas for further research or collaboration across disciplines.

Ensure your response demonstrates a deep understanding of both natural systems and urban planning principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and practical applicability.

Format your response using clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified natural system and its relevance to the urban challenge.",
            "The proposed biomimetic solution is innovative and clearly inspired by the natural system.",
            "The design effectively addresses the specified urban planning challenge.",
            "The implementation and scalability analysis is thorough and realistic.",
            "The environmental impact assessment is comprehensive and considers both positive and negative effects.",
            "The social and economic analysis is well-reasoned and considers multiple stakeholders.",
            "The response effectively integrates knowledge from multiple disciplines.",
            "The solution is creative while maintaining scientific plausibility and practical applicability.",
            "The response is well-structured, clear, and within the specified word count range of 1100-1400 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
