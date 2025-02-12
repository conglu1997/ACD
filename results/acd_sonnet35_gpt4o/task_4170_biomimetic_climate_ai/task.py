import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                'challenge': 'Urban heat islands',
                'location': 'Megacities',
                'biomimicry_inspiration': 'Termite mounds',
                'scale': 'City-wide'
            },
            {
                'challenge': 'Coastal erosion',
                'location': 'Tropical coastlines',
                'biomimicry_inspiration': 'Mangrove forests',
                'scale': 'Regional'
            },
            {
                'challenge': 'Agricultural water scarcity',
                'location': 'Arid regions',
                'biomimicry_inspiration': 'Namibian desert beetle',
                'scale': 'Large-scale farming'
            },
            {
                'challenge': 'Carbon dioxide accumulation',
                'location': 'Global atmosphere',
                'biomimicry_inspiration': 'Coral reefs',
                'scale': 'Global'
            }
        ]
        
        return {str(i+1): random.choice(environmental_challenges) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses biomimicry principles to develop innovative climate change mitigation strategies, then apply it to the following environmental challenge:

Challenge: {t['challenge']}
Location: {t['location']}
Biomimicry Inspiration: {t['biomimicry_inspiration']}
Scale: {t['scale']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for biomimetic climate solutions.
   b) Explain how your system integrates knowledge from biology, environmental science, and engineering.
   c) Detail how the system analyzes and applies biomimicry principles to climate challenges.
   d) Discuss any novel AI techniques or algorithms employed in your design.
   e) Include a high-level diagram or flowchart of your system architecture (describe it textually).

2. Biomimetic Analysis (250-300 words):
   a) Analyze the specified biomimicry inspiration ({t['biomimicry_inspiration']}) in detail.
   b) Explain how your AI system would extract and generalize principles from this biological model.
   c) Discuss how these principles could be applied to the given environmental challenge ({t['challenge']}).
   d) Identify at least three key features or mechanisms that could inform your solution.

3. Solution Design (300-350 words):
   a) Propose a specific solution to the given environmental challenge using your AI system.
   b) Explain how your solution incorporates biomimetic principles.
   c) Describe how the solution would be implemented at the specified scale ({t['scale']}).
   d) Discuss potential challenges in implementation and how they might be addressed.
   e) Provide a quantitative estimate of the solution's potential impact on climate change mitigation.

4. Adaptability and Scalability (200-250 words):
   a) Explain how your AI system and solution could be adapted to different environmental contexts.
   b) Discuss the potential for scaling the solution to address similar challenges in other locations.
   c) Propose at least two modifications that could enhance the solution's effectiveness or applicability.

5. Ethical and Environmental Considerations (200-250 words):
   a) Identify at least three potential ethical concerns related to implementing your solution.
   b) Discuss any possible negative environmental impacts and how they could be mitigated.
   c) Propose guidelines for responsible development and deployment of biomimetic climate solutions.

6. Future Research Directions (150-200 words):
   a) Suggest two potential enhancements to your AI system for biomimetic climate solutions.
   b) Propose a specific research question that could further advance this field.
   c) Discuss how emerging technologies might impact the development of biomimetic climate solutions.

Ensure your response demonstrates a deep understanding of artificial intelligence, environmental science, biology, and engineering principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Your total response should be between 1400-1700 words. Format your response with clear headings for each section, and number your paragraphs within each section for clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI, environmental science, biology, and engineering principles in the context of climate change mitigation.",
            f"The proposed AI system effectively addresses the given environmental challenge of {t['challenge']} using biomimicry principles inspired by {t['biomimicry_inspiration']}.",
            f"The solution is well-designed and feasible for implementation at the specified scale of {t['scale']}.",
            "The response includes innovative ideas while maintaining scientific plausibility and addressing real-world constraints.",
            "Ethical and environmental considerations are thoroughly addressed, demonstrating awareness of potential impacts and responsible development.",
            "The response follows the required format and word count guidelines, and includes specific examples and techniques for the given challenge."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
