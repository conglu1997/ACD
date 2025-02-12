import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            'Sehnsucht (German: a deep longing for something unattainable)',
            'Saudade (Portuguese: a melancholic longing for an absent something or someone)',
            'Hygge (Danish: a mood of coziness and comfortable conviviality)',
            'Wabi-sabi (Japanese: a worldview centered on the acceptance of transience and imperfection)'
        ]
        musical_styles = [
            'Western classical',
            'Indian classical (Hindustani)',
            'West African polyrhythmic',
            'Chinese traditional'
        ]
        cultures = [
            'Brazilian',
            'Korean',
            'Egyptian',
            'Finnish'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'emotion': random.choice(emotions),
                'musical_style': random.choice(musical_styles),
                'target_culture': random.choice(cultures)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates the complex human emotional state of {t['emotion']} into a musical composition in the style of {t['musical_style']}, considering the perception and expression of this emotion in {t['target_culture']} culture. Your response should include the following sections, clearly labeled and within the specified word limits:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system processes emotional input and generates musical output.
   c) Detail how cultural context is incorporated into the system's decision-making process.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Emotion-Music Translation Mechanism (200-250 words):
   a) Explain how your system translates the given emotion into musical elements (e.g., melody, harmony, rhythm, timbre).
   b) Describe how the system incorporates the specified musical style in its output.
   c) Discuss any novel algorithms or techniques used in this translation process.

3. Cultural Adaptation (200-250 words):
   a) Explain how your system adapts its output to reflect the target culture's musical traditions and emotional expressions.
   b) Provide an example of how the output might differ if adapted for a different culture.
   c) Discuss challenges in maintaining emotional authenticity across cultures.

4. Training and Data Considerations (150-200 words):
   a) Describe the type of data your system would need to be trained on.
   b) Explain how you would ensure diverse cultural representation in the training data.
   c) Discuss potential biases and how you would mitigate them.

5. Evaluation Metrics (100-150 words):
   a) Propose methods to evaluate the effectiveness of your system's emotion-to-music translations.
   b) Describe how you would validate the cultural appropriateness of the generated music.

6. Potential Applications and Ethical Considerations (150-200 words):
   a) Suggest two potential applications of your system beyond music composition.
   b) Discuss ethical implications of translating emotions into music across cultures.
   c) Propose guidelines for responsible development and use of emotion-to-music AI systems.

Ensure your response demonstrates a deep understanding of musicology, psychology, cultural studies, and AI system design. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your response will be evaluated based on the depth of understanding shown, the innovation and plausibility of your proposed system, the thoroughness of your discussion on cultural adaptation and ethical considerations, and the clarity and structure of your writing."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of musicology, psychology, cultural studies, and AI system design as applied to translating {t['emotion']} into {t['musical_style']} music for {t['target_culture']} culture.",
            "The proposed system architecture and emotion-music translation mechanism are innovative yet plausible, with clear reasoning provided.",
            "The discussion on cultural adaptation shows a nuanced understanding of cross-cultural differences in music and emotion.",
            "The training data considerations and evaluation metrics are well-thought-out and address potential biases.",
            "The response includes a thorough discussion of ethical implications and responsible development guidelines.",
            "The writing is clear, well-structured, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
