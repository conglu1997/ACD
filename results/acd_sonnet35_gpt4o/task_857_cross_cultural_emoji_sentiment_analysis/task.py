import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Japanese",
                "context": "business communication",
                "emoji_example": "🙇"
            },
            {
                "name": "Brazilian",
                "context": "social media interaction",
                "emoji_example": "🤙"
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(cultures)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and generate culturally-appropriate emoji-based communication for {t['name']} culture in the context of {t['context']}. Your system should be able to interpret the sentiment and meaning behind emoji usage in this specific cultural context, as well as generate appropriate emoji responses. As an example, consider the emoji {t['emoji_example']} and its usage in this culture.

Your response should include the following sections:

1. Cultural Analysis (150-200 words):
   a) Key characteristics of emoji usage in {t['name']} culture, particularly in {t['context']}.
   b) How emoji interpretation in this culture differs from others.
   c) Cultural taboos or sensitivities related to emoji use in this context.
   d) Specific meaning and usage of {t['emoji_example']} in this cultural context.

2. AI System Design (200-250 words):
   a) Architecture of your AI system, including key components and their functions.
   b) Method for analyzing sentiment and meaning of emojis in the given cultural context.
   c) Approach for generating culturally appropriate emoji responses.
   d) Handling of ambiguity or multiple interpretations of emojis.

3. Training and Data Considerations (150-200 words):
   a) Types of data needed to train your system.
   b) Methods to ensure cultural authenticity and relevance in training data.
   c) Potential biases in data collection and strategies to address them.

4. Cross-Cultural Adaptation (150-200 words):
   a) Process for adapting the system for use in other cultures.
   b) Challenges in cross-cultural emoji interpretation and proposed solutions.
   c) Facilitating cross-cultural communication using emojis.

5. Ethical Implications (100-150 words):
   a) Potential ethical concerns related to system use and development.
   b) Privacy considerations in analyzing personal emoji usage.
   c) Guidelines for responsible development and use of the system.

6. Practical Application (100-150 words):
   a) Specific use case for the system in {t['context']}.
   b) Potential benefits and limitations of using the system in this scenario.

Ensure your response demonstrates a deep understanding of cultural nuances, emoji semantics, and AI principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and technological plausibility.

Format your response using the following structure:
[Section Name]
[Your content for this section]

Your total response should be between 850-1150 words.

A successful response will thoroughly address all points in each section, demonstrate a deep understanding of the cultural context and technical aspects of the AI system, and provide innovative yet plausible solutions to the challenges presented.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Cultural Analysis section accurately describes emoji usage in {t['name']} culture, particularly in {t['context']}, and includes a specific analysis of {t['emoji_example']}.",
            "The AI System Design section clearly explains the system architecture and methods for analyzing and generating culturally appropriate emoji-based communication.",
            "The Training and Data Considerations section addresses potential biases and proposes methods to ensure cultural authenticity in the training data.",
            "The Cross-Cultural Adaptation section discusses concrete strategies for adapting the system to other cultures and facilitating cross-cultural communication.",
            "The Ethical Implications section identifies at least two specific ethical concerns and proposes clear guidelines for responsible system development and use.",
            f"The Practical Application section describes a plausible and detailed use case for the system in {t['context']}, including both benefits and limitations.",
            "The response demonstrates interdisciplinary knowledge, creativity, and critical thinking in cultural studies, linguistics, and artificial intelligence.",
            "The response follows the specified format and is between 850-1150 words in total length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
