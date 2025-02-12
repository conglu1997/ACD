class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "time_period": "Medieval to Renaissance Europe",
                "linguistic_feature": "Lexical borrowing",
                "cultural_domain": "Art and architecture",
                "comparative_period": "Industrial Revolution Europe"
            },
            "2": {
                "time_period": "Ancient to Modern China",
                "linguistic_feature": "Grammaticalization",
                "cultural_domain": "Political systems",
                "comparative_period": "Meiji Restoration Japan"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a computational model that simulates the co-evolution of language and culture over historical time periods, then use it to analyze and predict linguistic and cultural changes. Focus on the time period of {t['time_period']}, the linguistic feature of {t['linguistic_feature']}, and the cultural domain of {t['cultural_domain']}. Your response should include the following sections:

1. Model Architecture (300-350 words):
   a) Describe the key components of your computational model and how they interact.
   b) Explain how your model incorporates principles from linguistics, cultural evolution, and historical analysis.
   c) Detail how your model simulates the co-evolution of language and culture over time.
   d) Discuss how your model specifically handles the given linguistic feature and cultural domain.
   e) Include a high-level diagram or pseudocode to illustrate your model's architecture.
   f) Provide a concrete example or case study to illustrate your model's functionality.

2. Data and Parameters (200-250 words):
   a) Describe the types of data your model requires and potential sources for this data.
   b) Explain how you would preprocess and integrate data from different historical sources.
   c) Discuss the key parameters in your model and how they influence the simulation.
   d) Address how your model handles uncertainties or gaps in historical data.

3. Simulation Process (250-300 words):
   a) Provide a step-by-step explanation of how your model simulates changes over the specified time period.
   b) Describe how your model captures the interaction between linguistic and cultural changes.
   c) Explain how your model accounts for external historical events or influences.
   d) Discuss any novel approaches or algorithms used in your simulation process.
   e) Illustrate with a specific example from the given time period and cultural domain.

4. Analysis and Predictions (250-300 words):
   a) Describe how you would use your model to analyze historical linguistic and cultural changes.
   b) Explain your approach to generating predictions about future language and cultural evolution.
   c) Discuss how you would validate your model's results against known historical data.
   d) Propose a specific hypothesis about language-culture co-evolution that your model could test.
   e) Provide a quantitative analysis of a specific linguistic or cultural change predicted by your model, including error estimates.
   f) Compare and contrast the simulated linguistic and cultural evolution between {t['time_period']} and {t['comparative_period']}, highlighting key differences and similarities.

5. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or biases in your model and how they might be addressed.
   b) Discuss ethical implications of using computational models to study and predict cultural evolution.
   c) Address concerns about the application of such models in policy-making or education.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your model contributes to the fields of computational linguistics, cultural evolution, and historical analysis.
   b) Explore potential applications of your model in other domains (e.g., anthropology, sociology, or future studies).
   c) Propose two novel research questions that could be explored using your model.

Ensure your response demonstrates a deep understanding of computational modeling, linguistics, cultural evolution, and historical analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of computational modeling, linguistics, cultural evolution, and historical analysis.",
            "The proposed model architecture is well-explained, innovative, and scientifically plausible.",
            "The simulation process and data handling approaches are clearly described and appropriate for the task.",
            "The analysis and prediction methods are well-reasoned and demonstrate an understanding of the complexities involved.",
            "The quantitative analysis of a specific linguistic or cultural change is provided with error estimates.",
            "A comparative analysis between the two specified time periods is included, highlighting key differences and similarities.",
            "Ethical considerations and limitations are thoroughly explored.",
            "The interdisciplinary implications and potential applications are insightful and demonstrate broad thinking.",
            "The response is well-structured, adhering to the specified sections and word limits.",
            "The proposed model demonstrates innovative approaches or novel combinations of existing techniques.",
            "Concrete examples or case studies are provided to illustrate the model's functionality."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
