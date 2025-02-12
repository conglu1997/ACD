import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotion_dimensions = [
            "valence",
            "arousal",
            "dominance",
            "predictability"
        ]
        linguistic_features = [
            "lexical choice",
            "syntactic structure",
            "prosody",
            "pragmatics"
        ]
        cognitive_processes = [
            "attention",
            "memory",
            "decision-making",
            "social cognition"
        ]
        return {
            "1": {
                "emotion_dim": random.choice(emotion_dimensions),
                "ling_feature": random.choice(linguistic_features),
                "cog_process": random.choice(cognitive_processes)
            },
            "2": {
                "emotion_dim": random.choice(emotion_dimensions),
                "ling_feature": random.choice(linguistic_features),
                "cog_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model for representing and processing emotions in language, inspired by cognitive science and neurolinguistics. Your model should focus on the emotion dimension of {t['emotion_dim']}, the linguistic feature of {t['ling_feature']}, and the cognitive process of {t['cog_process']}. Your task consists of the following steps:

1. Model Architecture (250-300 words):
   a) Describe the overall structure of your emotional language model.
   b) Explain how it incorporates the specified emotion dimension, linguistic feature, and cognitive process.
   c) Discuss how your model integrates insights from cognitive science and neurolinguistics.
   d) Include a simple diagram or flowchart of your model's architecture.

2. Emotion Representation (200-250 words):
   a) Explain how your model represents the emotion dimension of {t['emotion_dim']}.
   b) Describe how this representation interacts with the linguistic feature of {t['ling_feature']}.
   c) Discuss how your representation captures the complexity and nuance of human emotions.

3. Language Processing (200-250 words):
   a) Detail how your model processes language input, focusing on the {t['ling_feature']} feature.
   b) Explain how emotional content is extracted or inferred from the linguistic input.
   c) Describe any novel algorithms or techniques used in this process.

4. Cognitive Integration (150-200 words):
   a) Explain how your model incorporates the cognitive process of {t['cog_process']}.
   b) Discuss how this integration enhances the model's emotional understanding or expression.
   c) Describe any feedback loops or interactions between emotional and cognitive components.

5. Example Analysis (200-250 words):
   Provide a step-by-step analysis of how your model would process the following sentence:
   'Despite the challenges, she felt a surge of determination and hope.'
   Explain how each component of your model contributes to the final emotional interpretation.

6. Evaluation and Limitations (150-200 words):
   a) Propose methods for evaluating the accuracy and effectiveness of your model.
   b) Discuss potential limitations or challenges in implementing your model.
   c) Suggest areas for future research or improvement.

7. Ethical Considerations (100-150 words):
   Discuss potential ethical implications or concerns related to modeling emotions in AI systems, and propose guidelines for responsible development and use of such technologies.

8. Code Snippet (50-100 words of explanation + code):
   Provide a small Python code snippet (10-20 lines) that demonstrates a key aspect of your model, such as emotion representation or linguistic feature processing. Briefly explain what the code does and how it relates to your overall model design.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1300-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model effectively incorporates the emotion dimension of {t['emotion_dim']}, the linguistic feature of {t['ling_feature']}, and the cognitive process of {t['cog_process']}.",
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence.",
            "The model design is creative, innovative, and scientifically plausible.",
            "The example analysis clearly demonstrates how the model would process emotional content in language.",
            "The response addresses ethical considerations and proposes responsible guidelines for development and use.",
            "The provided code snippet is relevant, demonstrates a key aspect of the model, and is accompanied by a clear explanation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
