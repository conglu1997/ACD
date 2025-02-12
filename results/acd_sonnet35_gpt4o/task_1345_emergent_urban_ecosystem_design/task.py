import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            'Sustainable transportation',
            'Affordable housing',
            'Energy efficiency',
            'Social cohesion',
            'Environmental resilience',
            'Economic inequality',
            'Public health',
            'Education access',
            'Cultural preservation',
            'Technological integration'
        ]
        
        emergent_principles = [
            'Self-organization',
            'Adaptive networks',
            'Feedback loops',
            'Distributed control',
            'Phase transitions',
            'Fractal scaling',
            'Swarm intelligence',
            'Edge of chaos',
            'Stigmergy',
            'Autopoiesis'
        ]
        
        task1 = {
            'challenge': random.choice(urban_challenges),
            'principle': random.choice(emergent_principles)
        }
        
        task2 = {
            'challenge': random.choice(urban_challenges),
            'principle': random.choice(emergent_principles)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        principle_explanations = {
            'Self-organization': 'the spontaneous emergence of order from local interactions',
            'Adaptive networks': 'systems that can modify their internal structure to changing conditions',
            'Feedback loops': 'circular processes where outputs affect inputs',
            'Distributed control': 'control spread across multiple components rather than centralized',
            'Phase transitions': 'abrupt changes in system properties at critical points',
            'Fractal scaling': 'similar patterns at different scales',
            'Swarm intelligence': 'collective behavior emerging from decentralized interactions',
            'Edge of chaos': 'balance between order and randomness where complexity emerges',
            'Stigmergy': 'indirect coordination through environmental modifications',
            'Autopoiesis': 'self-maintaining and self-reproducing systems'
        }
        
        return f"""Design a hypothetical urban ecosystem that addresses the challenge of {t['challenge']} using the emergent principle of {t['principle']} ({principle_explanations[t['principle']]}). Your response should include the following sections:

1. Urban Ecosystem Design (300-350 words):
   a) Describe the overall structure and key components of your urban ecosystem.
   b) Explain how your design incorporates the specified emergent principle.
   c) Detail how your ecosystem addresses the given urban challenge.
   d) Include at least one innovative feature that distinguishes your design from traditional urban planning approaches.
   e) Provide a conceptual diagram or detailed description of your urban ecosystem.

2. Emergent Dynamics (250-300 words):
   a) Explain how the specified emergent principle manifests in your urban ecosystem.
   b) Describe the key interactions and feedback loops that drive the system's behavior.
   c) Discuss how your ecosystem might evolve or adapt over time.

3. Societal and Environmental Impact Analysis (200-250 words):
   a) Analyze the potential positive and negative impacts of your urban ecosystem on society and the environment.
   b) Discuss how your design might influence human behavior and social dynamics.
   c) Consider potential unintended consequences and how they might be mitigated.

4. Implementation and Scalability (200-250 words):
   a) Propose a strategy for implementing your urban ecosystem design in a real-world context.
   b) Discuss the scalability of your design and how it might be adapted for different city sizes or cultural contexts.
   c) Identify potential challenges in implementation and suggest solutions.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of designing urban environments based on emergent principles.
   b) Address concerns related to individual agency, privacy, and social equity in your urban ecosystem.
   c) Propose guidelines for the responsible development and management of such systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research or experimentation related to your urban ecosystem design.
   b) Discuss how advancements in AI, IoT, or other technologies might enhance or modify your design in the future.

Ensure your response demonstrates a deep understanding of complex systems theory, urban planning principles, and societal dynamics. Be creative in your approach while maintaining scientific and practical plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Maintain internal consistency throughout your urban ecosystem design, ensuring that all components and dynamics align with the chosen emergent principle and urban challenge.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of complex systems theory and its application to urban planning.",
            "The urban ecosystem design effectively incorporates the specified emergent principle and addresses the given urban challenge.",
            "The design includes at least one innovative feature that distinguishes it from traditional urban planning approaches.",
            "The analysis of emergent dynamics and system behavior is thorough and well-reasoned.",
            "The societal and environmental impact analysis is comprehensive, considering both positive and negative effects.",
            "The implementation strategy and scalability discussion are practical and well-thought-out.",
            "Ethical considerations are addressed thoughtfully, with proposed guidelines for responsible development.",
            "Future research directions are insightful and relevant to advancing the field.",
            "The response maintains internal consistency throughout the urban ecosystem design.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
