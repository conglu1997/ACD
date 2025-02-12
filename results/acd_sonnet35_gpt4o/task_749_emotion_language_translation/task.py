import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {
                "emotion": "nostalgia",
                "description": "A sentimental longing or wistful affection for the past",
                "scenario": "Revisiting your childhood home after many years"
            },
            {
                "emotion": "schadenfreude",
                "description": "Pleasure derived from another's misfortune",
                "scenario": "Feeling secretly pleased when a boastful colleague fails at a task"
            }
        ]
        return {str(i+1): emotion for i, emotion in enumerate(emotions)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language for expressing emotions, then use it to translate the complex emotional experience of {t['emotion']} ({t['description']}) in the given scenario: {t['scenario']}. Finally, analyze how an AI system might process and understand this emotional language. Your task has the following components:

1. Emotion Language Design (200-250 words):
   a) Create a basic structure for your emotion language, including:
      - A system for representing emotional intensity (e.g., prefixes, suffixes, or modifiers)
      - A method for combining or modifying emotional concepts
      - At least one unique linguistic feature specifically designed for emotional expression
   b) Explain the rationale behind your language design, drawing from linguistics and psychology.
   c) Provide a small lexicon (5-7 terms) of basic emotional concepts in your language, with translations.

2. Emotional Experience Translation (150-200 words):
   a) Translate the emotional experience of {t['emotion']} in the given scenario into your constructed language.
   b) Provide a detailed explanation of your translation, including how different aspects of the emotion are represented.
   c) Discuss how your language captures nuances of {t['emotion']} that might be difficult to express in natural languages.

3. AI Processing Analysis (150-200 words):
   a) Hypothesize how an AI language model might process and represent the emotional concepts in your constructed language.
   b) Discuss potential challenges or advantages for AI in understanding emotions through your language compared to natural languages.
   c) Propose a specific experiment to test whether an AI system using your emotion language demonstrates improved emotional intelligence compared to one using natural language.

4. Meta-cognitive Reflection (100-150 words):
   a) Reflect on the process of creating this emotion language and its implications for understanding human emotions.
   b) Discuss how this exercise might provide insights into the relationship between language, emotion, and artificial intelligence.

Ensure your response demonstrates a deep understanding of linguistics, psychology, and AI language processing. Be creative in your language design while maintaining logical consistency. Use appropriate technical terminology and provide clear explanations of your reasoning throughout.

Format your response with clear headings for each section and number your answers according to the structure provided. Your total response should be between 600-800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The emotion language design must include all required components (intensity system, combination method, unique feature) and a lexicon of 5-7 terms.",
            f"The translation of {t['emotion']} should effectively use the constructed language and directly address the given scenario.",
            "The AI processing analysis should include a specific, testable experiment proposal.",
            "The response must follow the provided structure and word count guidelines.",
            "The overall response should demonstrate interdisciplinary thinking and creativity while remaining grounded in linguistics, psychology, and AI concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
