import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust', 'contempt', 'anticipation']
        musical_elements = ['melody', 'harmony', 'rhythm', 'tempo', 'dynamics', 'timbre']
        ai_approaches = ['neural networks', 'symbolic AI', 'evolutionary algorithms', 'fuzzy logic', 'bayesian networks']
        
        tasks = {
            "1": {
                "emotion": random.choice(emotions),
                "musical_element": random.choice(musical_elements),
                "ai_approach": random.choice(ai_approaches)
            },
            "2": {
                "emotion": random.choice(emotions),
                "musical_element": random.choice(musical_elements),
                "ai_approach": random.choice(ai_approaches)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate emotional states between music and natural language, focusing on the emotion of {t['emotion']}, the musical element of {t['musical_element']}, and using {t['ai_approach']} as the primary AI approach. Your response should include:

1. Emotion-Music Mapping (200-250 words):
   a) Analyze how the emotion {t['emotion']} is typically expressed in music, particularly through {t['musical_element']}.
   b) Provide specific musical examples or patterns that convey this emotion.
   c) Explain how cultural differences might affect this emotion-music mapping.

2. AI System Design (250-300 words):
   a) Describe the overall architecture of your AI system for emotion-music translation.
   b) Explain how you would implement {t['ai_approach']} to perform this task.
   c) Provide a detailed architecture diagram or pseudocode for your system.
   d) Detail how your system would process and represent both musical and linguistic inputs/outputs.

3. Translation Process (200-250 words):
   a) Describe step-by-step how your AI system would translate a given emotional state into a musical expression, focusing on {t['musical_element']}.
   b) Explain the reverse process: how it would interpret the emotion from a musical piece based on {t['musical_element']}.
   c) Provide a concrete example of translating the emotion {t['emotion']} into musical elements and vice versa.
   d) Discuss how your system would handle ambiguity or mixed emotions.

4. Evaluation Metrics (150-200 words):
   a) Propose metrics to evaluate the accuracy and effectiveness of your emotion-music translation system.
   b) Describe an experiment to test your system's performance, including methodology and expected outcomes.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications or concerns related to AI systems interpreting and generating emotional content.
   b) Propose guidelines for responsible development and use of such systems.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how this AI system could contribute to research in musicology, psychology, or affective computing.
   b) Suggest potential applications of this technology in fields such as music therapy, entertainment, or human-computer interaction.

Ensure your response demonstrates a deep understanding of music theory, emotional psychology, and artificial intelligence. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately analyzes how {t['emotion']} is expressed through {t['musical_element']} in music, with specific examples",
            f"The AI system design effectively incorporates {t['ai_approach']} for emotion-music translation, including a detailed architecture diagram or pseudocode",
            "The translation process is clearly explained for both emotion-to-music and music-to-emotion directions, with a concrete example provided",
            "Appropriate evaluation metrics and a well-designed experimental methodology are proposed",
            "Ethical considerations and guidelines are thoughtfully discussed, addressing potential implications",
            "Interdisciplinary implications and potential applications are explored creatively and plausibly",
            "The response demonstrates deep understanding of music theory, emotional psychology, and artificial intelligence",
            "The submission is well-structured, clear, and within the specified word count range of 1050-1350 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
