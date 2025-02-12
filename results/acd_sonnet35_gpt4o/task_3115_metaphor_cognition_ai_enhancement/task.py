import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_types = [
            'conceptual metaphors',
            'orientational metaphors',
            'ontological metaphors',
            'structural metaphors'
        ]
        ai_applications = [
            'creative writing assistance',
            'cross-cultural communication',
            'sentiment analysis',
            'automated metaphor detection'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'metaphor_type': random.choice(metaphor_types),
                'ai_application': random.choice(ai_applications)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive model for metaphor comprehension and generation, focusing on {t['metaphor_type']}, then use it to enhance an AI language model's metaphorical capabilities for {t['ai_application']}. Your response should include the following sections:

1. Cognitive Model of Metaphor Processing (300-350 words):
   a) Describe the key components of your cognitive model for metaphor comprehension and generation.
   b) Explain how your model accounts for the specific characteristics of {t['metaphor_type']}.
   c) Discuss how your model integrates insights from cognitive linguistics and neuroscience.
   d) Propose a novel mechanism or feature in your model that addresses a current limitation in metaphor processing theories.

2. AI Integration Architecture (250-300 words):
   a) Outline how you would integrate your cognitive model into an existing AI language model architecture.
   b) Explain any modifications needed to the AI model to accommodate metaphor processing.
   c) Describe how your integrated system would handle metaphor comprehension and generation.
   d) Discuss potential challenges in implementing this integration and how you would address them.

3. Application to {t['ai_application']} (200-250 words):
   a) Explain how your enhanced AI model would improve performance in {t['ai_application']}.
   b) Provide specific examples of how the system would handle metaphors in this application.
   c) Discuss any domain-specific challenges and how your model addresses them.

4. Evaluation Framework (200-250 words):
   a) Propose a comprehensive framework for evaluating your enhanced AI model's metaphorical capabilities.
   b) Describe specific metrics or tests you would use to assess performance in metaphor comprehension and generation.
   c) Explain how you would measure improvements in {t['ai_application']} specifically.

5. Ethical and Cultural Considerations (150-200 words):
   a) Discuss potential ethical implications of enhancing AI systems with advanced metaphor processing capabilities.
   b) Address how your model accounts for cultural differences in metaphor use and interpretation.
   c) Propose guidelines for responsible development and use of metaphor-enhanced AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential research directions that could further advance metaphor processing in AI systems.
   b) Discuss how improvements in this area might impact our understanding of human cognition and language use.
   c) Speculate on potential long-term implications for AI development and human-AI interaction.

Ensure your response demonstrates a deep understanding of cognitive linguistics, metaphor theory, and AI language models. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics, metaphor theory, and AI language models.",
            f"The cognitive model adequately addresses the specific characteristics of {t['metaphor_type']}.",
            "The AI integration architecture is well-explained and plausible.",
            f"The application to {t['ai_application']} is thoroughly discussed with specific examples.",
            "The evaluation framework is comprehensive and includes specific metrics for assessing metaphor processing capabilities.",
            "Ethical and cultural considerations are thoughtfully addressed.",
            "Future research directions are insightful and well-reasoned.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified format and word count guidelines (1250-1550 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
