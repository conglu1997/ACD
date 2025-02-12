import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'climate_scenario': 'Rising sea levels in coastal cities',
                'target_behavior': 'Adoption of water conservation practices'
            },
            {
                'climate_scenario': 'Increased frequency of heat waves in urban areas',
                'target_behavior': 'Reduction of personal carbon footprint'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts human behavior in response to climate change, then use it to propose interventions for promoting sustainable practices. Focus on the climate scenario of {t['climate_scenario']} and the target behavior of {t['target_behavior']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for modeling human behavior in response to climate change.
   b) Explain how your system integrates knowledge from environmental science, psychology, and data science.
   c) Detail how the AI processes climate data and human behavior data to make predictions.
   d) Include a text-based diagram or flowchart illustrating the system's architecture (use ASCII characters or simple text formatting).

2. Data Sources and Processing (200-250 words):
   a) Identify the types of data your system would use (e.g., climate projections, demographic data, behavioral surveys).
   b) Explain how you would collect, preprocess, and integrate these diverse data sources.
   c) Discuss any challenges in data collection or integration and how you would address them.

3. Behavioral Modeling (250-300 words):
   a) Describe the psychological theories or models of behavior change that inform your AI system.
   b) Explain how your system models the relationship between climate change perceptions and behavior.
   c) Detail how your AI accounts for individual differences, social influences, and contextual factors in behavior prediction.

4. Prediction and Intervention Generation (200-250 words):
   a) Explain how your system generates predictions about human behavior in response to {t['climate_scenario']}.
   b) Describe the process by which your AI proposes interventions to promote {t['target_behavior']}.
   c) Provide an example of a specific intervention your system might suggest, along with its predicted effectiveness.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues related to using AI to influence human behavior in the context of climate change.
   b) Address concerns about privacy, autonomy, and potential misuse of the system.
   c) Propose guidelines for the responsible development and use of your AI system.

6. Evaluation and Refinement (150-200 words):
   a) Propose methods for evaluating the accuracy of your system's predictions and the effectiveness of its interventions.
   b) Describe how your system could learn and improve from feedback and real-world outcomes.
   c) Suggest potential applications of your AI system beyond climate change mitigation.

Ensure your response demonstrates a deep understanding of artificial intelligence, environmental science, and social psychology. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI, environmental science, and social psychology.",
            "The proposed system architecture is comprehensive and integrates knowledge from multiple disciplines.",
            "The behavioral modeling approach is well-grounded in psychological theories and accounts for complex factors.",
            "The prediction and intervention generation process is clearly explained and includes a plausible example.",
            "Ethical considerations are thoroughly addressed, including privacy concerns and responsible use guidelines.",
            "The evaluation and refinement section proposes valid methods for assessing and improving the system.",
            "The overall response is creative, scientifically plausible, and ethically responsible.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
