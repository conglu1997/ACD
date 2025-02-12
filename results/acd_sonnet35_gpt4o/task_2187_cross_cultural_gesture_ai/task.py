import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "gesture_type": "Greeting",
                "source_culture": "Japanese",
                "target_culture": "Brazilian"
            },
            {
                "gesture_type": "Expressing disagreement",
                "source_culture": "Italian",
                "target_culture": "Thai"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of interpreting and generating culturally appropriate gestures for non-verbal communication across different cultures. Focus on the gesture type of {t['gesture_type']}, translating from {t['source_culture']} culture to {t['target_culture']} culture. Your response should include:

1. Gesture Analysis (200-250 words):
   a) Describe the typical gesture for {t['gesture_type']} in the {t['source_culture']} culture.
   b) Explain the cultural significance and nuances of this gesture.
   c) Describe the equivalent or most appropriate gesture for {t['gesture_type']} in the {t['target_culture']} culture.
   d) Discuss any potential misunderstandings or faux pas that could arise from using the source culture's gesture in the target culture.

2. AI System Architecture (300-350 words):
   a) Propose a high-level architecture for an AI system that can interpret the source gesture and generate an appropriate target gesture.
   b) Explain how your system would process visual input to recognize gestures.
   c) Describe the components needed for cultural context understanding and gesture translation.
   d) Discuss how your system would generate and potentially animate the output gesture.
   e) Include a diagram or flowchart of your proposed architecture (describe it textually).

3. Data and Training (200-250 words):
   a) Describe the types of data your AI system would need for training.
   b) Explain potential challenges in data collection and annotation for this task.
   c) Propose methods to ensure cultural sensitivity and accuracy in your training data.
   d) Discuss any ethical considerations in collecting and using this type of data.

4. Embodied Cognition Integration (200-250 words):
   a) Explain how principles of embodied cognition could enhance your AI system's performance.
   b) Describe how your system might model the physical and cognitive aspects of gesture production.
   c) Discuss potential benefits and challenges of incorporating embodied cognition in gesture AI.

5. Cross-cultural Adaptation (150-200 words):
   a) Propose a method for your AI system to adapt to new cultures not included in its initial training.
   b) Discuss how your system might handle gestures with no direct equivalent in the target culture.
   c) Explain how your system could maintain cultural sensitivity while generalizing across cultures.

6. Evaluation and Testing (150-200 words):
   a) Propose methods to evaluate your AI system's performance in gesture translation.
   b) Describe potential experiments to test the system's cultural appropriateness and accuracy.
   c) Discuss how you would involve human experts in the evaluation process.

7. Practical Applications and Implications (150-200 words):
   a) Suggest two practical applications for your gesture translation AI system.
   b) Discuss potential societal impacts of widespread use of such technology.
   c) Address any ethical concerns related to AI-mediated cross-cultural communication.

Ensure your response demonstrates a deep understanding of non-verbal communication, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and length.",
            f"The AI system design effectively addresses the gesture type of {t['gesture_type']}, translating from {t['source_culture']} culture to {t['target_culture']} culture.",
            "The response demonstrates a deep understanding of non-verbal communication, cultural anthropology, and artificial intelligence principles.",
            "The proposed AI system architecture is innovative, well-explained, and plausible.",
            "The response shows careful consideration of ethical implications and cultural sensitivity throughout all sections.",
            "The evaluation methods and practical applications proposed are thoughtful, relevant, and culturally appropriate.",
            "The response demonstrates a nuanced understanding of the cultural differences between the source and target cultures in relation to the specific gesture type."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
