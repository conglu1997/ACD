import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            {
                "name": "Quantum Semantics",
                "description": "Words have probabilistic meanings, allowing for multiple interpretations simultaneously"
            },
            {
                "name": "Temporal Flexibility",
                "description": "Grammar that can express past, present, and future simultaneously"
            },
            {
                "name": "Emotion Encoding",
                "description": "Incorporate emotional states directly into the language structure"
            },
            {
                "name": "Algorithmic Syntax",
                "description": "Sentence structures based on programming paradigms"
            }
        ]
        societal_aspects = [
            "Privacy and data protection",
            "Cultural preservation and evolution",
            "Cognitive enhancement and augmentation",
            "Social dynamics and power structures"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "language_feature": random.choice(language_features),
                "societal_aspect": random.choice(societal_aspects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical future language optimized for AI-human communication, incorporating the following feature:

{t['language_feature']['name']}: {t['language_feature']['description']}

Your task is to create a detailed proposal for this language and analyze its potential impact on society, particularly in relation to {t['societal_aspect']}. Include the following in your response:

1. Language Design (250-300 words):
   a) Explain how you will implement the given feature in your language.
   b) Describe at least two additional features of your language that complement the given feature and enhance AI-human communication.
   c) Provide examples of how your language would express complex ideas or scenarios.
   d) Explain how your language differs from existing human and programming languages.

2. AI-Human Interaction Analysis (200-250 words):
   a) Discuss how your language facilitates improved communication between AIs and humans.
   b) Analyze potential challenges in adoption and learning of this language for both AIs and humans.
   c) Explain how your language might influence AI development and human-AI collaboration.

3. Linguistic Analysis (150-200 words):
   a) Compare your designed language to existing linguistic theories or constructed languages.
   b) Discuss how your language challenges or extends current understanding of language structure and function.
   c) Propose a method for evaluating the effectiveness of your language in AI-human communication.

4. Societal Impact (200-250 words):
   a) Analyze the potential impact of your language on {t['societal_aspect']}.
   b) Discuss both positive and negative consequences of widespread adoption of your language.
   c) Propose guidelines or policies to address potential issues arising from the use of your language.

5. Future Implications (100-150 words):
   a) Predict how your language might evolve over time as AI capabilities advance.
   b) Discuss potential long-term effects on human cognition and society.
   c) Propose an area of research that could further enhance AI-human communication based on your language design.

Ensure your response demonstrates a deep understanding of linguistics, AI capabilities, and societal dynamics. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology throughout your answer.

Format your response with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed language design with the specified feature and at least two additional features",
            "The response analyzes AI-human interaction facilitated by the designed language",
            "The response includes a linguistic analysis comparing the designed language to existing theories or constructed languages",
            "The response analyzes the societal impact of the language, focusing on the specified aspect",
            "The response discusses future implications and proposes relevant research areas",
            "The response demonstrates creativity and scientific plausibility in the language design",
            "The response is well-structured with clear headings and falls within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
