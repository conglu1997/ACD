import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_stage': 'Sensorimotor',
                'age_equivalent': '0-2 years',
                'key_features': ['object permanence', 'goal-directed behavior', 'imitation'],
                'linguistic_focus': ['phoneme recognition', 'basic word association']
            },
            {
                'cognitive_stage': 'Preoperational',
                'age_equivalent': '2-7 years',
                'key_features': ['symbolic thinking', 'egocentrism', 'intuitive reasoning'],
                'linguistic_focus': ['vocabulary expansion', 'simple grammar', 'narrative formation']
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language learning curriculum for an AI system that simulates the {t['cognitive_stage']} stage of cognitive development (human age equivalent: {t['age_equivalent']}).

Your curriculum should address the following:

1. Learning Objectives (100-150 words):
   Outline 3-5 specific language learning objectives appropriate for this cognitive stage. Consider both the key cognitive features and linguistic focus areas provided:
   - Key cognitive features: {', '.join(t['key_features'])}
   - Linguistic focus: {', '.join(t['linguistic_focus'])}

2. Learning Activities (200-250 words):
   Describe 2-3 innovative learning activities or exercises that would help the AI system achieve the outlined objectives. Explain how each activity relates to the cognitive features and linguistic focus of this stage.

3. Assessment Methods (100-150 words):
   Propose 2-3 methods to assess the AI system's language acquisition progress at this stage. Explain how these methods align with the cognitive and linguistic characteristics of the stage.

4. Ethical Considerations (100-150 words):
   Discuss potential ethical implications or challenges that might arise when simulating this stage of language acquisition in an AI system. Consider issues related to data collection, privacy, and the potential impact on AI development.

5. Comparative Analysis (150-200 words):
   Compare and contrast your proposed AI language acquisition approach with theories of human language acquisition at this stage. Discuss potential advantages or limitations of applying human developmental models to AI systems.

Ensure your curriculum is creative, theoretically grounded, and considers the unique capabilities and limitations of AI systems compared to human learners. Your response should demonstrate a deep understanding of both cognitive development theories and AI learning processes.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The curriculum appropriately addresses the {t['cognitive_stage']} stage of cognitive development.",
            "Learning objectives and activities align with the provided cognitive features and linguistic focus areas.",
            "The response demonstrates a deep understanding of both cognitive development theories and AI learning processes.",
            "The curriculum is creative and considers the unique capabilities and limitations of AI systems compared to human learners.",
            "All sections (Learning Objectives, Learning Activities, Assessment Methods, Ethical Considerations, and Comparative Analysis) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
