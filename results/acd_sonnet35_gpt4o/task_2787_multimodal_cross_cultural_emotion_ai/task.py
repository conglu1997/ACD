import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = ['text', 'speech', 'facial expressions']
        cultures = ['Western', 'East Asian', 'Middle Eastern', 'African']
        emotions = ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise']
        applications = ['mental health support', 'cross-cultural communication', 'social robotics', 'content moderation']
        
        tasks = {}
        for i in range(1, 3):
            culture1 = random.choice(cultures)
            culture2 = random.choice([c for c in cultures if c != culture1])
            tasks[str(i)] = {
                "modality": random.choice(modalities),
                "culture1": culture1,
                "culture2": culture2,
                "emotion": random.choice(emotions),
                "application": random.choice(applications)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating emotional content in {t['modality']}, focusing on the emotion of {t['emotion']} across {t['culture1']} and {t['culture2']} cultures. Your system should be applicable to {t['application']}. Provide a comprehensive response addressing the following points:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for emotion analysis and generation.
   b) Explain how your system integrates knowledge from linguistics, psychology, and neuroscience.
   c) Detail the mechanisms used for cross-cultural emotional interpretation and expression.
   d) Discuss how your system handles the specific modality ({t['modality']}) for both analysis and generation.

2. Cross-Cultural Emotion Model (200-250 words):
   a) Describe how your system represents emotional states and their cultural variations.
   b) Explain the techniques used to map emotions between {t['culture1']} and {t['culture2']} cultures.
   c) Discuss how your model accounts for cultural differences in emotional expression and interpretation.
   d) Address potential biases in your model and how you mitigate them.

3. Multimodal Integration (if applicable) (150-200 words):
   a) Explain how your system could be extended to integrate other modalities beyond {t['modality']}.
   b) Discuss the challenges and benefits of multimodal emotion analysis and generation.
   c) Propose a method for resolving conflicts between emotional cues in different modalities.

4. Emotion Generation Example (200-250 words):
   a) Provide an example of how your system would generate content expressing {t['emotion']} in {t['modality']} for both {t['culture1']} and {t['culture2']} cultures.
   b) Explain the key differences in the generated content for each culture.
   c) Discuss how these differences reflect cultural variations in emotional expression.

5. Application in {t['application']} (150-200 words):
   a) Describe how your emotion AI system could be applied in the field of {t['application']}.
   b) Discuss the potential benefits and challenges of using your system in this context.
   c) Propose a specific use case or scenario demonstrating the system's value.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to cross-cultural emotion AI.
   b) Discuss how your system addresses concerns about privacy, consent, and cultural sensitivity.
   c) Propose guidelines for the responsible development and use of emotion AI technologies.

7. Evaluation and Validation (150-200 words):
   a) Describe methods for evaluating the accuracy and cultural appropriateness of your system.
   b) Propose an experiment to validate your system's performance across cultures.
   c) Discuss the challenges in creating a 'ground truth' for cross-cultural emotion AI.

8. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your emotion AI system.
   b) Discuss how these enhancements could advance our understanding of emotions and culture.

Ensure your response demonstrates a deep understanding of emotion theory, cross-cultural psychology, and artificial intelligence. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical considerations.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of emotion theory, cross-cultural psychology, and artificial intelligence.",
            "The system architecture is well-designed and clearly explains how emotion analysis and generation are implemented across cultures.",
            "The cross-cultural emotion model effectively addresses cultural variations in emotional expression and interpretation.",
            "The emotion generation example clearly illustrates cultural differences in expressing the specified emotion.",
            "The application of the AI system to the specified area is well-explained and includes a concrete use case.",
            "Ethical considerations are thoroughly addressed, including privacy, consent, and cultural sensitivity.",
            "The evaluation and validation methods are appropriate and address the challenges of cross-cultural emotion AI.",
            "Future directions are innovative and well-reasoned.",
            "The response is creative and demonstrates effective interdisciplinary knowledge integration.",
            "The response follows the required format, including section headings, and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
