import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language": "English",
                "time_frame": "50 years",
                "sociocultural_factor": "Technological advancements"
            },
            {
                "language": "Mandarin",
                "time_frame": "100 years",
                "sociocultural_factor": "Globalization"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a system that predicts the evolution of {t['language']} over the next {t['time_frame']}, with a focus on the impact of {t['sociocultural_factor']}. Your response should follow this structure:

1. System Overview (200-250 words):
   a) Describe the key components of your predictive linguistic system.
   b) Explain how your system integrates historical language data with current sociocultural trends.
   c) Outline the main steps in your prediction process.

2. Data and Methodology (200-250 words):
   a) Identify the types of linguistic and sociocultural data your system would use.
   b) Explain your approach to extrapolating linguistic trends over {t['time_frame']}.
   c) Discuss how your model handles uncertainty and multiple possible scenarios.

3. Specific Predictions (200-250 words):
   a) Provide two specific predictions about how {t['language']} might change over the next {t['time_frame']}.
   b) For each prediction, explain the reasoning behind it based on your model.
   c) Discuss potential interactions between these predicted changes.

4. Critical Analysis and Implications (200-250 words):
   a) Evaluate the strengths and limitations of your predictions and model.
   b) Discuss potential ethical concerns or societal impacts of your system.
   c) Suggest how your system might contribute to linguistics or other fields.

Ensure your response demonstrates understanding of linguistics, sociocultural dynamics, and predictive modeling. Balance creativity with scientific plausibility in your approach.

You may include citations to fictional research studies or data to support your ideas. If you do, use the format (Author, Year) for in-text citations.

Format your response with clear headings for each section. Your total response should be between 800-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of {t['language']} linguistics and the potential impact of {t['sociocultural_factor']}",
            "The system overview and methodology are clearly explained and account for complexity",
            "Specific predictions are provided with plausible reasoning based on the described model",
            "The critical analysis shows reflection on the strengths and limitations of the predictions and model",
            "Ethical considerations or societal implications are discussed",
            "The response balances creativity with scientific plausibility",
            "The response adheres to the specified structure and word count requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
