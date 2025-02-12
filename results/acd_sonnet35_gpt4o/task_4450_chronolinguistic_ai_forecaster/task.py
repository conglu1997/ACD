import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "syntax",
            "semantics",
            "phonology",
            "pragmatics"
        ]
        cognitive_processes = [
            "attention",
            "memory",
            "decision-making",
            "problem-solving"
        ]
        tasks = [
            {
                'linguistic_feature': random.choice(linguistic_features),
                'cognitive_process': random.choice(cognitive_processes)
            },
            {
                'linguistic_feature': random.choice(linguistic_features),
                'cognitive_process': random.choice(cognitive_processes)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes language patterns to predict future linguistic and cognitive evolution, then use it to forecast changes in human thought processes over the next century. Focus on the linguistic feature of {t['linguistic_feature']} and the cognitive process of {t['cognitive_process']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for analyzing language patterns and predicting future evolution.
   b) Explain how your system integrates linguistic analysis with cognitive modeling.
   c) Detail how your system incorporates historical data and current trends to make future predictions.

2. Linguistic-Cognitive Interface (200-250 words):
   a) Explain how your system models the relationship between {t['linguistic_feature']} and {t['cognitive_process']}.
   b) Discuss how changes in one domain might influence the other over time.
   c) Propose a novel mechanism for quantifying this relationship.

3. Predictive Algorithms (200-250 words):
   a) Describe the core algorithms used in your system for forecasting linguistic and cognitive changes.
   b) Explain how these algorithms account for societal, technological, and environmental factors.
   c) Discuss any machine learning or artificial intelligence techniques employed in your predictive model.

4. Data Requirements and Analysis (150-200 words):
   a) Specify the types and sources of data your system would require for accurate predictions.
   b) Describe how you would validate your model's predictions against real-world observations.
   c) Discuss potential biases in your data or model and how you would address them.

5. Century-Long Forecast (250-300 words):
   a) Present a detailed forecast of how {t['linguistic_feature']} and {t['cognitive_process']} might evolve over the next 100 years.
   b) Describe potential milestones or significant shifts in these areas at 25, 50, and 100-year intervals.
   c) Explain how these changes might impact broader aspects of human cognition and society.

6. Ethical Implications and Limitations (150-200 words):
   a) Discuss the ethical considerations of predicting and potentially influencing linguistic and cognitive evolution.
   b) Analyze potential misuses of your system and propose safeguards against them.
   c) Identify limitations of your approach and suggest areas for future research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The proposed AI system integrates linguistic analysis with cognitive modeling in a novel and plausible way.",
            "The predictive algorithms and data analysis methods are well-explained and scientifically sound.",
            "The century-long forecast is detailed, creative, and grounded in current scientific understanding.",
            "Ethical implications and limitations are thoughtfully addressed.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
