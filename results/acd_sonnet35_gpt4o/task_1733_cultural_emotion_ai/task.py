import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Japanese",
                "unique_emotion": "amae",
                "description": "A feeling of sweet dependence on someone"
            },
            {
                "name": "Danish",
                "unique_emotion": "hygge",
                "description": "A mood of coziness and comfortable conviviality with feelings of wellness and contentment"
            },
            {
                "name": "German",
                "unique_emotion": "waldeinsamkeit",
                "description": "The feeling of solitude and connectedness to nature when alone in the woods"
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze culturally-specific emotional expressions for the {t['name']} culture. Then, use this system to create a novel emotional concept for this culture. Your response should include:

1. System Design (250-300 words):
   a) Describe the key components of your AI system for generating and analyzing culturally-specific emotional expressions.
   b) Explain how your system incorporates cultural knowledge and linguistic patterns.
   c) Detail any novel techniques or algorithms used in your model.
   d) Include a brief diagram or flowchart description representing your system architecture.

2. Cultural Emotion Analysis (200-250 words):
   a) Analyze the unique emotion "{t['unique_emotion']}" ({t['description']}) in the context of {t['name']} culture.
   b) Explain how your AI system would process and represent this emotion.
   c) Discuss how this emotion reflects broader cultural values or experiences.

3. Novel Emotion Generation (200-250 words):
   a) Use your AI system to generate a novel emotional concept for the {t['name']} culture.
   b) Provide a name for this emotion (in English or the target language) and a brief definition.
   c) Explain how this new emotion relates to existing cultural values and experiences.
   d) Describe a hypothetical scenario where this emotion might be experienced.

4. Linguistic Expression (150-200 words):
   a) Explain how your AI system would generate linguistic expressions for the novel emotion.
   b) Provide three example sentences or phrases that express this new emotion in the context of {t['name']} culture.
   c) Discuss any challenges in translating or explaining this emotion to non-native speakers.

5. Evaluation and Validation (150-200 words):
   a) Propose a method to evaluate the cultural authenticity and emotional resonance of your AI-generated emotion.
   b) Describe an experiment to test whether native {t['name']} speakers can relate to and use the new emotional concept.
   c) Discuss potential biases or limitations in your approach.

6. Ethical Considerations (100-150 words):
   a) Discuss ethical implications of AI systems generating cultural emotional concepts.
   b) Consider potential positive and negative impacts on cross-cultural understanding and communication.
   c) Propose guidelines for responsible development and use of such AI systems.

Ensure your response demonstrates a deep understanding of emotions, cultural nuances, and AI systems. Be creative and innovative while maintaining cultural sensitivity and plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a deep understanding of {t['name']} culture and emotions",
            "The AI system design should be innovative yet plausible",
            "The novel emotional concept should be creative and culturally appropriate",
            "The linguistic expressions should reflect the nuances of the generated emotion",
            "Ethical considerations should be thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
