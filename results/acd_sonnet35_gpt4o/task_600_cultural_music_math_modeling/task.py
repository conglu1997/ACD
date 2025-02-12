import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Japanese', 'Brazilian', 'Egyptian', 'Irish']
        emotions = ['joy to sorrow', 'fear to courage', 'anger to serenity', 'anticipation to surprise']
        return {
            "1": {"culture": random.choice(cultures), "emotion_journey": random.choice(emotions)},
            "2": {"culture": random.choice(cultures), "emotion_journey": random.choice(emotions)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a mathematical model for analyzing and generating music based on cultural emotional patterns, focusing on {t['culture']} music. Then use your model to compose a short piece representing the emotional journey from {t['emotion_journey']}.

Your response should include:

1. Model Design (300-350 words):
   a) Describe the key components of your mathematical model.
   b) Explain how your model incorporates {t['culture']} musical elements.
   c) Detail how your model represents and transitions between emotions.
   d) Include at least one mathematical formula or algorithm used in your model.

2. Cultural Analysis (200-250 words):
   a) Analyze how {t['culture']} music traditionally expresses emotions.
   b) Explain how your model captures these cultural nuances.
   c) Discuss any challenges in mathematically representing cultural emotional patterns.

3. Composition Process (200-250 words):
   a) Describe how you used your model to compose a piece representing {t['emotion_journey']}.
   b) Explain key decision points in the composition process.
   c) Discuss how the model influenced the structure and elements of the piece.

4. Musical Notation and Analysis (150-200 words):
   a) Provide a brief musical notation or description of your composed piece.
   b) Analyze how specific elements in the piece reflect the emotional journey.
   c) Explain how {t['culture']} musical characteristics are evident in the composition.

5. Reflection and Potential Applications (100-150 words):
   a) Discuss the strengths and limitations of your model.
   b) Propose potential applications of this model in music therapy or cross-cultural communication.
   c) Suggest how this model could be expanded or improved in future iterations.

Ensure your response demonstrates a deep understanding of music theory, mathematical modeling, and {t['culture']} cultural elements. Be creative in your approach while maintaining scientific and cultural authenticity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed mathematical model incorporating {t['culture']} musical elements and emotional representations.",
            f"The cultural analysis should demonstrate a deep understanding of how {t['culture']} music traditionally expresses emotions.",
            f"The composition process should clearly explain how the model was used to create a piece representing the journey from {t['emotion_journey']}.",
            "The musical notation or description should be coherent and reflect the intended emotional journey.",
            "The reflection should provide insightful analysis of the model's strengths, limitations, and potential applications.",
            "The overall response should demonstrate interdisciplinary knowledge application and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
