import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        conceptual_blends = [
            {
                'concept1': 'Time',
                'concept2': 'Money',
                'blend_phrase': 'Time is money'
            },
            {
                'concept1': 'Argument',
                'concept2': 'War',
                'blend_phrase': 'Defending a position'
            },
            {
                'concept1': 'Love',
                'concept2': 'Journey',
                'blend_phrase': 'Our relationship has hit a roadblock'
            },
            {
                'concept1': 'Life',
                'concept2': 'Gambling',
                'blend_phrase': 'The odds are against us'
            },
            {
                'concept1': 'Ideas',
                'concept2': 'Food',
                'blend_phrase': 'Food for thought'
            }
        ]
        return {
            "1": random.choice(conceptual_blends),
            "2": random.choice(conceptual_blends)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the conceptual blend represented by the phrase '{t['blend_phrase']}', which combines the concepts of '{t['concept1']}' and '{t['concept2']}'.

1. Explain the conceptual blend (100-150 words):
   a) Describe how the two concepts are combined.
   b) Identify the shared structural elements between the two concepts.
   c) Explain how this blend creates new meaning or understanding.

2. Create a novel conceptual blend (100-150 words):
   a) Propose a new blend combining '{t['concept1']}' with a different concept of your choice.
   b) Explain the structural mapping between these concepts.
   c) Provide an example phrase or sentence that illustrates this new blend.

3. AI Language Model Analysis (150-200 words):
   a) Hypothesize how an AI language model might process and generate conceptual blends.
   b) Discuss potential strengths and limitations of AI models in understanding and creating conceptual blends compared to human cognition.
   c) Propose an experiment to test an AI's ability to handle conceptual blends, and predict the outcome.

4. Interdisciplinary Implications (100-150 words):
   Discuss how the study of conceptual blending in AI could inform or be applied to another field (e.g., cognitive science, linguistics, psychology, or computer science).

Ensure your response demonstrates a deep understanding of conceptual blending, linguistic creativity, and AI language models. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of conceptual blending and accurately analyzes the given blend.",
            "The novel conceptual blend is creative, well-explained, and logically sound.",
            "The AI language model analysis shows insight into both AI capabilities and limitations regarding conceptual blending.",
            "The interdisciplinary implications are thoughtful and demonstrate the ability to connect ideas across different fields.",
            "The overall response is well-structured, coherent, and demonstrates high-level analytical and creative thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
