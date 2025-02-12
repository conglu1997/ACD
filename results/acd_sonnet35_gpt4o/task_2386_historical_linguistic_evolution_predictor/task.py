import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Mandarin', 'Spanish', 'Arabic', 'Hindi']
        time_periods = ['50 years', '100 years', '200 years', '500 years']
        societal_aspects = ['Technology', 'Politics', 'Education', 'Entertainment', 'Social Interactions']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'language': random.choice(languages),
                'time_period': random.choice(time_periods),
                'societal_aspect': random.choice(societal_aspects)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system to analyze historical linguistic data and predict the evolution of {t['language']} over the next {t['time_period']}, focusing on its impact on {t['societal_aspect']}. Your response should include:

1. Data Analysis Framework (250-300 words):
   a) Describe the types of historical linguistic data your system would analyze.
   b) Explain how your system would process and interpret this data.
   c) Discuss any challenges in obtaining or analyzing historical language data for {t['language']}.

2. Predictive Model Design (300-350 words):
   a) Outline the key components of your predictive model for language evolution.
   b) Explain how your model accounts for factors like technological advancements, cultural shifts, and global interactions.
   c) Describe any machine learning or statistical techniques your model would employ.
   d) Discuss how your model would handle the uncertainty inherent in long-term predictions.

3. Language Evolution Prediction (250-300 words):
   a) Provide a detailed prediction of how {t['language']} might evolve over the next {t['time_period']}.
   b) Include specific examples of potential changes in vocabulary, grammar, or pronunciation.
   c) Explain the reasoning behind your predictions, citing historical patterns or current trends.

4. Societal Impact Analysis (250-300 words):
   a) Analyze how the predicted language changes might impact {t['societal_aspect']}.
   b) Provide concrete examples of how these linguistic shifts could alter social dynamics, cultural practices, or institutional structures.
   c) Discuss any potential challenges or opportunities arising from these changes.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss ethical implications of predicting language evolution and its societal impacts.
   b) Address potential biases in your model and how they might be mitigated.
   c) Explain limitations of your approach and areas where predictions might be less reliable.

6. Validation and Refinement Strategy (150-200 words):
   a) Propose methods to validate your model's predictions over time.
   b) Suggest how the system could be refined and improved as new data becomes available.
   c) Discuss how to handle potential divergences between predictions and actual language evolution.

Ensure your response demonstrates a deep understanding of linguistic principles, historical analysis, and predictive modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your predictions while maintaining plausibility based on historical trends and current knowledge.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of linguistic principles and historical language evolution.",
            "The proposed system for data analysis and predictive modeling is well-designed and scientifically plausible.",
            "The language evolution predictions are creative yet grounded in historical patterns and current trends.",
            "The societal impact analysis is insightful and considers multiple aspects of the specified area.",
            "Ethical considerations and limitations are thoroughly addressed.",
            "The validation and refinement strategy is well-thought-out and practical.",
            "The overall response is well-structured, coherent, and demonstrates high-level interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
