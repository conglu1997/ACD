import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise']
        cultures = ['Japanese', 'American', 'Nigerian', 'Indian', 'Brazilian', 'Russian']
        contexts = ['professional', 'intimate', 'public', 'artistic']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'emotion': random.choice(emotions),
                'culture1': random.choice(cultures),
                'culture2': random.choice([c for c in cultures if c != tasks.get(str(i-1), {}).get('culture1')]),
                'context': random.choice(contexts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating emotionally nuanced language across different cultures, with a focus on the emotion of {t['emotion']}. Then, use your system to analyze and produce culturally appropriate emotional expressions in a {t['context']} context, comparing {t['culture1']} and {t['culture2']} cultures. Your response should include:

1. System Architecture (300-350 words):
   a) Describe at least three key components of your AI system for cross-cultural emotional language processing.
   b) Explain how your system integrates linguistic, psychological, and cultural knowledge. Provide at least one specific example for each domain.
   c) Discuss at least one novel technique or algorithm used in your design.
   d) Include a high-level diagram or detailed description of your system's architecture.

2. Emotion Analysis (250-300 words):
   a) Use your system to analyze how {t['emotion']} is expressed in {t['culture1']} and {t['culture2']} cultures. Provide at least two specific examples for each culture.
   b) Compare and contrast at least three linguistic and paralinguistic features used to convey this emotion in each culture.
   c) Discuss how the {t['context']} context influences the expression of {t['emotion']} in each culture. Provide at least one concrete example for each.

3. Expression Generation (250-300 words):
   a) Use your system to generate two examples of emotionally nuanced language expressing {t['emotion']} in a {t['context']} context:
      - One example appropriate for {t['culture1']} culture (50-75 words)
      - One example appropriate for {t['culture2']} culture (50-75 words)
   b) Explain the rationale behind each generated expression, highlighting at least three cultural nuances for each.
   c) Discuss at least two methods your system uses to ensure cultural appropriateness and emotional accuracy.

4. Evaluation and Ethical Considerations (200-250 words):
   a) Propose at least two methods to evaluate the accuracy and cultural sensitivity of your system's outputs.
   b) Discuss at least three potential biases or limitations in your approach and how they might be addressed.
   c) Explore at least two ethical implications of using AI for cross-cultural emotional communication.

Ensure your response demonstrates a deep understanding of linguistics, psychology, cultural studies, and AI technologies. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and cultural accuracy.

Format your response with clear headings for each section and number your points as shown above. Your total response should be between 1000-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed and plausible AI system architecture for cross-cultural emotional language processing, with at least three key components described.",
            f"The analysis of {t['emotion']} expression in {t['culture1']} and {t['culture2']} cultures is thorough and culturally informed, with at least two specific examples for each culture.",
            f"The generated examples of emotional expression are appropriate for the given cultures and {t['context']} context, with explanations of at least three cultural nuances for each.",
            "The response demonstrates understanding of linguistics, psychology, cultural studies, and AI technologies, using appropriate technical terminology.",
            "At least two ethical considerations and three potential biases are thoughtfully discussed.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
