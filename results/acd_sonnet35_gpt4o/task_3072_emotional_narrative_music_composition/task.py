import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        narratives = [
            'overcoming adversity',
            'falling in love',
            'losing a loved one',
            'achieving a lifelong dream',
            'confronting a fear',
            'experiencing betrayal'
        ]
        musical_styles = ['classical', 'jazz', 'electronic', 'folk', 'rock', 'ambient']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'emotion': random.choice(emotions),
                'narrative': random.choice(narratives),
                'musical_style': random.choice(musical_styles)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze musical compositions conveying specific emotional narratives. Your system should bridge the gap between linguistic expression and musical communication. For this task, focus on the following parameters:

Emotion: {t['emotion']}
Narrative: {t['narrative']}
Musical Style: {t['musical_style']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating emotionally narrative music.
   b) Explain how your system integrates linguistic understanding, emotional processing, and musical composition.
   c) Detail the process of translating a narrative and emotion into musical elements.
   d) Discuss how your system incorporates the specified musical style.

2. Composition Generation (250-300 words):
   a) Explain how your AI would generate a musical composition for the given emotion, narrative, and style.
   b) Describe specific musical elements (e.g., tempo, key, instrumentation) your system would use to convey the emotion and narrative.
   c) Provide a high-level representation of the generated composition (e.g., a verbal description or a simplified musical notation).

3. Analysis and Interpretation (250-300 words):
   a) Describe how your AI system would analyze and interpret the emotional content and narrative of a given musical composition.
   b) Explain the features or patterns your system would look for to identify emotions and narrative elements in music.
   c) Discuss how your system would handle ambiguity or multiple interpretations in musical expression.

4. Cross-modal Evaluation (200-250 words):
   a) Propose a method for evaluating the effectiveness of your system in conveying emotions and narratives through music.
   b) Describe an experiment to compare human and AI interpretations of emotionally narrative music.
   c) Discuss potential applications of this technology in fields such as music therapy, film scoring, or cross-cultural communication.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues in using AI for emotional expression through music.
   b) Discuss limitations of your approach and potential biases in emotional interpretation.
   c) Propose guidelines for responsible development and use of emotion-generating AI in musical contexts.

Ensure your response demonstrates a deep understanding of music theory, emotional psychology, and artificial intelligence. Use appropriate terminology from these fields and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Your total response should be between 1200-1400 words. Use clear headings for each section in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of music theory, emotional psychology, and artificial intelligence.",
            "The system architecture effectively integrates linguistic understanding, emotional processing, and musical composition.",
            f"The composition generation process clearly incorporates the given emotion ({t['emotion']}), narrative ({t['narrative']}), and musical style ({t['musical_style']}).",
            "The analysis and interpretation section provides a plausible method for identifying emotions and narrative elements in music.",
            "The cross-modal evaluation proposal is well-thought-out and scientifically sound.",
            "Ethical considerations and limitations are thoroughly discussed with responsible guidelines proposed.",
            "The response is well-structured, addressing all required points comprehensively.",
            "The proposed system demonstrates creativity and innovation while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
