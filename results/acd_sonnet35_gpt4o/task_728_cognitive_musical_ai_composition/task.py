import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"emotion": "Joy", "description": "A feeling of great pleasure and happiness"},
            {"emotion": "Melancholy", "description": "A feeling of pensive sadness, typically with no obvious cause"},
            {"emotion": "Anger", "description": "A strong feeling of annoyance, displeasure, or hostility"},
            {"emotion": "Serenity", "description": "The state of being calm, peaceful, and untroubled"}
        ]
        return {str(i+1): emotion for i, emotion in enumerate(random.sample(emotions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music to evoke the emotion of {t['emotion']} based on cognitive models of emotion and musical perception. Your task has the following parts:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system incorporates cognitive models of emotion and musical perception.
   c) Discuss how your architecture translates emotional states into musical elements.

2. Cognitive-Musical Mapping (150-200 words):
   a) Explain how your system maps the emotion of {t['emotion']} to specific musical features (e.g., tempo, key, rhythm, harmony).
   b) Describe the theoretical basis for these mappings, citing relevant research in music psychology or cognitive science.
   c) Discuss any challenges in representing {t['emotion']} musically and how your system addresses them.

3. Composition Algorithm (200-250 words):
   a) Outline the step-by-step process your AI uses to compose a piece evoking {t['emotion']}.
   b) Explain how your algorithm balances cognitive models with musical theory and creativity.
   c) Describe how your system ensures musical coherence and aesthetic quality.

4. Output Analysis (150-200 words):
   a) Provide a detailed description of a short musical piece (30-60 seconds) that your AI might compose to evoke {t['emotion']}.
   b) Analyze how specific elements of this composition relate to the cognitive and emotional models employed.
   c) Discuss how effective you believe this piece would be in evoking {t['emotion']} in human listeners.

5. Evaluation and Refinement (100-150 words):
   a) Propose a method to evaluate the effectiveness of your AI's compositions in evoking {t['emotion']}.
   b) Describe how you would use this evaluation to refine and improve your AI system.
   c) Discuss potential limitations of your approach and areas for future research.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI to compose emotion-targeted music.
   b) Consider issues such as emotional manipulation, cultural bias in musical perception, and the role of human creativity.
   c) Propose guidelines for the responsible development and use of emotion-based AI music composition systems.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all 6 required sections for the emotion of {t['emotion']}",
            "The system architecture should integrate cognitive models of emotion and musical perception",
            "The cognitive-musical mapping should be well-justified and based on relevant research",
            "The composition algorithm should balance cognitive models, musical theory, and creativity",
            "The output analysis should provide a detailed and plausible description of a composition",
            "The evaluation method and ethical considerations should be thoughtfully addressed",
            "The response should demonstrate interdisciplinary knowledge and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
