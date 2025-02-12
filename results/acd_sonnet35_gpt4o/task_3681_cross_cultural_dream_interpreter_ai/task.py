import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'culture1': 'Japanese',
                'culture2': 'Aztec',
                'dream_theme': 'Flying',
                'psychological_aspect': 'Personal growth'
            },
            '2': {
                'culture1': 'Aboriginal Australian',
                'culture2': 'Nordic',
                'dream_theme': 'Water',
                'psychological_aspect': 'Emotional processing'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and interpreting dreams across different cultures, incorporating principles of cognitive science, cultural anthropology, and dream psychology. Then, apply your system to interpret a dream with the theme of {t['dream_theme']} in the context of {t['culture1']} and {t['culture2']} cultures, focusing on the psychological aspect of {t['psychological_aspect']}.

Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for cross-cultural dream interpretation.
   b) Explain how your system integrates knowledge from cognitive science, cultural anthropology, and dream psychology.
   c) Detail any novel techniques or algorithms used in your model.

2. Cultural Knowledge Representation (200-250 words):
   a) Explain how your system represents and utilizes cultural knowledge relevant to dream interpretation.
   b) Describe the process of acquiring and updating cultural information in your system.
   c) Discuss how your system handles conflicting or evolving cultural interpretations.

3. Dream Analysis Process (250-300 words):
   a) Outline the step-by-step process your AI system uses to analyze and interpret a dream.
   b) Explain how your system incorporates the specified psychological aspect into its interpretation.
   c) Describe how your system accounts for individual differences in dreamers while maintaining cultural relevance.

4. Cross-Cultural Comparison (200-250 words):
   a) Apply your AI system to interpret the given dream theme in the context of the two specified cultures.
   b) Provide a comparative analysis of the interpretations, highlighting similarities and differences.
   c) Explain how your system reconciles potentially conflicting cultural interpretations.

5. Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the accuracy and cultural sensitivity of your AI system's dream interpretations.
   b) Discuss potential biases in your system and how to mitigate them.
   c) Suggest how human experts could be integrated into the validation process.

6. Ethical Considerations (100-150 words):
   a) Discuss ethical implications of AI-driven dream interpretation across cultures.
   b) Address concerns about privacy, cultural appropriation, and the potential impact on traditional dream interpretation practices.
   c) Propose guidelines for the responsible use of your AI system.

7. Future Applications and Research Directions (150-200 words):
   a) Suggest potential applications of your system in fields such as mental health, cultural studies, or personal development.
   b) Propose future research directions to enhance AI-driven dream interpretation and cross-cultural understanding.
   c) Discuss how your system might contribute to our scientific understanding of dreams and cultural cognition.

Ensure your response demonstrates a deep understanding of cognitive science, cultural anthropology, dream psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with clear headings.",
            "The AI system design integrates knowledge from cognitive science, cultural anthropology, and dream psychology.",
            "The cultural knowledge representation and dream analysis process are well-explained and plausible.",
            "The cross-cultural comparison provides a thoughtful analysis of the given dream theme in the two specified cultures.",
            "The response addresses ethical considerations and future applications of the AI system.",
            "The total response is between 1300-1650 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0