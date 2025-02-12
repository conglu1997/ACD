import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_language": "Japanese",
                "target_language": "English",
                "emotion": "amae",
                "context": "workplace relationships"
            },
            {
                "source_language": "German",
                "target_language": "Mandarin Chinese",
                "emotion": "Schadenfreude",
                "context": "social media interactions"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can accurately translate and interpret emotional content from {t['source_language']} to {t['target_language']}, with a focus on the emotion of '{t['emotion']}' in the context of {t['context']}. Your response should include the following sections:

1. Conceptual Framework (200-250 words):
   a) Explain the challenges in translating emotions across cultures, particularly for '{t['emotion']}'.
   b) Discuss how cultural context affects the expression and interpretation of emotions.
   c) Describe your approach to bridging the gap between {t['source_language']} and {t['target_language']} emotional expressions.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI system for cross-cultural emotion translation.
   b) Explain how your system incorporates cultural knowledge and emotional intelligence.
   c) Describe the data sources and training approach for your system.
   d) Include a simple diagram or flowchart of your system architecture (using ASCII art or a clear textual description).

3. Emotion Recognition and Analysis (200-250 words):
   a) Detail how your AI system recognizes and analyzes emotional content in the source language.
   b) Explain any novel techniques used for detecting subtle emotional cues or context-dependent expressions.
   c) Discuss how your system handles ambiguity or multiple interpretations of emotional content.

4. Cultural Adaptation and Translation (200-250 words):
   a) Describe how your system adapts emotional content to the target culture.
   b) Explain the process of finding appropriate emotional equivalents in the target language.
   c) Discuss how context ({t['context']}) is used to refine the emotional translation.

5. Output Generation and Evaluation (150-200 words):
   a) Explain how your system generates emotionally appropriate output in the target language.
   b) Describe your approach to evaluating the accuracy and cultural appropriateness of the translations.
   c) Propose a method for gathering human feedback to improve the system's performance.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI for cross-cultural emotional translation.
   b) Address concerns about cultural appropriation or misrepresentation.
   c) Identify limitations of your system and propose guidelines for its responsible use.

7. Future Developments and Applications (100-150 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Propose two novel applications of your cross-cultural emotion AI in fields beyond translation.

Ensure your response demonstrates a deep understanding of linguistics, cultural studies, psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1600 words. Stay within the specified word count for each section.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of the challenges in translating emotions across cultures, particularly for '{t['emotion']}' from {t['source_language']} to {t['target_language']}.",
            "The AI system architecture is well-designed, incorporating cultural knowledge and emotional intelligence, with a clear explanation of its components and training approach.",
            "The emotion recognition and analysis process is thoroughly explained, including techniques for detecting subtle emotional cues and handling ambiguity.",
            f"The cultural adaptation and translation process is well-described, with a focus on finding appropriate emotional equivalents and considering the context of {t['context']}.",
            "The output generation and evaluation methods are clearly explained, including a proposal for gathering human feedback.",
            "Ethical considerations and limitations are thoughtfully discussed, addressing cultural appropriation concerns and proposing responsible use guidelines.",
            "The response includes creative and plausible suggestions for future developments and novel applications of the cross-cultural emotion AI.",
            "The overall submission demonstrates interdisciplinary knowledge integration, creative problem-solving, and scientific plausibility.",
            "The response adheres to the specified word count guidelines for each section and provides a clear system architecture diagram or description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
