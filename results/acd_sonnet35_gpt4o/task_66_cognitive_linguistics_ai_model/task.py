import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_principle': 'Embodied cognition',
                'linguistic_feature': 'Metaphorical mapping',
            },
            {
                'cognitive_principle': 'Prototype theory',
                'linguistic_feature': 'Radial categories',
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language model based on cognitive linguistics principles and analyze its potential impact on AI development and human-AI interaction. Use the following specifications:

Cognitive Principle: {t['cognitive_principle']}
Linguistic Feature: {t['linguistic_feature']}

Your task:
1. Briefly explain the given cognitive principle and linguistic feature (2-3 sentences each).
2. Design a hypothetical language model that incorporates these concepts. Describe its key components and functioning (4-5 sentences).
3. Provide two specific examples of how your model would process and generate language differently from traditional NLP models.
4. Analyze how this model could potentially improve AI's understanding of human language and thought processes (3-4 sentences).
5. Discuss possible challenges in implementing this model and how they might be addressed (2-3 sentences).
6. Explore the ethical implications of using such a model in AI systems, particularly in human-AI interaction (3-4 sentences).

Format your response as follows:

Concept Explanation:
[Your explanation of the cognitive principle and linguistic feature]

Model Design:
[Your description of the hypothetical language model]

Processing Examples:
1. [First example]
2. [Second example]

AI Understanding Analysis:
[Your analysis of potential improvements]

Implementation Challenges:
[Your discussion of challenges and potential solutions]

Ethical Implications:
[Your exploration of ethical considerations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the cognitive principle and linguistic feature is accurate and clear.",
            "The hypothetical language model design incorporates the given concepts in a creative and logical manner.",
            "The processing examples demonstrate a clear difference from traditional NLP models.",
            "The analysis of AI understanding improvements is insightful and well-reasoned.",
            "The discussion of implementation challenges and solutions is practical and thoughtful.",
            "The exploration of ethical implications is nuanced and considers multiple perspectives.",
            "The overall response demonstrates a deep understanding of cognitive linguistics and its potential applications in AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
