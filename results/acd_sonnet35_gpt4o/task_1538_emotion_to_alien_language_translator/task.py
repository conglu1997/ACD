import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy",
            "sorrow",
            "anger",
            "fear",
            "disgust",
            "surprise",
            "trust",
            "anticipation"
        ]
        alien_traits = [
            "hive mind",
            "non-linear time perception",
            "synesthesia-like sensory integration",
            "quantum entanglement-based communication"
        ]
        return {
            "1": {
                "emotion": random.choice(emotions),
                "alien_trait": random.choice(alien_traits)
            },
            "2": {
                "emotion": random.choice(emotions),
                "alien_trait": random.choice(alien_traits)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the human emotion of {t['emotion']} into a hypothetical alien language for a species with {t['alien_trait']}. Your response should include:

1. Alien Species Description (150-200 words):
   a) Describe the alien species, focusing on their cognitive and communicative characteristics.
   b) Explain how {t['alien_trait']} influences their perception and expression of emotions.
   c) Outline any unique sensory or physiological features relevant to their communication.

2. Emotion Analysis (200-250 words):
   a) Analyze the human emotion of {t['emotion']} in terms of its psychological and physiological components.
   b) Discuss how this emotion might be perceived or experienced differently by the alien species.
   c) Identify key challenges in translating this emotion across species boundaries.

3. Translation System Design (250-300 words):
   a) Describe the architecture of your emotion-to-alien-language translation system.
   b) Explain how your system captures and processes human emotional states.
   c) Detail the method for mapping human emotions to alien language constructs.
   d) Discuss how your system accounts for the aliens' {t['alien_trait']} in its translation process.

4. Output Representation (150-200 words):
   a) Provide an example 'translation' of {t['emotion']} into the alien language.
   b) Explain the components of this translation and their significance.
   c) Describe how this representation would be perceived or understood by the alien species.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical concerns in developing cross-species emotional translation systems.
   b) Explore practical applications of this technology in fields such as xenobiology, AI, or human-computer interaction.
   c) Suggest guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and computer science principles. Be creative and original in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 900-1150 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and computer science principles.",
            "The alien species description is creative, coherent, and considers the given trait in detail.",
            "The emotion analysis is thorough and considers both human and potential alien perspectives.",
            "The translation system design is innovative, well-explained, and accounts for the aliens' unique trait.",
            "The output representation is creative and logically connected to the described system and alien characteristics.",
            "Ethical and practical implications are thoughtfully addressed.",
            "The response is within the specified word count range (900-1150 words) and includes a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
