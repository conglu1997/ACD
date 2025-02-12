import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Mandarin', 'Arabic', 'Spanish']
        time_periods = [1000, 5000, 10000]
        
        tasks = {
            "1": {
                "language": random.choice(languages),
                "years_in_future": random.choice(time_periods)
            },
            "2": {
                "language": random.choice(languages),
                "years_in_future": random.choice(time_periods)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to predict long-term language evolution and apply it to forecast changes in {t['language']} {t['years_in_future']} years in the future. Your task has the following parts:

1. AI System Design (250-300 words):
   a) Describe the architecture of your AI system for predicting long-term language evolution.
   b) Explain what data sources and linguistic features your system would use.
   c) Discuss how your system accounts for factors like technological changes, cultural shifts, and potential extraterrestrial influences.

2. Linguistic Evolution Factors (200-250 words):
   a) Identify and explain at least five key factors that could influence the evolution of {t['language']} over {t['years_in_future']} years.
   b) Discuss how your AI system would model and weigh these factors in its predictions.

3. Language Forecast (250-300 words):
   Based on your AI system's prediction, describe how {t['language']} might change over {t['years_in_future']} years. Include:
   a) Changes in phonology (sound system)
   b) Changes in morphology and syntax
   c) Changes in semantics and vocabulary
   d) Potential influences from other languages or new technologies

4. Sample Text and Quantitative Analysis (150-200 words):
   a) Provide a short sample text (30-50 words) in the evolved version of {t['language']}, along with a 'translation' into present-day {t['language']}.
   b) Explain the key differences and the reasoning behind them.
   c) Provide a quantitative measure of the degree of change (e.g., percentage of words changed, syntactic similarity score) and briefly explain your methodology.

5. Challenges and Limitations (150-200 words):
   a) Discuss the main challenges in predicting language evolution over such a long time period.
   b) Explain any limitations of your AI system and how they might affect the accuracy of its predictions.

6. Implications and Applications (150-200 words):
   a) Discuss potential applications of your AI system beyond linguistic forecasting.
   b) Explore the implications of long-term language evolution prediction for fields like archaeology, anthropology, or interstellar communication.

Ensure your response demonstrates a deep understanding of linguistics, AI, and factors influencing long-term societal and technological changes. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, and adhere to the word limits provided for each part. Your total response should not exceed 1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed design of an AI system for predicting long-term language evolution",
            f"The answer identifies and explains at least five key factors influencing the evolution of {t['language']} over {t['years_in_future']} years",
            f"A plausible forecast of how {t['language']} might change over {t['years_in_future']} years is provided, covering phonology, morphology, syntax, semantics, and vocabulary",
            "The response includes a sample text in the evolved language with a translation and explanation",
            "A quantitative measure of the degree of language change is provided with a brief explanation of the methodology",
            "Challenges and limitations of long-term language evolution prediction are discussed",
            "Potential implications and applications of the AI system are explored",
            "The answer demonstrates interdisciplinary knowledge of linguistics, AI, and long-term societal/technological changes",
            "The response is creative while maintaining scientific plausibility",
            "The answer is well-structured with clear headings for each section and adheres to the provided word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
