import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {"emotion": "empathy", "context": "conflict resolution", "culture1": "Japanese", "culture2": "Brazilian"},
            {"emotion": "awe", "context": "scientific discovery", "culture1": "Maasai", "culture2": "Swedish"},
            {"emotion": "pride", "context": "athletic achievement", "culture1": "American", "culture2": "Chinese"},
            {"emotion": "gratitude", "context": "community service", "culture1": "Indian", "culture2": "Canadian"}
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system that allows AI agents to learn and express the emotion of {t['emotion']} through embodied experiences in diverse linguistic and cultural contexts, focusing on the scenario of {t['context']}. Your system should specifically address the cultural contexts of {t['culture1']} and {t['culture2']} cultures. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your VR system for embodied emotional learning.
   b) Explain how your system integrates virtual reality, AI, linguistics, and emotion theory.
   c) Discuss how your system handles the challenges of cross-cultural emotion expression and interpretation.
   d) Include a simple diagram of your system architecture using ASCII art or Unicode characters.

2. Embodied Learning Process (200-250 words):
   a) Explain the process of how AI agents learn to embody and express {t['emotion']} in the VR environment.
   b) Describe the virtual physical and social cues your system uses to represent and teach this emotion.
   c) Discuss how linguistic and cultural differences between {t['culture1']} and {t['culture2']} are incorporated into the learning process.

3. Emotion Expression and Recognition (200-250 words):
   a) Detail how AI agents express {t['emotion']} through virtual embodiment (e.g., gestures, facial expressions, vocalizations).
   b) Explain how your system enables AI agents to recognize and interpret this emotion in others.
   c) Describe how the system handles ambiguity and context-dependence in emotional expression.

4. Application to {t['context']} (200-250 words):
   a) Explain how your system could be applied to the scenario of {t['context']}.
   b) Provide a specific example of how AI agents might use their embodied understanding of {t['emotion']} in this context.
   c) Discuss potential benefits and challenges of using embodied AI in this scenario.

5. Cross-cultural Adaptation (150-200 words):
   a) Describe how your system adapts the expression and interpretation of {t['emotion']} between {t['culture1']} and {t['culture2']} cultures.
   b) Explain how linguistic differences are addressed in the cross-cultural expression of this emotion.
   c) Discuss any ethical considerations in modeling emotions across these specific cultures.

6. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system in teaching embodied emotional intelligence.
   b) Suggest an experiment to validate your system's performance in expressing and recognizing {t['emotion']} across {t['culture1']} and {t['culture2']} cultures.
   c) Discuss potential biases in your system and how you would address them.

7. Future Implications (100-150 words):
   a) Discuss the potential impact of embodied emotive AI on human-AI interaction and communication.
   b) Propose two potential applications of your system beyond the given scenario.

Ensure your response demonstrates a deep understanding of embodied cognition, virtual reality, linguistics, emotion theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1600 words. Stay within the specified word count for each section.

For the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of embodied cognition, virtual reality, linguistics, emotion theory, and artificial intelligence.",
            f"The system architecture effectively integrates VR, AI, linguistics, and emotion theory to teach and express {t['emotion']}.",
            f"The embodied learning process and emotion expression mechanisms are well-explained and plausible for {t['emotion']}.",
            f"The application to {t['context']} is innovative and well-reasoned.",
            f"The cross-cultural adaptation of {t['emotion']} expression between {t['culture1']} and {t['culture2']} cultures is thoughtfully addressed.",
            "The evaluation methods and future implications are insightful and demonstrate strong interdisciplinary thinking.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
