class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "language_family": "Indo-European",
                "focus_languages": ["Sanskrit", "Ancient Greek", "Latin"],
                "time_frame": "5000 BCE to 3000 CE"
            },
            "2": {
                "language_family": "Sino-Tibetan",
                "focus_languages": ["Old Chinese", "Classical Tibetan", "Burmese"],
                "time_frame": "4000 BCE to 3000 CE"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a computational system for reconstructing the proto-language of the {t['language_family']} family and predicting its future evolution. Focus on the following languages: {', '.join(t['focus_languages'])}. Your system should cover the time frame from {t['time_frame']}. Your task has the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your computational system for proto-language reconstruction and future language evolution prediction.
   b) Explain how your system integrates historical linguistic data, computational models, and AI-driven predictive algorithms.
   c) Provide a diagram or flowchart of your system architecture.

2. Proto-language Reconstruction (200-250 words):
   a) Explain the methods your system uses to reconstruct the proto-language.
   b) Describe how it handles phonological, morphological, and semantic changes.
   c) Provide an example of a reconstructed word or phrase in the proto-language, showing your system's reasoning process.

3. Evolution Prediction Model (200-250 words):
   a) Detail the AI-driven model used for predicting future language evolution.
   b) Explain how it accounts for factors such as language contact, social changes, and technological advancements.
   c) Describe any novel approaches or algorithms used in your predictive model.

4. Validation and Accuracy (150-200 words):
   a) Propose methods to validate your system's reconstruction and predictions.
   b) Discuss potential sources of error and how your system addresses them.
   c) Explain how your system handles uncertainties in historical data and future predictions.

5. Linguistic Insights (200-250 words):
   a) Describe two novel linguistic insights that your system could potentially uncover about the {t['language_family']} family.
   b) Explain how these insights might contribute to our understanding of language evolution and human history.

6. Ethical Considerations and Implications (150-200 words):
   a) Discuss potential ethical concerns or societal impacts of using such a system.
   b) Address issues such as cultural sensitivity and the potential misuse of predictive linguistic models.
   c) Propose guidelines for the responsible development and use of proto-language reconstruction and evolution prediction systems.

7. Future Research Directions (100-150 words):
   a) Suggest two potential research projects that could further enhance or validate your system.
   b) Briefly describe the methodology and expected outcomes of these projects.

8. Sample Output (100-150 words):
   Provide a sample output from your system, including:
   a) A reconstructed sentence in the proto-language with its estimated time period.
   b) The same sentence's predicted form in 3000 CE.
   c) A brief explanation of the major changes observed.

Ensure your response demonstrates a deep understanding of historical linguistics, computational linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your system design while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1750 words, not including the diagram. Include the diagram as a text-based representation (e.g., ASCII art or a structured text description) within your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a comprehensive and scientifically plausible system design for proto-language reconstruction and evolution prediction.",
            "The system architecture integrates historical linguistic data, computational models, and AI-driven predictive algorithms effectively.",
            "The proto-language reconstruction method and evolution prediction model are well-explained and demonstrate a deep understanding of linguistic principles.",
            "The response includes creative and novel approaches while maintaining scientific rigor.",
            "Ethical considerations and future research directions are thoughtfully addressed.",
            "The response adheres to the specified word count ranges for each section and demonstrates a sophisticated understanding of historical linguistics, computational linguistics, and AI concepts.",
            "The sample output provided is consistent with the described system and demonstrates its capability in reconstructing proto-languages and predicting language evolution."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
