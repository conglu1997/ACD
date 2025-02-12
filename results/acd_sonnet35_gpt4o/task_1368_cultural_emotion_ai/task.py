import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Brazilian",
            "Ethiopian",
            "French",
            "Indian"
        ]
        emotions = [
            "amae (Japanese: dependency)",
            "saudade (Portuguese: melancholic longing)",
            "ubuntu (Zulu: compassionate interconnectedness)",
            "l'appel du vide (French: call of the void)",
            "malu (Indonesian: social embarrassment)"
        ]
        return {
            "1": {
                "culture": random.choice(cultures),
                "emotion": random.choice(emotions)
            },
            "2": {
                "culture": random.choice(cultures),
                "emotion": random.choice(emotions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel AI-based sentiment analysis system that can accurately detect and analyze the emotion of {t['emotion']} in {t['culture']} text. Your system should go beyond traditional sentiment analysis methods by incorporating cultural context and recognizing complex emotional states.

Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI-based sentiment analysis system.
   b) Explain how your system incorporates cultural context in its analysis.
   c) Detail how your system recognizes and processes complex emotional states.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Linguistic and Cultural Integration (200-250 words):
   a) Explain how your system accounts for linguistic nuances specific to the {t['culture']} language or dialect.
   b) Describe how cultural knowledge is embedded in your system to accurately interpret {t['emotion']}.
   c) Discuss any challenges in translating or mapping this emotion across cultures.
   d) Provide at least two concrete examples of phrases or sentences in the {t['culture']} language that express {t['emotion']}, and explain how your system would analyze them.

3. Machine Learning Approach (200-250 words):
   a) Detail the machine learning techniques used in your system (e.g., deep learning, transfer learning).
   b) Explain how you would train your model to recognize {t['emotion']} in {t['culture']} text.
   c) Describe any novel features or algorithms in your approach.
   d) Provide a brief pseudocode or mathematical representation of a key algorithm in your approach.

4. Data Requirements and Preprocessing (150-200 words):
   a) Outline the types and sources of data needed to train your system.
   b) Describe any necessary data preprocessing or augmentation techniques.
   c) Address potential biases in data collection and how you would mitigate them.
   d) Propose a method for generating synthetic training data to improve your system's performance.

5. Evaluation and Performance Metrics (150-200 words):
   a) Propose a method to evaluate your system's performance in detecting {t['emotion']}.
   b) Suggest appropriate metrics for measuring accuracy and cultural sensitivity.
   c) Describe a potential benchmark or test set for your system.
   d) Provide an example confusion matrix or performance table that your system might produce.

6. Ethical Considerations and Limitations (100-150 words):
   a) Discuss ethical implications of analyzing culturally-specific emotions.
   b) Address potential limitations or biases in your approach.
   c) Suggest guidelines for responsible use of your system.
   d) Propose a method for ongoing monitoring and improvement of your system's cultural sensitivity.

Ensure your response demonstrates a deep understanding of natural language processing, cultural linguistics, and machine learning. Be innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide clear explanations for complex concepts.

Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed AI system that clearly incorporates cultural context and complex emotional states in sentiment analysis.",
            "The system architecture is coherent and addresses the specific challenges of analyzing the given emotion in the specified culture.",
            "The machine learning approach is well-explained, appropriate for the task, and includes a pseudocode or mathematical representation of a key algorithm.",
            "The response demonstrates a deep understanding of linguistic nuances and cultural knowledge relevant to the task, including concrete examples of phrases or sentences and their analysis.",
            "The evaluation method and performance metrics are appropriate, well-justified, and include an example confusion matrix or performance table.",
            "Ethical considerations and limitations are thoughtfully addressed, including a method for ongoing monitoring and improvement of cultural sensitivity.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
