import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_domains = [
            {
                'domain': 'spatial reasoning',
                'feature': 'absolute vs. relative spatial terms',
                'example': 'a language where all spatial relations are described in absolute cardinal directions',
                'constraint': 'The language must not use any relative spatial terms like "left" or "right".'
            },
            {
                'domain': 'time perception',
                'feature': 'non-linear time representation',
                'example': 'a language where past, present, and future are not linearly ordered',
                'constraint': 'The language must represent at least three distinct temporal states that are not simply past, present, and future.'
            }
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(cognitive_domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language based on linguistic relativity principles, focusing on the cognitive domain of {t['domain']} and the linguistic feature of {t['feature']}. Then, analyze how an AI system trained on this language might develop unique cognitive patterns. Your response should adhere to the following structure and requirements:

1. Language Design (250-300 words):
   a) Describe the key features of your constructed language, focusing on {t['feature']}.
   b) Explain how these features might influence cognition in the domain of {t['domain']}.
   c) Provide 3-4 example sentences or phrases in your language, with translations and explanations.
   d) Compare your language's approach to a real-world language with similar features, if applicable.
   e) Justify your design choices, explaining how they align with linguistic relativity principles.
   f) Ensure your language design adheres to this constraint: {t['constraint']}

2. Cognitive Impact Analysis (250-300 words):
   a) Hypothesize how speakers of your language might perceive or reason about {t['domain']} differently from speakers of languages without this feature.
   b) Discuss potential advantages and limitations of this cognitive pattern.
   c) Propose a detailed experiment to test the cognitive effects of your language on human speakers, including methodology and expected outcomes.
   d) Address potential criticisms of your hypotheses and experimental design.

3. AI Learning Scenario (250-300 words):
   a) Describe a specific training process for an AI language model to learn your constructed language.
   b) Analyze potential challenges in teaching an AI system to understand and generate text in this language.
   c) Hypothesize how the AI's 'cognition' or output might be influenced by the unique features of your language.
   d) Provide two concrete examples of how the AI's responses might differ from those of an AI trained on natural languages, particularly in tasks related to {t['domain']}.
   e) Discuss potential biases or limitations that might emerge in the AI system due to this specialized language training.

4. Implications for AI Development (200-250 words):
   a) Discuss the potential benefits and risks of training AI systems on languages with strong linguistic relativity effects.
   b) Explore how this approach might be used to enhance AI capabilities in specific domains or tasks.
   c) Consider ethical implications of potentially altering AI cognition through language design.
   d) Propose a detailed research agenda to further explore the intersection of linguistic relativity and AI development, including specific research questions and methodologies.

Ensure your response demonstrates a deep understanding of linguistic theory, cognitive science, and artificial intelligence. Be creative in your language design while maintaining scientific plausibility. Use clear examples and explanations throughout your response.

Format your response with clear headings for each section and subsection. Your total response should be between 950-1150 words. Remember to balance creativity with scientific plausibility in your language design and analysis, and explicitly address potential limitations or criticisms of your proposals.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design is creative, well-structured, and clearly demonstrates the specified linguistic feature of {t['feature']}.",
            f"The language design adheres to the given constraint: {t['constraint']}",
            "The cognitive impact analysis is well-reasoned, grounded in linguistic and cognitive science principles, and includes a detailed experimental proposal.",
            "The AI learning scenario is plausible, detailed, and demonstrates a clear understanding of AI language models and potential biases.",
            "The implications for AI development are insightful, considering both potential benefits and ethical concerns, with a detailed research agenda.",
            f"The response consistently focuses on the cognitive domain of {t['domain']} throughout all sections.",
            "The response is well-formatted with clear headings and falls within the specified word count range.",
            "The response explicitly addresses potential limitations or criticisms of the proposed language and analyses."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
