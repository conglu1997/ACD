import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy",
            "melancholy",
            "excitement",
            "serenity"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre"
        ]
        tasks = [
            {
                "emotion": random.choice(emotions),
                "musical_element": random.choice(musical_elements)
            },
            {
                "emotion": random.choice(emotions),
                "musical_element": random.choice(musical_elements)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate musical structures into linguistic patterns and vice versa, then use it to create a 'musical language' for the emotion of {t['emotion']}, focusing on the musical element of {t['musical_element']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for musical-linguistic translation.
   b) Explain how your system integrates music theory concepts with linguistic structures.
   c) Detail how the system ensures the generated 'musical language' effectively conveys the emotion of {t['emotion']}.

2. Translation Process (200-250 words):
   a) Explain the specific techniques your system uses to translate between musical and linguistic structures.
   b) Provide an example of how a particular {t['musical_element']} pattern would be translated into a linguistic feature.
   c) Discuss how your system handles the subjective nature of emotional interpretation in music and language.

3. Musical Language Features (200-250 words):
   a) Describe 3-4 key features of the generated 'musical language' for {t['emotion']}, explaining how they reflect both musical and linguistic elements.
   b) Provide examples of 'words' or 'phrases' in the new language, with explanations of their musical and emotional significance.
   c) Explain how these features contribute to expressing the emotion of {t['emotion']}.

4. AI Learning and Adaptation (150-200 words):
   a) Discuss how your AI system learns and improves its translations over time.
   b) Explain how it might adapt to different musical genres or linguistic styles.

5. Practical Application (150-200 words):
   a) Describe a specific scenario where this 'musical language' could be used in composition or emotional expression.
   b) Explain the potential benefits and challenges of using this system in music therapy or emotional communication.

6. Ethical Considerations and Limitations (100-150 words):
   a) Discuss potential ethical implications of creating a language that directly links music and emotions.
   b) Address limitations of your approach and areas for future research or improvement.

Ensure your response demonstrates a deep understanding of music theory, linguistics, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your language design while maintaining scientific plausibility.

Your total response should be between 1050-1350 words. Organize your answer using clear headings for each section, numbered as above.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, linguistics, and AI principles",
            "The proposed system effectively integrates musical structures with linguistic patterns",
            f"The design addresses the specific emotion of {t['emotion']} and focuses on the musical element of {t['musical_element']}",
            "The 'musical language' features are creative, well-explained, and plausibly linked to the target emotion",
            "The practical applications and ethical considerations are thoughtfully discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
