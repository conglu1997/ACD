import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_families = [
            "Indo-European",
            "Sino-Tibetan",
            "Afroasiatic",
            "Austronesian"
        ]
        time_periods = [
            "Ancient (3000 BCE - 500 CE)",
            "Medieval (500 CE - 1500 CE)",
            "Early Modern (1500 CE - 1800 CE)"
        ]
        linguistic_features = [
            "Phonological changes",
            "Morphological evolution",
            "Syntactic shifts",
            "Semantic drift"
        ]
        return {
            "1": {
                "language_family": random.choice(language_families),
                "time_period": random.choice(time_periods),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "language_family": random.choice(language_families),
                "time_period": random.choice(time_periods),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to reconstruct historical languages and model their evolution over time, focusing on the {t['language_family']} language family during the {t['time_period']} period, with particular emphasis on {t['linguistic_feature']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for historical language reconstruction and evolution modeling.
   b) Explain how your system integrates linguistic theory, machine learning, and historical data analysis.
   c) Detail how the system handles uncertainty and incomplete data, which are common in historical linguistics.
   d) Discuss any novel AI approaches or algorithms used in your system.
   e) Provide a simple diagram or pseudocode snippet (5-10 lines) illustrating a key aspect of your system's implementation.

2. Data Sources and Processing (250-300 words):
   a) Identify the types of linguistic and historical data your system would use.
   b) Explain how your system would integrate and analyze these diverse data types.
   c) Describe any specific techniques for extracting linguistic information from historical texts or artifacts.
   d) Discuss how your system would handle variations in writing systems or orthography over time.

3. Linguistic Analysis and Reconstruction (250-300 words):
   a) Describe how your system would model {t['linguistic_feature']} in the {t['language_family']} family.
   b) Explain the methods used to infer historical language states from limited data.
   c) Discuss how your system would account for language contact and borrowing.
   d) Provide an example of how your system might reconstruct a specific linguistic feature.
   e) Cite at least one relevant linguistic theory or study that informs your approach.

4. Evolution Modeling (200-250 words):
   a) Explain how your AI system models language evolution over time.
   b) Describe any statistical or probabilistic methods used in your evolutionary model.
   c) Discuss how your system accounts for social and historical factors in language change.

5. Visualization and Interpretation (150-200 words):
   a) Propose an innovative method for visualizing language evolution and reconstruction.
   b) Explain how your system would generate insights about historical languages and their development.
   c) Describe how the system would present uncertainty or alternative reconstructions.

6. Validation and Limitations (200-250 words):
   a) Propose methods for validating the accuracy of your system's reconstructions and evolutionary models.
   b) Discuss the limitations of your approach and potential biases in the reconstructed languages.
   c) Suggest ways to improve the system's performance or address its limitations.

7. Interdisciplinary Applications (150-200 words):
   a) Discuss how your system could contribute to research in historical linguistics, anthropology, or other related fields.
   b) Explore potential applications of your system in other domains (e.g., literary analysis, cultural studies).

Ensure your response demonstrates a deep understanding of linguistics, machine learning, and historical analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words.

Example (without giving away the solution):
For instance, if modeling phonological changes in the Indo-European family, your system might analyze patterns of sound shifts across related languages to reconstruct earlier forms. It could use techniques like comparative reconstruction and internal reconstruction, while accounting for regular sound changes and analogical changes."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system architecture that effectively integrates linguistics, machine learning, and historical data analysis for the {t['language_family']} language family.",
            f"The system demonstrates a strong approach to modeling {t['linguistic_feature']} during the {t['time_period']} period.",
            "The response shows a nuanced understanding of the challenges in historical language reconstruction and evolution modeling.",
            "The proposed system includes innovative features for visualization, interpretation, and validation of results.",
            "The response addresses ethical considerations and potential limitations of the AI system in historical linguistics.",
            "The response cites at least one relevant linguistic theory or study.",
            "The response adheres to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
