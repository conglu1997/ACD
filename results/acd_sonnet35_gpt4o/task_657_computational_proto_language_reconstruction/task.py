import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language_family": "Indo-European",
                "target_proto_language": "Proto-Indo-European",
                "key_feature": "Phonological reconstruction",
                "historical_period": "6000-4000 BCE"
            },
            {
                "language_family": "Austronesian",
                "target_proto_language": "Proto-Austronesian",
                "key_feature": "Lexical reconstruction",
                "historical_period": "4000-2000 BCE"
            },
            {
                "language_family": "Sino-Tibetan",
                "target_proto_language": "Proto-Sino-Tibetan",
                "key_feature": "Morphological reconstruction",
                "historical_period": "5000-3000 BCE"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational system to reconstruct the {t['target_proto_language']} using machine learning techniques and historical linguistic principles. Your system should focus on the {t['language_family']} language family and the historical period of {t['historical_period']}, with particular emphasis on {t['key_feature']}.

Your response should include the following sections:

1. System Architecture (200-250 words):
   a) Describe the key components of your computational system for proto-language reconstruction.
   b) Explain how your system integrates machine learning techniques with historical linguistic principles.
   c) Discuss how your architecture addresses the challenges specific to {t['key_feature']}.

2. Data Processing and Analysis (150-200 words):
   a) Describe the types of linguistic data your system would use for reconstruction.
   b) Explain how your system would preprocess and analyze this data.
   c) Discuss any novel approaches to handling sparse or uncertain historical language data.

3. Machine Learning Model (200-250 words):
   a) Propose a specific machine learning model or algorithm for proto-language reconstruction.
   b) Explain how this model incorporates linguistic rules and historical sound changes.
   c) Describe how your model would handle uncertainties and ambiguities in the reconstruction process.

4. Historical Linguistic Integration (150-200 words):
   a) Explain how your system incorporates established methods of historical linguistics.
   b) Describe how your system would validate its reconstructions against existing linguistic theories.
   c) Discuss any potential conflicts between computational and traditional approaches, and how you would resolve them.

5. Reconstruction Output and Visualization (100-150 words):
   a) Describe the format of your system's reconstructed proto-language output.
   b) Propose an innovative method to visualize the reconstruction process and results.
   c) Explain how your visualization would aid linguists in understanding and validating the reconstruction.

6. Evaluation and Validation (100-150 words):
   a) Propose methods for evaluating the accuracy and plausibility of your system's reconstructions.
   b) Describe how you would validate your system using known language histories or simulated data.
   c) Discuss the limitations of your evaluation approach and potential improvements.

7. Ethical Considerations and Implications (100-150 words):
   a) Discuss potential ethical implications of using AI for historical language reconstruction.
   b) Address concerns about the impact of such systems on traditional linguistic scholarship.
   c) Propose guidelines for the responsible use and interpretation of AI-generated proto-language reconstructions.

Ensure your response demonstrates a deep understanding of computational linguistics, historical linguistics, and machine learning. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1000-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content",
            "The system design demonstrates integration of computational linguistics, historical linguistics, and machine learning",
            f"The system focuses on reconstructing {t['target_proto_language']} with emphasis on {t['key_feature']}",
            f"The historical period of {t['historical_period']} is considered in the reconstruction process",
            "The response is creative while maintaining scientific and technological plausibility",
            "The ethical considerations and limitations are thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
