import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_domain': 'spatial relations',
                'ai_application': 'visual scene understanding'
            },
            {
                'cognitive_domain': 'causality',
                'ai_application': 'predictive text generation'
            },
            {
                'cognitive_domain': 'theory of mind',
                'ai_application': 'conversational AI'
            }
        ]
        return {str(i+1): random.choice(tasks) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a system to enhance AI language models using conceptual primitives derived from cognitive linguistics and developmental psychology. Focus on the cognitive domain of {t['cognitive_domain']} and its application to {t['ai_application']}. Your response should include:

1. Conceptual Primitives Analysis (250-300 words):
   a) Explain the concept of conceptual primitives in cognitive science and linguistics.
   b) Identify and describe 3-5 key conceptual primitives related to {t['cognitive_domain']}.
   c) Discuss how these primitives develop in human cognition, citing relevant research.

2. AI Enhancement Framework (300-350 words):
   a) Propose a framework for incorporating these conceptual primitives into AI language models.
   b) Explain how this framework could enhance {t['ai_application']}.
   c) Describe the potential advantages of this approach over current AI methodologies.
   d) Address potential challenges or limitations of implementing this framework.

3. Implementation Strategy (200-250 words):
   a) Outline a step-by-step approach for implementing your framework in an AI system.
   b) Suggest specific algorithms or techniques that could be used.
   c) Propose a method for evaluating the effectiveness of your enhanced AI system.

4. Interdisciplinary Implications (150-200 words):
   a) Discuss how your framework might contribute to our understanding of human cognition.
   b) Explore potential applications of this approach in fields beyond AI (e.g., education, psychology, linguistics).

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to implementing cognitive primitives in AI systems.
   b) Propose guidelines for responsible development and use of this technology.

6. Future Research Directions (100-150 words):
   a) Suggest 2-3 areas for further research that could build on your framework.
   b) Explain how these research directions could advance both AI and cognitive science.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific accuracy and addressing potential limitations or challenges. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual primitives in cognitive science and linguistics.",
            "The proposed AI enhancement framework is innovative, well-explained, and relevant to the given cognitive domain and AI application.",
            "The implementation strategy is clear, feasible, and addresses potential challenges.",
            "The response effectively explores interdisciplinary implications and ethical considerations.",
            "The suggested future research directions are insightful and have the potential to advance both AI and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
