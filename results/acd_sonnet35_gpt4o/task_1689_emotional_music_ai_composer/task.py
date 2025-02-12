import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"name": "Joy", "description": "A feeling of great pleasure and happiness"},
            {"name": "Melancholy", "description": "A feeling of pensive sadness, typically with no obvious cause"},
            {"name": "Anger", "description": "A strong feeling of annoyance, displeasure, or hostility"},
            {"name": "Serenity", "description": "The state of being calm, peaceful, and untroubled"}
        ]
        return {
            "1": random.choice(emotions),
            "2": random.choice(emotions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music to express the emotion of {t['name']}, described as {t['description']}. Then, analyze its output for musical and psychological coherence. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI music composition system.
   b) Explain how your system integrates knowledge of music theory, emotion psychology, and AI techniques.
   c) Detail how the system translates emotional states into musical elements (e.g., key, tempo, rhythm, melody).
   d) Discuss any novel components or algorithms specific to emotional music generation.

2. Emotion-to-Music Mapping (200-250 words):
   a) Explain how your system maps the specific emotion ({t['name']}) to musical characteristics.
   b) Provide examples of at least three musical elements and how they would be manipulated to express this emotion.
   c) Discuss how your system handles the nuances and potential ambiguities in emotional expression through music.

3. AI Composition Process (200-250 words):
   a) Describe the step-by-step process your AI uses to compose a piece of music expressing {t['name']}.
   b) Explain how the system ensures musical coherence and structure while maintaining emotional expressiveness.
   c) Discuss how your AI balances creativity and adherence to musical conventions.

4. Output Analysis (250-300 words):
   a) Propose a method to analyze the musical output of your AI system.
   b) Describe how you would evaluate the composition's effectiveness in expressing {t['name']}.
   c) Discuss potential metrics for assessing both musical quality and emotional coherence.
   d) Explain how you would validate the system's output against human-composed emotional music.

5. Psychological Implications (150-200 words):
   a) Discuss the potential psychological effects of AI-composed emotional music on listeners.
   b) Explore how this technology might be used in music therapy or mood regulation.
   c) Address any ethical considerations related to AI-generated emotional manipulation through music.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in your AI music composition system.
   b) Propose two ways to extend or improve your system in future research.
   c) Suggest a specific experiment to further explore the relationship between AI, music, and emotions.

Ensure your response demonstrates a deep understanding of music theory, emotion psychology, and AI techniques. Be creative in your approach while maintaining scientific and artistic plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of music theory, emotion psychology, and AI techniques.",
            "The system architecture is innovative, detailed, and scientifically plausible, incorporating principles from all relevant domains.",
            "The emotion-to-music mapping is well-explained and psychologically grounded.",
            "The AI composition process is clearly described and balances creativity with musical conventions.",
            "The output analysis method is comprehensive and includes both musical and psychological evaluation metrics.",
            "Psychological implications and ethical considerations are thoughtfully addressed.",
            "Limitations and future directions are insightful and demonstrate critical thinking.",
            "The response shows strong interdisciplinary reasoning, combining insights from music, psychology, and AI.",
            "The writing is clear, well-structured, and adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
