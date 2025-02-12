import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'emotion': 'contentment',
                'primary_sense': 'visual',
                'secondary_sense': 'auditory',
                'context': 'workplace environment'
            },
            {
                'emotion': 'anxiety',
                'primary_sense': 'tactile',
                'secondary_sense': 'olfactory',
                'context': 'healthcare settings'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel human-computer interface that uses synesthesia-inspired mappings to detect and communicate the emotion of {t['emotion']}, focusing primarily on the {t['primary_sense']} sense and secondarily on the {t['secondary_sense']} sense. The interface should be designed for use in {t['context']}. Your task:

1. Emotion Analysis (100-150 words):
   a) Briefly describe the characteristics of {t['emotion']} and its importance in {t['context']}.
   b) Explain how this emotion might manifest in non-verbal cues related to the primary and secondary senses.

2. Synesthetic Mapping Design (200-250 words):
   a) Create a detailed mapping system that translates {t['emotion']} into {t['primary_sense']} and {t['secondary_sense']} experiences.
   b) Explain the rationale behind your mapping choices, considering both psychological principles and potential cultural variations.
   c) Describe how your system accounts for intensity variations of the emotion.

3. Interface Components (200-250 words):
   a) Detail the key components of your human-computer interface, including both input (emotion detection) and output (emotion communication) mechanisms.
   b) Explain how these components leverage the synesthetic mappings you designed.
   c) Describe any novel technologies or sensors your interface would require.

4. User Interaction Scenario (150-200 words):
   Provide a specific scenario of how a user would interact with your interface in {t['context']}, demonstrating both the emotion detection and communication aspects.

5. Ethical Considerations (100-150 words):
   Discuss potential ethical implications of your interface, including privacy concerns, potential for misuse, and impact on human communication skills.

6. Evaluation Method (100-150 words):
   Propose a method for evaluating the effectiveness and accuracy of your interface in detecting and communicating {t['emotion']}.

Ensure your response demonstrates a deep understanding of emotion theory, synesthesia, sensory perception, and human-computer interaction principles. Be creative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified emotion and its relevance to the given context.",
            "The synesthetic mapping design is creative, well-justified, and considers both psychological principles and cultural variations.",
            "The interface components are innovative, clearly described, and effectively leverage the synesthetic mappings.",
            "The user interaction scenario is detailed, plausible, and effectively demonstrates the interface's capabilities.",
            "Ethical considerations are thoughtfully discussed, covering relevant issues such as privacy and potential misuse.",
            "The proposed evaluation method is appropriate and well-designed for assessing the interface's effectiveness.",
            "The overall response shows interdisciplinary creativity, combining concepts from psychology, technology, and sensory perception in a novel way."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
