import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy",
            "sadness",
            "anger",
            "fear",
            "disgust",
            "surprise"
        ]
        culture_pairs = [
            ("Japanese", "Brazilian"),
            ("Indian", "Swedish"),
            ("Nigerian", "Canadian"),
            ("Egyptian", "South Korean")
        ]
        contexts = [
            "business negotiation",
            "family gathering",
            "romantic relationship",
            "political debate"
        ]
        return {
            "1": {
                "emotion": random.choice(emotions),
                "source_culture": culture_pairs[0][0],
                "target_culture": culture_pairs[0][1],
                "context": random.choice(contexts)
            },
            "2": {
                "emotion": random.choice(emotions),
                "source_culture": culture_pairs[1][0],
                "target_culture": culture_pairs[1][1],
                "context": random.choice(contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate and adapt the emotional expression of {t['emotion']} from {t['source_culture']} culture to {t['target_culture']} culture in the context of a {t['context']}. Your response should include the following sections, with each section clearly labeled:

1. Emotional Expression Analysis (200-250 words):
   a) Describe how {t['emotion']} is typically expressed in {t['source_culture']} culture, considering verbal, non-verbal, and contextual cues.
   b) Explain potential cultural misunderstandings that could arise when this expression is perceived by someone from {t['target_culture']} culture.
   c) Discuss how the {t['context']} might influence the expression and perception of {t['emotion']} in both cultures.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI system for emotional intelligence and cultural translation.
   b) Explain how your system would process and analyze emotional expressions from {t['source_culture']} culture.
   c) Describe the mechanisms your system would use to adapt these expressions for {t['target_culture']} culture.
   d) Discuss how your system would incorporate context-awareness for the {t['context']} scenario.

3. Translation and Adaptation Process (200-250 words):
   a) Provide a step-by-step explanation of how your AI system would translate and adapt a specific instance of {t['emotion']} from {t['source_culture']} to {t['target_culture']} in the given {t['context']}.
   b) Include examples of input and output for your system, considering verbal and non-verbal aspects of communication.
   c) Explain how your system ensures cultural sensitivity and appropriateness in its adaptations.

4. Evaluation and Refinement (150-200 words):
   a) Propose methods to evaluate the effectiveness and accuracy of your AI system's emotional-cultural translations.
   b) Describe how your system would learn and improve from feedback and new data.
   c) Discuss potential challenges in evaluating emotional intelligence across cultures and how you would address them.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI-driven emotional and cultural translation.
   b) Discuss how your system addresses concerns about cultural appropriation or stereotyping.
   c) Propose guidelines for the responsible development and use of emotionally intelligent, cross-cultural AI systems.

6. Broader Implications (100-150 words):
   a) Discuss how your AI system could impact fields such as international diplomacy, global business, or intercultural education.
   b) Propose a novel research question that emerges from the development of your system.

Ensure your response demonstrates a deep understanding of emotional intelligence, cultural differences, and AI system design. Be creative and innovative while maintaining scientific and cultural accuracy. Format your response with clear headings for each section and adhere to the word count limits provided. Your total response should be between 1050-1350 words. Include a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a nuanced understanding of emotional expression in the specified cultures.",
            "The AI system architecture is well-designed and addresses the complexities of emotional and cultural translation.",
            "The translation and adaptation process is clearly explained and culturally sensitive.",
            "The evaluation methods and ethical considerations are thoughtfully addressed.",
            "The response shows creativity and innovation while maintaining scientific and cultural accuracy.",
            "The response adheres to the specified format with clear section headings and word count limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
