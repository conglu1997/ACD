import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "emotion": "contentment",
                "cultures": ["Japanese", "Brazilian"],
                "ai_approaches": ["transformer-based", "rule-based"]
            },
            "2": {
                "emotion": "pride",
                "cultures": ["American", "Chinese"],
                "ai_approaches": ["deep learning", "knowledge-based"]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and compare two AI systems for cross-cultural emotion recognition in text, focusing on the emotion of {t['emotion']} as expressed in {t['cultures'][0]} and {t['cultures'][1]} cultures. Your task is to:

1. Briefly explain the challenges in cross-cultural emotion recognition, particularly for the emotion of {t['emotion']} (2-3 sentences).

2. Describe how {t['emotion']} is typically expressed in text in {t['cultures'][0]} and {t['cultures'][1]} cultures, highlighting key differences (3-4 sentences).

3. Propose two distinct AI architectures or approaches for recognizing {t['emotion']} across these cultures: one using a {t['ai_approaches'][0]} approach and another using a {t['ai_approaches'][1]} approach. Include at least one unique feature or component for each that addresses cultural variations (4-5 sentences per approach).

4. Compare and contrast how each AI system would handle idioms, metaphors, or culturally specific expressions related to {t['emotion']} (4-5 sentences).

5. Describe potential datasets and training approaches for each AI system, considering the need for cultural diversity and balance (3-4 sentences per system).

6. Discuss one ethical consideration for each approach in developing and deploying such AI systems, and propose mitigation strategies (2-3 sentences per approach).

7. Evaluate the strengths and weaknesses of each approach in terms of scalability to other emotions or cultures, and potential applications beyond text analysis (4-5 sentences).

Ensure your response is well-reasoned, creative, and grounded in linguistic, cultural, and AI principles. Organize your answer using clear headings for each section, and subheadings where appropriate to distinguish between the two AI approaches."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response explains challenges in cross-cultural emotion recognition",
            f"Differences in expressing {t['emotion']} between {t['cultures'][0]} and {t['cultures'][1]} cultures are described",
            f"Two distinct AI architectures are proposed: one {t['ai_approaches'][0]} and one {t['ai_approaches'][1]}, each with unique features addressing cultural variations",
            "The handling of idioms, metaphors, or culturally specific expressions is compared between the two approaches",
            "Potential datasets and training approaches are described for both AI systems",
            "Ethical considerations and mitigation strategies are discussed for both approaches",
            "The response evaluates the strengths and weaknesses of each approach in terms of scalability and potential applications",
            "The answer demonstrates understanding of linguistics, cultural studies, and AI concepts",
            "The response is well-organized with clear headings and subheadings for each section and approach"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
