import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        cultures = ['Western', 'East Asian', 'African', 'Middle Eastern', 'Latin American', 'South Asian']
        return {
            "1": {"emotion": random.choice(emotions), "culture": random.choice(cultures)},
            "2": {"emotion": random.choice(emotions), "culture": random.choice(cultures)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational system that analyzes and generates music based on the emotional state of {t['emotion']} within the context of {t['culture']} culture. Your system should integrate principles from music theory, cognitive science, and artificial intelligence. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your system and how they interact.
   b) Explain how your system incorporates music theory principles specific to {t['culture']} culture.
   c) Detail how cognitive models of emotion are integrated into your architecture.
   d) Discuss the AI techniques used for music analysis and generation.

2. Emotional-Cultural Mapping (250-300 words):
   a) Explain how your system maps the emotion of {t['emotion']} to musical elements (e.g., rhythm, melody, harmony, timbre).
   b) Describe how cultural context influences this mapping in {t['culture']} music.
   c) Provide an example of how a specific musical feature would be analyzed or generated to express {t['emotion']} in {t['culture']} music.

3. Learning and Adaptation (200-250 words):
   a) Describe how your system learns from existing music to improve its analysis and generation capabilities.
   b) Explain how it adapts to individual listener preferences while maintaining cultural authenticity.
   c) Discuss any novel machine learning techniques you've incorporated for this purpose.

4. Evaluation Methodology (200-250 words):
   a) Propose a method to evaluate the effectiveness of your system in generating emotionally and culturally appropriate music.
   b) Describe potential experiments, including control conditions and measurable outcomes.
   c) Discuss how you would validate the cultural authenticity and emotional impact of the generated music.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in developing an AI system for cultural music generation.
   b) Discuss how your system addresses concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for the responsible use and development of such systems.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system contributes to our understanding of the relationship between music, emotion, and culture.
   b) Explain potential applications of your system in fields such as music therapy, cross-cultural communication, or music education.
   c) Propose a future research direction that builds on your system's capabilities.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and cultural sensitivity.

Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence.",
            "The system architecture is well-designed and integrates all required components effectively.",
            "The emotional-cultural mapping is well-explained and culturally sensitive.",
            "The learning and adaptation mechanisms are innovative and well-described.",
            "The evaluation methodology is comprehensive and well-thought-out.",
            "Ethical considerations are thoroughly addressed.",
            "The interdisciplinary implications are insightful and demonstrate broad understanding.",
            "The response is creative while maintaining scientific plausibility.",
            "All sections are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
