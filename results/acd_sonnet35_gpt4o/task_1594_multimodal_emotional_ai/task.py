import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "emotion": "grief",
                "context": "loss of a loved one",
                "cultural_background": "Japanese"
            },
            {
                "emotion": "joy",
                "context": "birth of a child",
                "cultural_background": "Nigerian"
            },
            {
                "emotion": "anger",
                "context": "workplace discrimination",
                "cultural_background": "American"
            },
            {
                "emotion": "pride",
                "context": "academic achievement",
                "cultural_background": "Indian"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating emotionally nuanced language across different modalities (text, speech, and non-verbal cues), then use it to analyze and respond to a complex emotional scenario involving {t['emotion']} in the context of {t['context']} for someone with a {t['cultural_background']} cultural background. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for processing and generating emotionally nuanced language across modalities.
   b) Explain how your system integrates text, speech, and non-verbal cue processing.
   c) Detail how the system incorporates cultural knowledge to interpret and generate appropriate emotional responses.
   d) Discuss any novel approaches or algorithms used in your design, particularly for emotion recognition and generation.

2. Emotional-Linguistic Framework (250-300 words):
   a) Explain how your system represents and processes emotions in language.
   b) Describe how cultural factors are integrated into the emotional-linguistic model.
   c) Detail how the system handles the interplay between verbal and non-verbal emotional cues.

3. Scenario Analysis (200-250 words):
   Using your designed system, analyze a hypothetical multimodal input (provide a brief description of text, speech, and non-verbal cues) expressing {t['emotion']} in the context of {t['context']} from a person with a {t['cultural_background']} cultural background. Explain how your system interprets the emotional state and cultural nuances.

4. Response Generation (250-300 words):
   a) Generate an appropriate multimodal response (text, speech characteristics, and non-verbal cues) to the analyzed scenario.
   b) Explain how your system determined the appropriate emotional tone and cultural considerations for the response.
   c) Discuss how the response demonstrates emotional intelligence and cultural sensitivity.

5. Evaluation and Challenges (200-250 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your system's emotional understanding and generation.
   b) Discuss potential challenges or limitations in implementing your system, particularly regarding cultural diversity and emotional complexity.
   c) Suggest areas for future research or improvement in multimodal emotional AI.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI systems that process and generate emotional content.
   b) Discuss how your system addresses concerns about privacy, manipulation, and the authenticity of AI-generated emotional responses.
   c) Propose guidelines for the responsible development and use of emotionally intelligent AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence as they relate to emotion processing. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and ethically-considered design for an AI system that effectively processes and generates emotionally nuanced language across text, speech, and non-verbal modalities, with specific consideration for the emotion of {t['emotion']} in the context of {t['context']} for a person with a {t['cultural_background']} cultural background.",
            "The emotional-linguistic framework demonstrates a deep understanding of how emotions are represented and processed in language, including cultural factors and the interplay between verbal and non-verbal cues.",
            f"The scenario analysis shows insightful interpretation of a multimodal input expressing {t['emotion']} in the given context and cultural background.",
            "The generated response demonstrates appropriate emotional tone, cultural sensitivity, and effective use of multiple modalities (text, speech, and non-verbal cues).",
            "The discussion of evaluation methods, challenges, and ethical considerations shows a nuanced understanding of the complexities involved in developing emotionally intelligent AI systems.",
            "The overall response shows a strong grasp of cognitive science, linguistics, and artificial intelligence as they relate to emotion processing, with appropriate use of technical terminology and clear explanations of complex concepts.",
            "The response adheres to the specified word count guidelines for each section and the overall submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
