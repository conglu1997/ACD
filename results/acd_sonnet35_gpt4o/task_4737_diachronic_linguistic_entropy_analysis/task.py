import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            "English",
            "Mandarin Chinese",
            "Spanish",
            "Arabic",
            "Hindi",
            "Russian",
            "Japanese",
            "Swahili"
        ]
        time_periods = [
            "Ancient (3000 BCE - 500 CE)",
            "Medieval (500 CE - 1500 CE)",
            "Early Modern (1500 CE - 1800 CE)",
            "Modern (1800 CE - present)"
        ]
        linguistic_features = [
            "Phonology",
            "Morphology",
            "Syntax",
            "Semantics",
            "Pragmatics"
        ]
        return {
            "1": {
                "language": random.choice(languages),
                "time_period": random.choice(time_periods),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "language": random.choice(languages),
                "time_period": random.choice(time_periods),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a machine learning system that analyzes the entropy of language evolution over time, focusing on {t['language']} during the {t['time_period']} period, with particular emphasis on changes in {t['linguistic_feature']}. Then use this system to predict future linguistic changes and reconstruct earlier forms of the language. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your machine learning system for analyzing linguistic entropy.
   b) Explain how your system integrates historical linguistic data, information theory principles, and machine learning algorithms.
   c) Detail any novel approaches or techniques used in your design.

2. Entropy Analysis Method (200-250 words):
   a) Explain how your system quantifies and analyzes linguistic entropy over time.
   b) Describe how it accounts for changes specifically in {t['linguistic_feature']}.
   c) Discuss any challenges in applying information theory to historical linguistics and how your system addresses them.

3. Data Requirements and Preprocessing (150-200 words):
   a) Specify the types and sources of data your system would need.
   b) Describe how you would preprocess and normalize historical linguistic data.
   c) Explain how you would handle incomplete or uncertain data from historical sources.

4. Machine Learning Model (200-250 words):
   a) Describe the specific machine learning model(s) used in your system.
   b) Explain how your model is trained on historical linguistic data.
   c) Discuss any techniques used to improve the model's performance on diachronic linguistic tasks.

5. Predictive Capabilities (200-250 words):
   a) Explain how your system predicts future changes in {t['language']}, focusing on {t['linguistic_feature']}.
   b) Provide an example prediction with justification based on historical trends.
   c) Discuss the limitations and uncertainty in these predictions.

6. Language Reconstruction (200-250 words):
   a) Describe how your system approaches the reconstruction of earlier forms of {t['language']}.
   b) Explain how it balances computational predictions with established linguistic theories.
   c) Provide an example of a reconstructed linguistic feature from an earlier time period.

7. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy of your system's analyses and predictions.
   b) Describe how you would validate the reconstructed language forms.
   c) Discuss potential biases in your system and how you would address them.

8. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system might contribute to our understanding of language evolution and historical linguistics.
   b) Explore potential applications of your system in other fields (e.g., anthropology, cognitive science).
   c) Suggest future research directions that could emerge from this work.

Ensure your response demonstrates a deep understanding of historical linguistics, information theory, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of historical linguistics, information theory, and machine learning, with a focus on {t['language']} during the {t['time_period']} period and changes in {t['linguistic_feature']}.",
            "The system architecture and entropy analysis method are well-designed and clearly explained.",
            "The machine learning model and its application to diachronic linguistics are thoroughly described.",
            "The predictive capabilities and language reconstruction approach are innovative and scientifically plausible.",
            "The evaluation methods and interdisciplinary implications are thoughtfully discussed.",
            "The response is well-structured, within the specified word limit, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
