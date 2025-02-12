import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'source_language': 'Mandarin Chinese',
                'target_language': 'Arabic',
                'context': 'Business negotiation',
                'gesture_complexity': 'High',
                'gesture_vocabulary': ['Beckoning with palm down', 'Thumb up', 'Hand slice', 'Pointing with middle finger', 'Palm-down wave']
            },
            '2': {
                'source_language': 'Spanish',
                'target_language': 'Japanese',
                'context': 'Cultural exchange event',
                'gesture_complexity': 'Medium',
                'gesture_vocabulary': ['Finger heart', 'Namaste greeting', 'Nose pointing', 'Cheek screw', 'Hand fan']
            }
        }
        return {str(i): task for i, task in enumerate(random.sample(list(tasks.values()), len(tasks)), 1)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can interpret and generate human gestures as a form of language, then apply it to facilitate communication between {t['source_language']} and {t['target_language']} speakers in a {t['context']} setting. The system should handle gestures of {t['gesture_complexity']} complexity, including but not limited to the following gesture vocabulary: {', '.join(t['gesture_vocabulary'])}.

Your response should include the following sections:

1. Gesture-Language AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for gesture interpretation and generation.
   b) Explain how your system integrates computer vision, natural language processing, and gesture synthesis.
   c) Detail any novel approaches or algorithms used in your design.
   d) Include a simple diagram or flowchart of your system's architecture (use ASCII or Unicode characters).

2. Gesture Representation and Analysis (250-300 words):
   a) Explain how your system represents and analyzes gestures, particularly those in the given gesture vocabulary.
   b) Describe how cultural differences in gestures are accounted for between {t['source_language']} and {t['target_language']}.
   c) Discuss how your system handles the temporal and spatial aspects of gestures.
   d) Explain how your system deals with gesture ambiguity and context-dependence.

3. Cross-Cultural Communication Application (250-300 words):
   a) Describe how your system would facilitate communication between {t['source_language']} and {t['target_language']} speakers.
   b) Explain how the system adapts to the {t['context']} setting.
   c) Provide an example scenario of your system in use, including at least three specific gestures from the given vocabulary and their interpretations.
   d) Discuss how your system handles {t['gesture_complexity']} complexity gestures in this context.

4. Learning and Adaptation (200-250 words):
   a) Explain how your system learns and improves its gesture interpretation and generation over time.
   b) Describe any user feedback mechanisms incorporated into your system.
   c) Discuss how your system could adapt to new cultural contexts or gesture vocabularies.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues related to using AI for cross-cultural gesture communication.
   b) Address privacy concerns and propose safeguards for user data.
   c) Explain limitations of your system and potential misunderstandings it might cause.
   d) Suggest guidelines for responsible development and use of gesture-language AI systems.

6. Future Developments and Research Directions (150-200 words):
   a) Propose potential enhancements or extensions to your system.
   b) Suggest a research question that arises from your design.
   c) Discuss how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of gesture-based communication, cultural linguistics, computer vision, and artificial intelligence. Be creative in your design while maintaining scientific plausibility and addressing real-world communication challenges. Use appropriate terminology from all relevant fields and provide clear explanations throughout your response.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of gesture-based communication, cultural linguistics, computer vision, and artificial intelligence.",
            "The proposed AI system design is innovative, well-explained, and addresses the challenges of cross-cultural gesture communication.",
            "The gesture representation and analysis approach effectively accounts for cultural differences and gesture complexities, including the specific gesture vocabulary provided.",
            "The cross-cultural communication application is well-described and provides a convincing example scenario using at least three gestures from the given vocabulary.",
            "The learning and adaptation mechanisms are clearly explained and plausible.",
            "Ethical considerations are thoughtfully addressed, with appropriate guidelines proposed for responsible use.",
            "The suggested future developments and research directions are creative and relevant.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0