import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "language": "English",
                "time_frame": "50 years",
                "focus_area": "vocabulary",
                "trend": "increased digital communication"
            },
            "2": {
                "language": "Mandarin Chinese",
                "time_frame": "100 years",
                "focus_area": "syntax",
                "trend": "globalization and cultural exchange"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that predicts future changes in {t['language']} over the next {t['time_frame']}, focusing on {t['focus_area']} and considering the trend of {t['trend']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for predicting linguistic evolution.
   b) Explain how your system integrates historical linguistic data with current socio-technological trends.
   c) Detail the algorithms or models used for predictive analysis.
   d) Discuss how your system accounts for factors like social dynamics and cross-cultural interactions.

2. Data Sources and Processing (200-250 words):
   a) Identify the types of data your system would use (e.g., historical texts, social media, academic corpora).
   b) Explain how your system processes and analyzes this data.
   c) Discuss any challenges in data collection or integration and how you address them.

3. Predictive Model (250-300 words):
   a) Describe how your system models linguistic change over time.
   b) Explain how it incorporates the specified trend ({t['trend']}) into its predictions.
   c) Discuss how your model handles uncertainty and variability in language evolution.

4. Specific Predictions (200-250 words):
   a) Provide at least three specific predictions for changes in {t['language']} {t['focus_area']} over the next {t['time_frame']}.
   b) Explain the reasoning behind each prediction, citing relevant linguistic principles and social factors.
   c) Discuss potential implications of these changes for speakers and learners of the language.

5. Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the accuracy of your system's predictions.
   b) Discuss limitations of your approach and potential areas for improvement.
   c) Consider ethical implications of predicting language change, such as potential impacts on linguistic diversity or language policy.

Ensure your response demonstrates a deep understanding of linguistics, artificial intelligence, and social dynamics. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and forward-thinking in your predictions while maintaining scientific plausibility. Balance innovative ideas with established linguistic principles.

Format your response with clear headings for each section and use proper paragraph structure within each section. Your total response should be between 1050-1300 words. Cite relevant academic sources where appropriate to support your design and predictions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, AI, and social dynamics.",
            "The system architecture is well-designed, clearly explained, and integrates historical data with current trends.",
            "The data sources and processing methods are appropriate and thoroughly discussed.",
            "The predictive model is clearly explained and incorporates the specified trend in a logical manner.",
            f"At least three specific, plausible predictions for changes in {t['language']} {t['focus_area']} are provided, with well-reasoned explanations.",
            "The evaluation methods and limitations are thoughtfully discussed, including ethical considerations.",
            "The response is creative and forward-thinking while maintaining scientific plausibility.",
            "Appropriate terminology is used throughout, with clear explanations for complex concepts.",
            "The response is well-structured, adhering to the specified format and word count.",
            "Relevant academic sources are cited to support the design and predictions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
