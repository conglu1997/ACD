import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "era": "Ancient Rome",
                "event": "Fall of the Western Roman Empire",
                "future_period": "Next 100 years"
            },
            {
                "era": "Industrial Revolution",
                "event": "Invention of the steam engine",
                "future_period": "Next 200 years"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes historical patterns and predicts potential future events, then apply it to the following historical scenario: {t['event']} in {t['era']}. Your task is to predict significant events and developments for the {t['future_period']} following this event. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for historical analysis and prediction.
   b) Explain how your system integrates data from various historical sources and disciplines.
   c) Detail how the system identifies patterns and trends across different historical periods.
   d) Discuss any novel elements in your design that enable long-term predictive modeling.

2. Data Processing and Analysis (200-250 words):
   a) Describe the types of historical data your system would use as input.
   b) Explain how your system would preprocess and integrate diverse historical sources.
   c) Discuss any challenges in data representation and how your architecture addresses them.
   d) Outline the key analytical techniques your system employs (e.g., time series analysis, causal inference).

3. Pattern Recognition and Extrapolation (200-250 words):
   a) Explain how your system identifies relevant patterns in historical data.
   b) Describe the methods used to extrapolate these patterns into future predictions.
   c) Discuss how your system accounts for the unique aspects of the given historical scenario.
   d) Explain how your system handles the uncertainty inherent in long-term predictions.

4. Scenario Application (250-300 words):
   a) Apply your AI system to analyze the {t['event']} in {t['era']}.
   b) Provide at least three specific predictions for significant events or developments in the {t['future_period']} following this event.
   c) Explain the reasoning behind each prediction, citing historical patterns or trends identified by your system.
   d) Discuss any potential alternative scenarios your system might consider.

5. Evaluation and Validation (150-200 words):
   a) Propose a method to evaluate the accuracy and reliability of your system's predictions.
   b) Discuss how you would validate your system using known historical data.
   c) Explain how your system could be updated or refined based on new historical insights.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI for historical analysis and future prediction.
   b) Address concerns about potential misuse or misinterpretation of your system's predictions.
   c) Explain limitations of your approach and areas where human expertise remains crucial.

Ensure your response demonstrates a deep understanding of historical analysis, AI systems, and predictive modeling. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining historical and technological plausibility.

Format your response using clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical analysis, AI systems, and predictive modeling",
            "The AI system design is creative, plausible, and integrates various historical data sources",
            "The scenario application provides at least three specific, well-reasoned predictions based on historical patterns",
            "The response addresses ethical considerations and limitations of AI in historical analysis",
            "The total response is between 1200-1500 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
