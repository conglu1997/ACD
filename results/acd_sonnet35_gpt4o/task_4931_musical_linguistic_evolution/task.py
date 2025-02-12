import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = ['rhythm', 'melody', 'harmony']
        linguistic_features = ['phonology', 'syntax', 'semantics']
        mathematical_principles = ['Markov chains', 'dynamical systems', 'network theory']
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "linguistic_feature": random.choice(linguistic_features),
                "mathematical_principle": random.choice(mathematical_principles)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "linguistic_feature": random.choice(linguistic_features),
                "mathematical_principle": random.choice(mathematical_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates the co-evolution of music and language in a hypothetical culture, focusing on the musical element of {t['musical_element']}, the linguistic feature of {t['linguistic_feature']}, and using the mathematical principle of {t['mathematical_principle']} for analysis and prediction. Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the key components of your computational model and how they interact.
   b) Explain how your model incorporates the specified musical element and linguistic feature.
   c) Detail how you integrate the given mathematical principle into your model.
   d) Discuss any novel techniques or algorithms used in your design.

2. Evolutionary Dynamics (250-300 words):
   a) Explain how your model simulates the co-evolution of music and language over time.
   b) Describe the mechanisms for cultural transmission and innovation in your model.
   c) Discuss how you handle the interaction between musical and linguistic evolution.

3. Mathematical Analysis (200-250 words):
   a) Provide a detailed explanation of how you apply {t['mathematical_principle']} in your model.
   b) Include at least one relevant equation or formal notation.
   c) Explain how this mathematical approach enhances the model's predictive capabilities.

4. Simulation and Predictions (250-300 words):
   a) Describe a specific simulation scenario using your model.
   b) Present the results of this simulation, focusing on the evolution of {t['musical_element']} and {t['linguistic_feature']}.
   c) Make three specific predictions about long-term cultural evolution based on your model.

5. Interdisciplinary Implications (200-250 words):
   a) Discuss how your model contributes to our understanding of cultural evolution.
   b) Explain potential applications in fields such as anthropology, cognitive science, or AI.
   c) Propose a future research direction that builds on your model's capabilities.

6. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or biases in your model.
   b) Discuss ethical considerations in modeling cultural evolution.
   c) Propose guidelines for the responsible use and development of such models.

Ensure your response demonstrates a deep understanding of musicology, linguistics, cultural evolution theory, and mathematical modeling. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and cultural sensitivity.

Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of musicology, linguistics, cultural evolution theory, and mathematical modeling.",
            "The model architecture is well-designed and integrates all required components effectively.",
            "The evolutionary dynamics are well-explained and plausible.",
            "The mathematical analysis is thorough and correctly applies the specified principle.",
            "The simulation and predictions are detailed and insightful.",
            "The interdisciplinary implications are well-considered and demonstrate broad understanding.",
            "Limitations and ethical considerations are thoroughly addressed.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "All sections are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
