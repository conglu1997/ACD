import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'culture_pair': ('Japanese', 'Brazilian'),
                'emotion': 'gratitude',
                'context': 'receiving a gift from a superior'
            },
            '2': {
                'culture_pair': ('British', 'Indian'),
                'emotion': 'disagreement',
                'context': 'business negotiation'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of detecting and generating emotionally nuanced language across different cultures. Focus on the emotion of {t['emotion']} in the context of {t['context']}, comparing how it's expressed in {t['culture_pair'][0]} and {t['culture_pair'][1]} cultures. Your response should include:

1. Emotional-Linguistic Analysis (250-300 words):
   a) Describe how {t['emotion']} is typically expressed in {t['culture_pair'][0]} and {t['culture_pair'][1]} cultures, particularly in the context of {t['context']}.
   b) Analyze key linguistic features (e.g., word choice, sentence structure, idioms) that differ between these cultures in expressing this emotion.
   c) Discuss any cultural taboos or norms that might affect the expression of this emotion in each culture.
   d) Provide two example phrases or expressions for each culture that demonstrate these differences.

2. AI System Design (300-350 words):
   a) Outline the architecture of your AI system, including components for emotion detection and generation.
   b) Explain how your system would handle the cultural differences in emotional expression.
   c) Describe the training data and process you would use to make your system culturally aware.
   d) Provide a simple pseudocode snippet or flowchart illustrating how your system would process input and generate culturally appropriate output.

3. Application and Limitations (200-250 words):
   a) Propose two potential applications for your AI system in real-world scenarios.
   b) Discuss the limitations of your system and potential challenges in its implementation.
   c) Address any ethical concerns related to using AI for cross-cultural emotional communication.

4. Evaluation Method (200-250 words):
   a) Design an experiment to test the effectiveness of your AI system in accurately detecting and generating emotionally nuanced language across the specified cultures.
   b) Describe your methodology, including how you would measure success and account for cultural biases in your evaluation.
   c) Propose specific metrics or benchmarks for assessing the system's performance.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and AI principles. Be creative in your approach while maintaining scientific and technological plausibility. Format your response with clear headings for each section and subsection (e.g., 1a, 1b, etc.). Your total response should be between 950-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a nuanced understanding of how {t['emotion']} is expressed in {t['culture_pair'][0]} and {t['culture_pair'][1]} cultures, with specific examples provided for each.",
            "The AI system design is innovative, technically sound, and explicitly addresses cross-cultural emotional nuances, including a clear description of its architecture and training process.",
            "The proposed applications and limitations analysis shows a deep understanding of the challenges in cross-cultural AI communication, with specific real-world scenarios discussed.",
            "The evaluation method is well-designed, accounts for cultural differences and potential biases, and includes specific metrics or benchmarks for assessing performance.",
            "The response adheres to the specified format and word count, with clear headings and subheadings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0