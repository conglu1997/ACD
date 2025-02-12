import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "phonological changes",
            "morphological simplification",
            "syntactic restructuring",
            "lexical borrowing"
        ]
        cognitive_factors = [
            "memory constraints",
            "attention mechanisms",
            "social cognition",
            "embodied cognition"
        ]
        language_families = [
            "Indo-European",
            "Sino-Tibetan",
            "Austronesian",
            "Afroasiatic"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_factor": random.choice(cognitive_factors),
                "language_family": random.choice(language_families)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_factor": random.choice(cognitive_factors),
                "language_family": random.choice(language_families)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that predicts semantic drift in language evolution, focusing on the {t['linguistic_feature']} in the context of {t['language_family']} languages, and incorporating the cognitive factor of {t['cognitive_factor']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for predicting semantic drift.
   b) Explain how it incorporates the specified linguistic feature and cognitive factor.
   c) Detail how the system models language evolution in the given language family.
   d) Include a high-level diagram or pseudocode illustrating the system's architecture.

2. Data and Training (200-250 words):
   a) Describe the types of data your system would require for training.
   b) Explain your approach to data collection and preprocessing.
   c) Discuss any challenges in obtaining or using historical linguistic data.
   d) Propose a novel method for augmenting limited historical data.

3. Semantic Drift Modeling (250-300 words):
   a) Explain how your system models and predicts semantic drift.
   b) Describe the role of the specified cognitive factor in your model.
   c) Provide an example of how your system would predict drift for a specific word or phrase.
   d) Discuss how your model accounts for cultural and historical factors in semantic drift.

4. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy of your semantic drift predictions.
   b) Describe how you would validate your model against historical linguistic data.
   c) Suggest a novel approach to measure the impact of the cognitive factor on prediction accuracy.
   d) Discuss the challenges in evaluating long-term language evolution predictions.

5. Applications and Implications (200-250 words):
   a) Propose three potential applications of your semantic drift prediction system.
   b) Discuss the implications of accurate semantic drift prediction for linguistics and cognitive science.
   c) Explore how your system could contribute to our understanding of language evolution.
   d) Address any ethical considerations in developing and using such a system.

6. Future Directions and Challenges (150-200 words):
   a) Identify two major challenges in improving semantic drift prediction.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss how advancements in AI and cognitive science might impact future iterations of your system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and machine learning, using appropriate terminology from all fields.",
            f"The AI system effectively incorporates the specified linguistic feature ({t['linguistic_feature']}) and cognitive factor ({t['cognitive_factor']}) in the context of {t['language_family']} languages.",
            "The system design is innovative, scientifically plausible, and thoroughly explained.",
            "The response addresses all required sections with appropriate depth and insight.",
            "The proposed applications and future directions show creativity and a strong grasp of the field's potential."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
