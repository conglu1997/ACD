import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        languages = ['Mandarin', 'Spanish', 'Arabic', 'Hindi', 'Russian', 'Japanese']
        linguistic_features = ['prosody', 'syntax', 'lexical choice', 'pragmatics']
        
        tasks = {
            "1": {
                "emotion": random.choice(emotions),
                "language": random.choice(languages),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "emotion": random.choice(emotions),
                "language": random.choice(languages),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }
        
        # Ensure the two tasks are different
        while tasks["1"] == tasks["2"]:
            tasks["2"] = {
                "emotion": random.choice(emotions),
                "language": random.choice(languages),
                "linguistic_feature": random.choice(linguistic_features)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for detecting {t['emotion']} in {t['language']}, focusing on the linguistic feature of {t['linguistic_feature']}. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system for emotion detection.
   b) Explain how your system incorporates {t['linguistic_feature']} analysis for {t['language']}.
   c) Discuss any language-specific challenges and how your system addresses them.

2. Linguistic Analysis (200-250 words):
   a) Analyze how {t['emotion']} is typically expressed in {t['language']}, focusing on {t['linguistic_feature']}.
   b) Provide examples of linguistic patterns or cues associated with this emotion in the given language.
   c) Explain how cultural context influences the expression and interpretation of this emotion.

3. AI Model Design (250-300 words):
   a) Propose a specific AI model or algorithm for your emotion detection system.
   b) Explain how your model processes and analyzes {t['linguistic_feature']} in {t['language']}.
   c) Describe the training data and process you would use for this specific emotion and language combination.

4. Evaluation and Challenges (150-200 words):
   a) Suggest metrics and methods to evaluate your system's performance.
   b) Discuss potential biases or limitations in your approach.
   c) Propose solutions to mitigate these challenges.

5. Cross-cultural Application (150-200 words):
   a) Discuss how your system could be adapted for detecting {t['emotion']} in a different language.
   b) Explain any modifications needed to account for cultural and linguistic differences.

Ensure your response demonstrates a deep understanding of linguistics, cultural nuances, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of how {t['emotion']} is expressed in {t['language']}, particularly through {t['linguistic_feature']}.",
            "The AI system design is technically sound and incorporates appropriate linguistic analysis techniques.",
            "The answer shows awareness of cultural nuances and their impact on emotion expression and detection.",
            "The proposed evaluation methods and cross-cultural application discussion are thoughtful and relevant.",
            "The response is well-structured, clear, and uses appropriate technical terminology from linguistics and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
