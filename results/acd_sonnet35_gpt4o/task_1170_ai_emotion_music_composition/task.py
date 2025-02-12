import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust', 'love', 'excitement']
        musical_elements = ['melody', 'harmony', 'rhythm', 'tempo', 'timbre', 'dynamics']
        genres = ['classical', 'jazz', 'rock', 'electronic', 'folk', 'hip-hop']
        
        tasks = {
            "1": {
                "emotion": random.choice(emotions),
                "musical_elements": random.sample(musical_elements, 3),
                "genre": random.choice(genres)
            },
            "2": {
                "emotion": random.choice(emotions),
                "musical_elements": random.sample(musical_elements, 3),
                "genre": random.choice(genres)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can compose music expressing the emotion of {t['emotion']} in the {t['genre']} genre, focusing on the musical elements of {', '.join(t['musical_elements'])}. Your system should also be capable of analyzing the emotional content of existing music.

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI music composition and analysis system.
   b) Explain how the system processes emotional input for composition.
   c) Detail how the system analyzes emotional content in existing music.
   d) Discuss how the system incorporates the specified musical elements and genre constraints.

2. Emotion-to-Music Mapping (250-300 words):
   a) Explain how your system translates emotions into musical features.
   b) Provide specific examples of how {t['emotion']} would be expressed in {t['genre']} using the elements {', '.join(t['musical_elements'])}.
   c) Discuss any challenges in maintaining genre authenticity while expressing emotions.

3. Machine Learning Approach (200-250 words):
   a) Describe the machine learning techniques used in your system.
   b) Explain how the system is trained on emotional and musical data.
   c) Discuss any novel AI approaches you've incorporated for music generation or analysis.

4. Music Theory Integration (200-250 words):
   a) Explain how your system incorporates music theory principles.
   b) Discuss how these principles interact with the emotion-driven composition process.
   c) Provide an example of how music theory guides the system's decisions in composing for {t['emotion']} in {t['genre']}.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the emotional accuracy of the composed music.
   b) Describe how you would validate the system's analysis of existing music.
   c) Discuss potential challenges in assessing the quality and emotional impact of AI-generated music.

6. Ethical and Creative Implications (150-200 words):
   a) Discuss the ethical considerations of using AI for emotional expression in music.
   b) Analyze the potential impact of this technology on human musicians and the music industry.
   c) Explore the philosophical question of whether AI can truly 'understand' or 'express' emotions through music.

Ensure your response demonstrates a deep understanding of both music theory and artificial intelligence. Use appropriate terminology from both fields and provide clear explanations where necessary. Be creative in your system design while maintaining scientific and artistic plausibility.

Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of music theory, particularly in relation to the {t['genre']} genre and the elements of {', '.join(t['musical_elements'])}.",
            f"The AI system design effectively incorporates methods for expressing the emotion of {t['emotion']} through music composition.",
            "The emotion-to-music mapping is well-explained and provides concrete examples.",
            "The machine learning approach is clearly described and appropriate for the task of music composition and analysis.",
            "The integration of music theory principles is well-explained and applied to the emotion-driven composition process.",
            "The proposed evaluation and validation methods are sound and address the challenges of assessing AI-generated music.",
            "The ethical and creative implications of AI music composition are thoughtfully explored."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
