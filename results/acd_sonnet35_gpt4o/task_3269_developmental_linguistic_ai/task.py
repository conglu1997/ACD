import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin", "English"),
            ("Arabic", "Spanish"),
            ("Hindi", "Russian"),
            ("Swahili", "Japanese")
        ]
        linguistic_features = [
            "phonological awareness",
            "syntax acquisition",
            "semantic development",
            "pragmatic competence"
        ]
        developmental_stages = [
            "early childhood (2-4 years)",
            "middle childhood (5-7 years)",
            "late childhood (8-10 years)",
            "early adolescence (11-13 years)"
        ]
        tasks = {
            "1": {
                "language_pair": random.choice(language_pairs),
                "linguistic_feature": random.choice(linguistic_features),
                "developmental_stage": random.choice(developmental_stages)
            },
            "2": {
                "language_pair": random.choice(language_pairs),
                "linguistic_feature": random.choice(linguistic_features),
                "developmental_stage": random.choice(developmental_stages)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human language acquisition and development, focusing on {t['linguistic_feature']} in {t['language_pair'][0]} and {t['language_pair'][1]} during the {t['developmental_stage']} stage. Then, use your system to analyze and predict linguistic milestones for this feature across these two languages and cultures. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating language acquisition and development.
   b) Explain how your system integrates theories from linguistics, cognitive science, and developmental psychology.
   c) Discuss how your system handles the challenges of cross-linguistic and cross-cultural language development.
   d) Include a simple diagram or flowchart of your system architecture (describe this textually).

2. Language Acquisition Simulation (200-250 words):
   a) Explain how your system simulates the acquisition of {t['linguistic_feature']} in both {t['language_pair'][0]} and {t['language_pair'][1]}.
   b) Describe the key differences in the acquisition process between the two languages.
   c) Discuss how your system accounts for cultural factors influencing language development.

3. Linguistic Milestone Prediction (200-250 words):
   a) Using your system, predict at least three linguistic milestones related to {t['linguistic_feature']} for each language during the {t['developmental_stage']} stage.
   b) Explain the reasoning behind these predictions, citing relevant linguistic and cognitive theories.
   c) Discuss any potential differences in milestone achievement between the two languages and cultures.

4. Cross-linguistic Analysis (150-200 words):
   a) Compare and contrast the development of {t['linguistic_feature']} between {t['language_pair'][0]} and {t['language_pair'][1]}.
   b) Identify any unique challenges or advantages in acquiring this feature in each language.
   c) Discuss how these differences might impact overall language proficiency and cognitive development.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy of your system's simulations and predictions.
   b) Suggest an experiment to validate your system's performance in analyzing {t['linguistic_feature']} across {t['language_pair'][0]} and {t['language_pair'][1]}.
   c) Discuss potential biases in your system and how you would address them.

6. Ethical Considerations (100-150 words):
   a) Discuss the ethical implications of using AI to simulate and predict child language development.
   b) Address privacy concerns related to collecting and using developmental language data.
   c) Propose guidelines for the responsible development and use of AI systems in studying child language acquisition.

7. Potential Applications (100-150 words):
   a) Suggest two potential applications of your AI system in fields such as education, speech therapy, or cognitive science.
   b) Briefly explain how each application could benefit from cross-linguistic developmental analysis.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, developmental psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['linguistic_feature']} in the context of language acquisition and development",
            f"The AI system design effectively integrates theories from linguistics, cognitive science, and developmental psychology to simulate language acquisition in {t['language_pair'][0]} and {t['language_pair'][1]}",
            f"The linguistic milestone predictions for the {t['developmental_stage']} stage are plausible and well-reasoned for both languages",
            "The cross-linguistic analysis provides insightful comparisons between the two languages",
            "The proposed evaluation methods and experiments are appropriate and well-designed",
            "The response addresses ethical considerations and proposes relevant guidelines",
            "The suggested applications demonstrate practical relevance of the AI system",
            "The writing is clear, well-structured, and uses appropriate technical terminology",
            "The response follows the required format and stays within the specified word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
