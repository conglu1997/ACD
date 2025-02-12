import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_domains = [
            {
                "domain": "Temporal cognition",
                "feature": "Non-linear time conceptualization"
            },
            {
                "domain": "Spatial reasoning",
                "feature": "Absolute vs. relative spatial references"
            },
            {
                "domain": "Color perception",
                "feature": "Continuous color spectrum representation"
            }
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(cognitive_domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language structure that emphasizes {t['feature']} within the cognitive domain of {t['domain']}, based on principles of linguistic relativity. Then, analyze its potential effects on human cognition and AI language processing. Your response should include the following sections:

1. Language Design (250-300 words):
   a) Describe the key features of your novel language structure, focusing on how it emphasizes {t['feature']}.
   b) Explain how these features differ from typical structures in existing natural languages.
   c) Provide 3-4 example sentences or phrases in your language with their English translations and explanations of how they embody the target feature.

2. Cognitive Effects Analysis (250-300 words):
   a) Hypothesize how your language structure might influence human cognition in the domain of {t['domain']}.
   b) Discuss potential advantages and disadvantages of this cognitive effect.
   c) Propose an experiment to test the cognitive effects of your language structure on human speakers.

3. AI Language Processing Implications (250-300 words):
   a) Analyze how current AI language models might process or struggle with your novel language structure.
   b) Speculate on how exposure to this language structure might alter an AI's internal representations or reasoning processes.
   c) Discuss the potential implications for AI development in natural language processing and understanding.

4. Linguistic Relativity Reflection (200-250 words):
   a) Reflect on how your language design and analysis relate to the broader debate on linguistic relativity.
   b) Discuss the ethical implications of designing languages to influence cognition, for both humans and AI.
   c) Consider potential real-world applications or consequences of your findings.

5. Meta-Analysis of AI Response (200-250 words):
   a) Analyze your own response to this task as an AI language model.
   b) Reflect on any challenges or limitations you experienced in designing and analyzing the novel language structure.
   c) Discuss how your response might differ from that of a human linguist or cognitive scientist.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your language design while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic relativity, cognitive science, and AI language processing",
            "The language design is creative, well-described, and plausibly linked to the specified cognitive domain and feature",
            "The cognitive effects analysis is logically sound and demonstrates understanding of how language may influence thought",
            "The AI language processing implications are insightful and show an understanding of current AI capabilities and limitations",
            "The linguistic relativity reflection thoughtfully considers broader implications and ethical concerns",
            "The meta-analysis demonstrates self-awareness and critical thinking about the AI's own response",
            "The response is well-structured and adheres to the word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
