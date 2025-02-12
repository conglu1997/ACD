import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        regions = [
            {
                "name": "Mesopotamia",
                "period": "Bronze Age",
                "known_sites": ["Ur", "Uruk", "Babylon"],
                "environmental_factors": ["river proximity", "elevation", "soil type"]
            },
            {
                "name": "Yucatan Peninsula",
                "period": "Classic Maya",
                "known_sites": ["Chichen Itza", "Uxmal", "Coba"],
                "environmental_factors": ["cenote proximity", "rainfall", "vegetation density"]
            },
            {
                "name": "Indus Valley",
                "period": "Harappan Civilization",
                "known_sites": ["Mohenjo-daro", "Harappa", "Dholavira"],
                "environmental_factors": ["river systems", "climate fluctuations", "trade routes"]
            },
            {
                "name": "Orkney Islands",
                "period": "Neolithic",
                "known_sites": ["Skara Brae", "Ring of Brodgar", "Maeshowe"],
                "environmental_factors": ["coastal proximity", "wind patterns", "peat bog formation"]
            }
        ]
        return {
            "1": random.choice(regions),
            "2": random.choice(regions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a computational model to predict the locations of undiscovered archaeological sites in the {t['name']} region during the {t['period']}. Your task involves the following steps:

1. Data Integration and Preprocessing (250-300 words):
   a) Describe how you would integrate data from known archaeological sites ({', '.join(t['known_sites'])}) with environmental factors ({', '.join(t['environmental_factors'])}).
   b) Explain your approach to handling missing or uncertain data in the archaeological record.
   c) Discuss any data normalization or transformation techniques you would apply.

2. Predictive Model Design (300-350 words):
   a) Propose a statistical or machine learning model for predicting site locations.
   b) Explain how your model incorporates spatial and temporal factors.
   c) Describe how you would account for potential biases in the archaeological record.
   d) Discuss how your model handles the interaction between different environmental factors.

3. Model Implementation (200-250 words):
   a) Provide pseudocode for the core algorithm of your predictive model. The pseudocode should be detailed enough to convey the main steps and logic of your algorithm, but does not need to be in any specific programming language.
   b) Explain how you would train and validate your model using the available data.
   c) Describe any computational optimizations you would implement for large-scale spatial analysis.

4. Prediction and Analysis (200-250 words):
   a) Describe the output format of your model's predictions.
   b) Explain how you would visualize the predicted site locations and their probability distribution.
   c) Discuss methods for quantifying the uncertainty in your model's predictions.

5. Archaeological Interpretation (150-200 words):
   a) Explain how archaeologists could use your model's predictions in field research.
   b) Discuss potential insights about past human behavior that could be derived from your model.
   c) Address any ethical considerations in using predictive models for archaeological discovery.

6. Model Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the accuracy of your model's predictions.
   b) Describe how you would refine your model based on new archaeological discoveries.
   c) Discuss the limitations of your approach and potential areas for improvement.

Ensure your response demonstrates a deep understanding of archaeological principles, statistical modeling, and geospatial analysis. Use appropriate terminology from archaeology and data science. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all six required sections with appropriate word counts",
            "The data integration section effectively combines archaeological and environmental data, addressing missing data and normalization",
            "The predictive model design is statistically sound, incorporates spatial-temporal factors, and accounts for biases",
            "The implementation section includes clear, detailed pseudocode and explains model training and optimization",
            "The prediction and analysis section describes output format, visualization methods, and uncertainty quantification",
            "The archaeological interpretation demonstrates understanding of field application, behavioral insights, and ethical considerations",
            "The evaluation and refinement section proposes valid methods for model improvement and acknowledges limitations",
            "The overall response shows interdisciplinary knowledge, creative problem-solving, and appropriate use of terminology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
