import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'context': 'Business negotiation',
                'cultures': ['American', 'Japanese'],
                'emotion': 'frustration'
            },
            {
                'context': 'Family gathering',
                'cultures': ['Italian', 'Swedish'],
                'emotion': 'joy'
            },
            {
                'context': 'Academic debate',
                'cultures': ['British', 'Indian'],
                'emotion': 'skepticism'
            },
            {
                'context': 'Romantic relationship',
                'cultures': ['French', 'Chinese'],
                'emotion': 'affection'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of detecting and generating emotionally nuanced language across different contexts and cultures, then apply it to the following scenario:

Context: {t['context']}
Cultures: {t['cultures'][0]} and {t['cultures'][1]}
Emotion to focus on: {t['emotion']}

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for emotional language processing.
   b) Explain how your system incorporates cultural knowledge and emotional intelligence.
   c) Discuss any novel elements in your design that enable accurate detection and generation of emotionally nuanced language.

2. Emotional and Cultural Modeling (200-250 words):
   a) Explain how your system models emotional expressions in language, focusing on the given emotion.
   b) Describe how your model accounts for cultural differences in emotional expression between the two specified cultures.
   c) Discuss how your system handles potential cultural misunderstandings or conflicts related to emotional expression.

3. Scenario Application (250-300 words):
   a) Apply your AI system to the given scenario, demonstrating how it would detect and generate emotionally nuanced language.
   b) Provide example dialogues or texts showing how your system adapts its emotional expression for each culture.
   c) Explain how your system navigates potential cultural pitfalls in this specific context.

4. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI for emotional language processing and generation.
   b) Address concerns about cultural stereotyping or oversimplification of emotions.
   c) Propose guidelines for responsible development and use of emotionally intelligent AI systems.

5. Evaluation Methodology (150-200 words):
   a) Propose a method to evaluate the effectiveness and cultural appropriateness of your system's emotional language processing.
   b) Describe metrics you would use to assess both emotional accuracy and cultural sensitivity.
   c) Suggest how you would involve human experts from the relevant cultures in the evaluation process.

Ensure your response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, and natural language processing. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and technological plausibility.

Format your response using clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of emotional intelligence and its application in AI systems.",
            "The system design shows creativity and plausibility in addressing the challenge of cross-cultural emotional language processing.",
            "The scenario application provides clear, culturally-sensitive examples of the system's capabilities.",
            "Ethical considerations are thoroughly explored, with thoughtful guidelines proposed.",
            "The evaluation methodology is well-designed and considers both technical and cultural aspects."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
