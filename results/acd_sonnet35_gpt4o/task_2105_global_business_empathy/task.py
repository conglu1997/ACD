import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "Negotiating a joint venture",
                "culture_a": "Japanese",
                "culture_b": "Brazilian",
                "challenge": "Conflicting communication styles and decision-making processes"
            },
            {
                "context": "Resolving a product quality dispute",
                "culture_a": "German",
                "culture_b": "Indian",
                "challenge": "Different approaches to conflict resolution and quality standards"
            },
            {
                "context": "Implementing a global diversity initiative",
                "culture_a": "American",
                "culture_b": "Saudi Arabian",
                "challenge": "Balancing global standards with local cultural norms"
            },
            {
                "context": "Managing a cross-cultural virtual team",
                "culture_a": "Chinese",
                "culture_b": "Swedish",
                "challenge": "Overcoming differences in work styles and team dynamics"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and respond to the following cross-cultural business scenario, demonstrating high emotional intelligence and adaptive communication skills:

Context: {t['context']}
Culture A: {t['culture_a']}
Culture B: {t['culture_b']}
Challenge: {t['challenge']}

1. Cultural Analysis (200-250 words):
   a) Describe key cultural differences between {t['culture_a']} and {t['culture_b']} business cultures relevant to this scenario.
   b) Explain how these differences might contribute to the challenge described.
   c) Identify potential areas of misunderstanding or conflict.

2. Emotional Intelligence Strategy (200-250 words):
   a) Propose an approach to address the emotional aspects of this challenge.
   b) Explain how you would demonstrate empathy and build trust across cultures.
   c) Describe specific emotional intelligence techniques you would employ.

3. Communication Plan (200-250 words):
   a) Develop a communication strategy that bridges the cultural gap.
   b) Provide examples of how you would adapt your communication style for each culture.
   c) Explain how your plan addresses the specific challenge mentioned.

4. Problem-Solving Approach (200-250 words):
   a) Outline a step-by-step approach to resolve the challenge.
   b) Explain how your approach integrates cultural sensitivity and emotional intelligence.
   c) Describe potential obstacles and how you would overcome them.

5. Reflection and Learning (150-200 words):
   a) Discuss what you've learned from this scenario about cross-cultural business interactions.
   b) Explain how this experience could inform future global business strategies.
   c) Propose one way to improve cross-cultural competence in your organization.

Ensure your response demonstrates a deep understanding of both cultures, emotional intelligence principles, and effective cross-cultural communication strategies. Be specific in your examples and recommendations. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a nuanced understanding of both {t['culture_a']} and {t['culture_b']} business cultures.",
            "The emotional intelligence strategy effectively addresses the cultural challenge.",
            "The communication plan is well-adapted to both cultures and the specific context.",
            "The problem-solving approach integrates cultural sensitivity and emotional intelligence effectively.",
            "The reflection demonstrates meaningful insights and learning from the scenario.",
            "The overall response shows high levels of cultural empathy and adaptive communication skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
