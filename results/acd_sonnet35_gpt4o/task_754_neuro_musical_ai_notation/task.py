import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        music_styles = ['Classical', 'Jazz', 'Electronic']
        return {
            "1": {"music_style": random.choice(music_styles)},
            "2": {"music_style": random.choice(music_styles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate human brain activity during {t['music_style']} music perception into a novel form of musical notation. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system.
   b) Explain how the system integrates knowledge from neuroscience, linguistics, and music theory.
   c) Detail how the AI processes brain activity data and converts it into musical notation.

2. Novel Notation Design (200-250 words):
   a) Describe your proposed musical notation system.
   b) Explain how it differs from traditional notation and why it's suitable for representing neural activity.
   c) Provide an example of how a simple musical phrase would be notated in your system.

3. Neural-Musical Mapping (150-200 words):
   a) Explain how your system maps specific neural patterns to musical elements.
   b) Discuss any challenges in this mapping process and how your system addresses them.
   c) Describe how your system accounts for individual differences in brain activity and musical perception.

4. AI Learning and Adaptation (150-200 words):
   a) Describe how your AI system learns and improves its translation capabilities over time.
   b) Explain how it adapts to different musical styles and complexities.
   c) Propose a method for validating the accuracy of the AI's translations.

5. Potential Applications and Implications (150-200 words):
   a) Discuss potential applications of this technology in music composition, education, or therapy.
   b) Analyze ethical considerations related to 'reading' and translating thoughts into music.
   c) Speculate on how this technology might influence our understanding of music cognition and creativity.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, music theory, and AI principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, music theory, and AI principles.",
            "The proposed AI system and notation design are creative, innovative, and scientifically plausible.",
            "The answer addresses all required sections with appropriate detail and word count.",
            "The response shows clear interdisciplinary thinking and synthesis of knowledge from different fields.",
            f"The system design and explanation are tailored to the specific music style ({t['music_style']}) mentioned in the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
