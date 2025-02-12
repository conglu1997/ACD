import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                'challenge': 'Urban heat island effect',
                'ecosystem': 'Savanna grasslands',
                'location': 'Singapore'
            },
            {
                'challenge': 'Air pollution',
                'ecosystem': 'Coral reefs',
                'location': 'Beijing'
            }
        ]
        return {str(i+1): challenge for i, challenge in enumerate(environmental_challenges)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates biomimetic architectural solutions for sustainable urban development, then use it to create a novel building concept. Focus on addressing the environmental challenge of {t['challenge']} by drawing inspiration from the {t['ecosystem']} ecosystem. The building should be designed for {t['location']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating biomimetic architectural solutions.
   b) Explain how the system integrates knowledge from biology, architecture, and environmental science.
   c) Detail how the AI ensures the proposed solutions are both biomimetic and practical for urban development.
   d) Include a brief textual description of a flowchart representing your system's architecture.

2. Biomimetic Analysis (250-300 words):
   a) Analyze how the {t['ecosystem']} ecosystem addresses challenges similar to {t['challenge']}.
   b) Identify at least three key biological strategies or mechanisms that could be applied to architecture.
   c) Explain how these strategies could be translated into architectural elements or systems.

3. Novel Building Concept (300-350 words):
   a) Use your AI system to generate a novel building concept for {t['location']} that addresses {t['challenge']}.
   b) Describe the overall form, structure, and key features of the building.
   c) Explain how the design incorporates biomimetic elements inspired by the {t['ecosystem']}.
   d) Discuss how the building would function to mitigate {t['challenge']} in its urban context.

4. Technical Feasibility (200-250 words):
   a) Analyze the technical challenges in implementing your biomimetic building concept.
   b) Propose innovative materials or construction techniques necessary for realization.
   c) Discuss any potential limitations or areas requiring further research and development.

5. Environmental Impact Assessment (200-250 words):
   a) Evaluate the potential environmental benefits of your building design.
   b) Discuss any possible negative environmental impacts and how they could be mitigated.
   c) Compare the sustainability of your biomimetic approach to traditional architectural solutions.

6. Sociocultural Considerations (150-200 words):
   a) Analyze how your biomimetic building might be perceived by the local population in {t['location']}.
   b) Discuss potential cultural or social impacts of introducing this type of architecture.
   c) Propose strategies for community engagement and acceptance of the innovative design.

7. Future Developments (150-200 words):
   a) Suggest two potential improvements or extensions to your AI system for biomimetic architecture.
   b) Propose a novel application of your system beyond individual building design (e.g., urban planning, infrastructure).
   c) Discuss how this approach could influence future trends in sustainable architecture and AI-driven design.

Ensure your response demonstrates a deep understanding of biomimicry, architectural design principles, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biomimicry, architectural design, and environmental science",
            "The AI system design is innovative and plausibly integrates knowledge from multiple disciplines",
            "The biomimetic analysis shows a clear connection between the specified ecosystem and architectural solutions",
            "The novel building concept effectively addresses the given environmental challenge using biomimetic principles",
            "Technical feasibility, environmental impact, and sociocultural considerations are thoroughly addressed",
            "The response is creative and original while maintaining scientific plausibility",
            "The writing is clear, well-structured, and adheres to the specified word count (1550-1900 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
