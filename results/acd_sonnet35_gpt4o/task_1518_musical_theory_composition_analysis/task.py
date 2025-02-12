import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            "Baroque counterpoint",
            "Jazz improvisation",
            "Minimalist repetition",
            "Atonal serialism"
        ]
        cultural_contexts = [
            "Western classical tradition",
            "African polyrhythms",
            "Indian raga system",
            "Chinese pentatonic scales"
        ]
        emotional_themes = [
            "Joy and exuberance",
            "Melancholy and longing",
            "Tension and resolution",
            "Spiritual transcendence"
        ]
        
        return {
            "1": {
                "style": random.choice(musical_styles),
                "context": random.choice(cultural_contexts),
                "theme": random.choice(emotional_themes)
            },
            "2": {
                "style": random.choice(musical_styles),
                "context": random.choice(cultural_contexts),
                "theme": random.choice(emotional_themes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"As an expert in music theory, composition, and cultural analysis, your task is to create and analyze a musical composition based on the following parameters:\n\nMusical Style: {t['style']}\nCultural Context: {t['context']}\nEmotional Theme: {t['theme']}\n\nYour response should include the following sections:\n\n1. Composition Description (250-300 words):\n   a) Describe the key musical elements of your composition (e.g., melody, harmony, rhythm, form).\n   b) Explain how your composition incorporates the given musical style.\n   c) Discuss how you've integrated elements from the specified cultural context.\n   d) Describe how your composition expresses the given emotional theme.\n\n2. Notation and Analysis (200-250 words):\n   a) Provide a brief musical notation of a key section of your composition using a text-based format (e.g., 'C4 quarter note, D4 half note, E4 quarter note' for a simple melody).\n   b) Analyze the theoretical aspects of your composition, including any innovative techniques you've employed.\n\n3. Cultural and Historical Context (200-250 words):\n   a) Discuss how your composition relates to the broader cultural context specified.\n   b) Explain any historical influences or references in your composition.\n   c) Cite at least two specific musical examples or techniques from the given cultural context and explain how you've incorporated or adapted them.\n\n4. Emotional and Psychological Impact (200-250 words):\n   a) Analyze how specific musical elements in your composition contribute to the intended emotional theme.\n   b) Discuss potential psychological effects of your composition on listeners.\n   c) Propose a specific experiment or study design to validate your analysis of the composition's emotional impact.\n\n5. Cross-Cultural Comparison (150-200 words):\n   a) Compare how your composition might be interpreted in two different cultural contexts: the one specified in the task and one of your choosing.\n   b) For each culture, discuss:\n      - Potential cultural significance of key musical elements\n      - How the emotional theme might be perceived\n      - Any challenges in translating the musical style or emotional theme\n\n6. Innovation and Future Directions (150-200 words):\n   a) Identify any innovative aspects of your composition or analysis.\n   b) Propose how this approach to composition and analysis could be applied in music education or therapy.\n   c) Suggest potential technological applications for this type of musical analysis and composition.\n\nEnsure your response demonstrates a deep understanding of music theory, composition techniques, cultural analysis, and the psychology of music. Be creative in your approach while maintaining musical and cultural authenticity. Use appropriate musical terminology and provide explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1150-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition description demonstrates a clear understanding and application of the given musical style, cultural context, and emotional theme.",
            "The notation and analysis section provides a clear text-based musical notation and shows a deep understanding of music theory and innovative composition techniques.",
            "The cultural and historical context analysis is well-researched, insightful, and cites specific musical examples from the given cultural context.",
            "The emotional and psychological impact analysis is thorough, considers multiple perspectives, and proposes a specific experiment to validate the analysis.",
            "The cross-cultural comparison demonstrates a nuanced understanding of cultural differences in musical interpretation, addressing all required points for both cultures.",
            "The innovation and future directions section proposes creative and plausible applications of the composition and analysis approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
