import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = [
            "music",
            "language",
            "visual_art"
        ]
        elements = {
            "music": ["tempo", "key", "rhythm", "melody", "harmony", "dynamics"],
            "language": ["metaphor", "syntax", "vocabulary", "tone", "narrative structure"],
            "visual_art": ["color", "composition", "texture", "form", "line"]
        }
        emotions = [
            "joy",
            "sadness",
            "anger",
            "fear",
            "surprise",
            "love"
        ]
        
        def generate_task():
            source = random.choice(modalities)
            target = random.choice([m for m in modalities if m != source])
            return {
                "source": source,
                "target": target,
                "element": random.choice(elements[source]),
                "emotion": random.choice(emotions),
                "word_count": random.randint(1150, 1400)
            }
        
        task1 = generate_task()
        task2 = generate_task()
        while task2['source'] == task1['source'] and task2['target'] == task1['target']:
            task2 = generate_task()
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop an innovative system to translate {t['source']} representations of emotions into {t['target']} representations, focusing on the {t['source']} element of {t['element']} and the emotion of {t['emotion']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your translation system, emphasizing its novelty.
   b) Explain how your system analyzes the specified {t['source']} element in depth.
   c) Detail how your system maps {t['source']} features to {t['target']} representations, highlighting any unique approaches.
   d) Discuss any cutting-edge techniques or algorithms employed in your system.

2. Source Analysis (200-250 words):
   a) Provide a vivid description of a hypothetical {t['source']} piece that strongly expresses the emotion of {t['emotion']}.
   b) Analyze in detail how the {t['element']} in this piece contributes to expressing the emotion.
   c) Identify and explain how other elements interact with {t['element']} to convey the emotion.

3. Target Translation (250-300 words):
   a) Translate the source analysis into a rich and nuanced {t['target']} representation of the emotional experience.
   b) Explain how your translation captures the subtleties and complexities of the original expression.
   c) Discuss any challenges in conveying emotions across these modalities and how your system overcomes them.

4. Cross-Cultural and Cross-Modal Considerations (200-250 words):
   a) Analyze how cultural differences might affect the interpretation of emotions across {t['source']} and {t['target']}.
   b) Explain how your system accounts for or adapts to these cultural variations, providing specific examples.
   c) Compare and contrast emotional expression in {t['source']} and {t['target']}, highlighting unique aspects of each.

5. Applications and Implications (200-250 words):
   a) Propose two innovative potential applications of your multimodal emotion translation system.
   b) Discuss the far-reaching implications of this system for fields such as psychology, art therapy, or AI.
   c) Address any ethical considerations related to emotional interpretation and expression across modalities, proposing guidelines for responsible use.

Ensure your response demonstrates a deep understanding of {t['source']}, {t['target']}, and emotional psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be approximately {t['word_count']} words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep and nuanced understanding of the relationship between {t['source']}, {t['target']}, and emotion, particularly focusing on {t['element']} and {t['emotion']}",
            f"The system design is highly innovative, scientifically plausible, and effectively incorporates both {t['source']} and {t['target']} elements in a novel way",
            f"The {t['source']} analysis is thorough, insightful, and provides a vivid description of the emotional piece",
            f"The translation to {t['target']} is creative, rich in detail, and effectively captures the complexities of the emotional content",
            "The discussion of cross-cultural and cross-modal considerations shows deep, thoughtful reflection on the intricacies of emotional expression across cultures and modalities",
            "The proposed applications and implications are highly innovative, relevant, and well-reasoned, showing potential for significant impact",
            "The response thoroughly addresses ethical considerations and proposes comprehensive guidelines for responsible use",
            "The writing is clear, well-structured, uses appropriate technical terminology, and demonstrates a high level of creativity and originality",
            "The response follows the required format, including section numbering and appropriate word count",
            f"The response is approximately {t['word_count']} words (±50 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
