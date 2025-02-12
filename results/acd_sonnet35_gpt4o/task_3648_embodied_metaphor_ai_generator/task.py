import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        embodied_domains = [
            {
                'source_domain': 'temperature',
                'target_domain': 'emotional states',
                'application': 'poetry generation'
            },
            {
                'source_domain': 'spatial relations',
                'target_domain': 'time perception',
                'application': 'cross-cultural communication'
            }
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(embodied_domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets novel metaphors based on principles of embodied cognition, focusing on the relationship between the source domain of {t['source_domain']} and the target domain of {t['target_domain']}. Then, analyze its potential applications in {t['application']}. Your response should include:

1. Embodied Cognition Framework (200-250 words):
   a) Explain the key principles of embodied cognition relevant to metaphor creation.
   b) Describe how {t['source_domain']} experiences might shape our understanding of {t['target_domain']}.
   c) Discuss any existing research on this specific metaphorical mapping.

2. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor generation and interpretation.
   b) Explain how your system incorporates embodied cognition principles.
   c) Detail any novel techniques or algorithms used in your model.
   d) Include a high-level diagram or flowchart of your AI system's architecture.

3. Metaphor Generation Process (250-300 words):
   a) Explain step-by-step how your AI system generates novel metaphors.
   b) Provide two examples of metaphors your system might generate, linking {t['source_domain']} to {t['target_domain']}.
   c) Discuss how your system ensures the metaphors are both novel and comprehensible.

4. Metaphor Interpretation Mechanism (200-250 words):
   a) Describe how your AI system interprets and explains the meaning of metaphors.
   b) Use one of the examples from the previous section to illustrate the interpretation process.
   c) Discuss how your system handles ambiguity or multiple possible interpretations.

5. Application Analysis (250-300 words):
   a) Analyze how your AI system could be applied to {t['application']}.
   b) Provide a specific example of how it might be used in this context.
   c) Discuss potential benefits and limitations of using AI-generated metaphors in this application.
   d) Provide a quantitative estimate of the metaphor's effectiveness in this application, using a proposed metric of your choice.

6. Cognitive Linguistics Implications (200-250 words):
   a) Discuss how your AI system's approach to metaphor generation and interpretation might inform our understanding of human cognition and language use.
   b) Propose an experiment using your AI system to investigate a specific question in cognitive linguistics.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical concerns related to AI-generated metaphors and their applications.
   b) Suggest guidelines for responsible use of your system.
   c) Propose two future research directions that could enhance or extend your AI system's capabilities.

Ensure your response demonstrates a deep understanding of cognitive linguistics, embodied cognition, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 1550-1900 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of embodied cognition and its application to metaphor generation, specifically relating {t['source_domain']} to {t['target_domain']}.",
            "The AI system architecture is innovative, scientifically plausible, and thoroughly explained with clear components and processes.",
            f"The metaphor generation and interpretation processes are well-described, with plausible examples linking {t['source_domain']} to {t['target_domain']}.",
            f"The application analysis for {t['application']} is insightful and considers both benefits and limitations, including a quantitative estimate of the metaphor's effectiveness.",
            "The cognitive linguistics implications and proposed experiment are scientifically sound and demonstrate a deep understanding of the field.",
            "Ethical considerations are thoughtfully addressed, with clear guidelines and future research directions proposed.",
            "The response adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
