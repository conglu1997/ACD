import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_pairs = [
            {
                'source_domain': 'Time',
                'target_domain': 'Money',
                'metaphor': 'Time is money',
                'example': 'You\'re wasting my time'
            },
            {
                'source_domain': 'Love',
                'target_domain': 'Journey',
                'metaphor': 'Love is a journey',
                'example': 'Our relationship has hit a dead-end'
            }
        ]
        
        return {str(i+1): pair for i, pair in enumerate(metaphor_pairs)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a system that translates the cognitive metaphor '{t['metaphor']}' from the domain of {t['source_domain']} to a new target domain of your choice. Then, analyze an AI language model's ability to understand and generate metaphor translations using your system. Complete the following steps:

1. Metaphor Translation System (250-300 words):
   a) Choose a new target domain for the metaphor '{t['metaphor']}' that is different from {t['target_domain']}.
   b) Describe your system for translating the cognitive metaphor to this new domain.
   c) Explain the key components and processes involved in your translation system.
   d) Provide an example of how your system would translate the specific aspect "{t['example']}" to the new domain.

2. AI Comprehension Test (200-250 words):
   a) Design a test to evaluate an AI language model's understanding of your metaphor translation.
   b) Include at least three questions or tasks that assess different aspects of metaphor comprehension.
   c) Explain how each question/task measures the AI's ability to grasp the translated metaphor.

3. AI Generation Challenge (200-250 words):
   a) Create a prompt that challenges an AI to generate its own translation of '{t['metaphor']}' to yet another domain.
   b) Explain what aspects of metaphorical thinking and creativity this challenge is designed to assess.
   c) Describe how you would evaluate the AI's generated metaphor translation.

4. Cognitive-Linguistic Analysis (200-250 words):
   a) Analyze the cognitive and linguistic processes involved in understanding and translating metaphors across domains.
   b) Discuss how these processes might differ between human cognition and AI language models.
   c) Explain how your system and tests could reveal these differences.

5. Potential Applications and Implications (150-200 words):
   a) Propose two potential applications of your metaphor translation system in fields such as education, creative writing, or cross-cultural communication.
   b) Discuss the implications of AI systems capable of advanced metaphorical reasoning for natural language understanding and generation.

Ensure your response demonstrates a deep understanding of cognitive linguistics, metaphor theory, and AI language models. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Include the word count for each section in parentheses at the end of the section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed metaphor translation system with a new target domain different from {t['target_domain']}.",
            f"The system successfully translates the example '{t['example']}' to the new domain.",
            "The AI comprehension test includes at least three questions/tasks that effectively assess understanding of the translated metaphor.",
            "The AI generation challenge prompts creative metaphorical thinking and includes clear evaluation criteria.",
            "The cognitive-linguistic analysis demonstrates deep understanding of metaphor processing in both humans and AI.",
            "The potential applications and implications are insightful, well-reasoned, and relevant to the proposed metaphor translation system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
