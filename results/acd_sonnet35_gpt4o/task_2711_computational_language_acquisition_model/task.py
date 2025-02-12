import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'stage': 'phonological',
                'age_range': '0-12 months',
                'key_features': ['babbling', 'phoneme recognition']
            },
            {
                'stage': 'semantic',
                'age_range': '12-18 months',
                'key_features': ['first words', 'fast mapping']
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model of language acquisition that simulates the {t['stage']} stage of language development in children aged {t['age_range']}, integrating theories from linguistics, cognitive science, and developmental psychology. Your model should focus on the key features of {', '.join(t['key_features'])}. Provide your response in the following format:

1. Theoretical Framework (250-300 words):
   a) Explain the key theories from linguistics, cognitive science, and developmental psychology that inform your model for this stage of language acquisition.
   b) Discuss how these theories interact and complement each other in explaining {t['stage']} development.
   c) Describe any debates or controversies in the field regarding this stage of language acquisition and how your model addresses them.

2. Model Architecture (300-350 words):
   a) Describe the main components of your computational model and how they interact.
   b) Explain how your model simulates the key features of {', '.join(t['key_features'])}.
   c) Discuss how your model accounts for individual differences in language acquisition.
   d) Provide a high-level diagram or flowchart of your model's architecture (describe it textually).

3. Learning Mechanisms (250-300 words):
   a) Explain the learning algorithms or mechanisms your model employs to simulate language acquisition.
   b) Describe how your model processes input data and generates output.
   c) Discuss how your model handles errors and adapts over time.

4. Environmental Factors (200-250 words):
   a) Describe how your model incorporates environmental factors that influence language acquisition.
   b) Explain how your model simulates the role of caregiver input and social interaction.
   c) Discuss how your model accounts for variations in linguistic environments.

5. Model Validation and Predictions (200-250 words):
   a) Propose methods to validate your model against empirical data on child language acquisition.
   b) Describe specific predictions your model makes about language development in the {t['stage']} stage.
   c) Discuss potential experiments or studies that could test these predictions.

6. Limitations and Future Directions (150-200 words):
   a) Identify the main limitations of your model and areas for improvement.
   b) Propose two potential extensions of your model for future research.
   c) Discuss the broader implications of your model for understanding human language acquisition and developing AI language systems.

Ensure your response demonstrates a deep understanding of language acquisition theories, computational modeling, and cognitive development. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of linguistic, cognitive, and developmental theories relevant to the specified stage of language acquisition.",
            f"The proposed model effectively simulates the key features of {', '.join(t['key_features'])} in the {t['stage']} stage of language development.",
            "The model architecture is clearly described, innovative, and scientifically plausible.",
            "The learning mechanisms and environmental factors are well-explained and grounded in current research.",
            "The response includes appropriate methods for model validation and makes specific, testable predictions.",
            "The limitations and future directions are thoughtfully considered and demonstrate a deep understanding of the field.",
            "The overall response showcases interdisciplinary knowledge integration and creative problem-solving in computational modeling of language acquisition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
