import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotion_modalities = [
            {"source": "Text", "target": "Music"},
            {"source": "Facial Expression", "target": "Color Palette"},
            {"source": "Body Language", "target": "Abstract Art"},
            {"source": "Voice Tone", "target": "Tactile Sensation"}
        ]
        emotions = ["Joy", "Sadness", "Anger", "Fear", "Disgust", "Surprise", "Contempt", "Love"]
        return {
            "1": {
                "modalities": random.choice(emotion_modalities),
                "emotion": random.choice(emotions)
            },
            "2": {
                "modalities": random.choice(emotion_modalities),
                "emotion": random.choice(emotions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the emotional content of {t['emotion']} from {t['modalities']['source']} to {t['modalities']['target']}, analyze the implications for AI emotional intelligence, and design an experiment to test AI emotional understanding. Your response should include:

1. Emotional Translation (200-250 words):
   a) Describe a specific instance of {t['emotion']} expressed through {t['modalities']['source']}.
   b) Translate this emotional content into {t['modalities']['target']}, providing a detailed description of your translation.
   c) Explain your rationale for the translation, highlighting key emotional elements preserved or transformed.

2. AI Emotional Intelligence Analysis (200-250 words):
   a) Discuss the challenges an AI might face in performing this type of emotional translation.
   b) Analyze how developing this capability could enhance AI emotional intelligence.
   c) Explore potential applications and ethical considerations of AI systems with advanced emotional translation abilities.

3. Experiment Design (250-300 words):
   Design an experiment to test an AI system's ability to understand and translate emotions between {t['modalities']['source']} and {t['modalities']['target']}. Include:
   a) Hypothesis
   b) Methodology
   c) Data collection and analysis procedures
   d) Expected results and their implications
   e) Potential limitations and ethical considerations

4. Reflection on Human Emotion (100-150 words):
   a) Compare the process of emotional translation between modalities for humans versus AI systems.
   b) Discuss what this comparison reveals about the nature of human emotion and cognition.

Ensure your response demonstrates a deep understanding of emotional expression, cross-modal translation, and AI development challenges. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of emotional expression in both {t['modalities']['source']} and {t['modalities']['target']}.",
            "The emotional translation is creative, detailed, and preserves key emotional elements.",
            "The analysis of AI emotional intelligence challenges and potential is insightful and well-reasoned.",
            "The experimental design is well-structured, feasible, and directly addresses the challenge of AI emotional understanding.",
            "The reflection on human emotion shows depth of thought and connects well with the broader themes of the task.",
            "The overall response shows a strong grasp of emotional intelligence, cross-modal translation, and AI development principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
