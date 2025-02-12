import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'source_cultures': ['Japanese', 'Brazilian'],
                'target_domain': 'environmental sustainability',
                'blend_type': 'metaphorical'
            },
            {
                'source_cultures': ['Indian', 'Nordic'],
                'target_domain': 'conflict resolution',
                'blend_type': 'double-scope network'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating conceptual blends across different languages and cultures, then apply it to solve a complex global issue. Focus on blending concepts from {t['source_cultures'][0]} and {t['source_cultures'][1]} cultures to address {t['target_domain']}, using a {t['blend_type']} blend.

Note: A double-scope network blend involves integrating two input spaces with different and often clashing organizing frames, resulting in a novel emergent structure.

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cross-cultural conceptual blending.
   b) Explain how your system incorporates linguistic and cultural knowledge.
   c) Detail how the system generates and evaluates conceptual blends.
   d) Discuss any novel features that enable cross-cultural understanding and creativity.
   e) Explain how your system handles the differences between metaphorical and double-scope network blends.

2. Conceptual Blend Generation (250-300 words):
   a) Explain how your system would generate a {t['blend_type']} blend related to {t['target_domain']} using concepts from {t['source_cultures'][0]} and {t['source_cultures'][1]} cultures.
   b) Provide an example of a potential blend your system might create.
   c) Analyze the cognitive and cultural implications of this blend.

3. Application to Global Issue (250-300 words):
   a) Describe how your AI system would apply the generated blend to address challenges in {t['target_domain']}.
   b) Explain how this approach could lead to novel solutions or perspectives.
   c) Discuss potential challenges in implementing these solutions and how they might be overcome.

4. Evaluation Methodology (200-250 words):
   a) Propose a method to evaluate the effectiveness and cultural appropriateness of your system's conceptual blends.
   b) Describe metrics you would use to assess both creativity and practical applicability.
   c) Explain how you would ensure the system's outputs are respectful and beneficial to all cultures involved.

5. Ethical Considerations (200-250 words):
   a) Discuss potential ethical implications of using AI for cross-cultural conceptual blending.
   b) Address issues of cultural appropriation, misrepresentation, and power dynamics.
   c) Propose guidelines for responsible development and use of such a system.

6. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Briefly describe how these extensions could enhance cross-cultural understanding or problem-solving in global issues.

Ensure your response demonstrates a deep understanding of cognitive linguistics, cultural anthropology, and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and cultural plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive linguistics, cultural anthropology, and AI systems.",
            f"The proposed AI system effectively generates and applies conceptual blends from {t['source_cultures'][0]} and {t['source_cultures'][1]} cultures to address {t['target_domain']}.",
            f"The {t['blend_type']} blend example is creative, culturally appropriate, and relevant to {t['target_domain']}.",
            "The system architecture clearly explains how it handles different types of conceptual blends, including metaphorical and double-scope network blends.",
            "The evaluation methodology and ethical considerations are thorough and well-reasoned.",
            "The response shows innovative thinking while maintaining scientific and cultural plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
