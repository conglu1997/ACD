import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_changes = [
            {
                "change": "Rising sea levels",
                "region": "Coastal cities",
                "timeframe": "Next 50 years"
            },
            {
                "change": "Increased frequency of heatwaves",
                "region": "Urban areas in temperate climates",
                "timeframe": "Next 30 years"
            },
            {
                "change": "Desertification",
                "region": "Sub-Saharan Africa",
                "timeframe": "Next 100 years"
            },
            {
                "change": "Melting permafrost",
                "region": "Arctic regions",
                "timeframe": "Next 75 years"
            }
        ]
        return {
            "1": random.choice(environmental_changes),
            "2": random.choice(environmental_changes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts human cognitive responses to the following environmental change caused by climate change, then use it to propose adaptive strategies:

Environmental Change: {t['change']}
Affected Region: {t['region']}
Timeframe: {t['timeframe']}

Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling cognitive responses.
   b) Explain how your system integrates principles from cognitive science, environmental studies, and AI.
   c) Detail how the system accounts for cultural, social, and individual differences in cognitive responses.
   d) Discuss how the system incorporates uncertainty and variability in climate change projections.

2. Cognitive Response Modeling (250-300 words):
   a) Explain your approach to modeling cognitive responses to the specified environmental change.
   b) Describe the key cognitive processes your model considers (e.g., risk perception, decision-making, emotional responses).
   c) Propose a method for validating the accuracy of your AI's cognitive response predictions.

3. Prediction and Analysis (250-300 words):
   a) Present a sample prediction of cognitive responses to the specified environmental change.
   b) Analyze how these cognitive responses might evolve over the given timeframe.
   c) Discuss potential feedback loops between cognitive responses and environmental changes.

4. Adaptive Strategies (200-250 words):
   a) Based on your AI system's predictions, propose three adaptive strategies to address the cognitive challenges identified.
   b) Explain how each strategy takes into account both the environmental change and the predicted cognitive responses.
   c) Discuss potential barriers to implementing these strategies and how they might be overcome.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss ethical implications of using AI to model and predict human cognitive responses to climate change.
   b) Address potential biases in your system and how they might be mitigated.
   c) Identify limitations of your approach and propose ways to address them.

6. Interdisciplinary Implications (150-200 words):
   a) Explain how your system could contribute to advancements in cognitive science, AI, and climate change adaptation.
   b) Propose potential applications of your system in fields such as public policy, education, or urban planning.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and environmental studies. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, artificial intelligence, and environmental studies",
            "The AI system architecture is well-described and integrates principles from relevant fields",
            "The cognitive response modeling approach is clearly explained and considers key cognitive processes",
            "The sample prediction and analysis are thorough and consider evolving responses over time",
            "The proposed adaptive strategies are creative, relevant, and well-justified",
            "Ethical considerations and limitations are thoughtfully addressed",
            "The interdisciplinary implications and potential applications are insightful and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
