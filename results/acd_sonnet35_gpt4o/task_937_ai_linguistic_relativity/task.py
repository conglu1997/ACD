import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language_feature": "grammatical gender",
                "cognitive_domain": "object classification",
                "ai_application": "image recognition systems"
            },
            {
                "language_feature": "color vocabulary",
                "cognitive_domain": "color perception",
                "ai_application": "computer vision in autonomous vehicles"
            },
            {
                "language_feature": "future tense",
                "cognitive_domain": "decision making",
                "ai_application": "predictive algorithms in finance"
            },
            {
                "language_feature": "evidentiality markers",
                "cognitive_domain": "source evaluation",
                "ai_application": "fake news detection systems"
            },
            {
                "language_feature": "spatial reference frames",
                "cognitive_domain": "navigation",
                "ai_application": "robotics in search and rescue operations"
            },
            {
                "language_feature": "counterfactual expressions",
                "cognitive_domain": "causal reasoning",
                "ai_application": "explainable AI in healthcare diagnostics"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an experiment to test the concept of linguistic relativity in artificial intelligence systems, focusing on the influence of {t['language_feature']} on {t['cognitive_domain']} in the context of {t['ai_application']}. Then, analyze the implications for AI development and human-AI interaction. Your response should include:\n\n1. Experimental Design (300-350 words):\n   a) Briefly explain the chosen language feature and its potential influence on cognition.\n   b) Describe your experimental setup, including AI systems, datasets, and control groups.\n   c) Detail the specific tasks or tests you will use to measure the influence of the language feature on the AI's cognitive processes.\n   d) Explain how you will isolate the effect of the language feature from other variables.\n   e) Discuss any ethical considerations in your experimental design.\n\n2. Hypotheses and Predictions (150-200 words):\n   a) State your main hypothesis about how the language feature will affect the AI's cognitive processes.\n   b) Provide at least two specific, testable predictions based on your hypothesis.\n   c) Explain the reasoning behind your predictions, drawing on relevant linguistic and cognitive theories.\n\n3. Data Analysis Plan (200-250 words):\n   a) Describe the key metrics you will use to evaluate your hypotheses.\n   b) Explain your planned statistical analyses or machine learning approaches for interpreting the results.\n   c) Discuss how you will account for potential confounding factors or biases in your analysis.\n\n4. Implications for AI Development (250-300 words):\n   a) Discuss how your findings could influence the development of {t['ai_application']}.\n   b) Explore potential benefits and risks of incorporating linguistic relativity principles in AI design.\n   c) Propose guidelines for developing linguistically aware AI systems based on your experiment.\n\n5. Human-AI Interaction Analysis (200-250 words):\n   a) Analyze how linguistic differences between humans and AI could affect their interaction in the context of {t['ai_application']}.\n   b) Propose strategies to mitigate potential misunderstandings or biases arising from these differences.\n   c) Discuss the ethical implications of AI systems potentially shaping human cognition through language.\n\n6. Future Research Directions (150-200 words):\n   a) Suggest two follow-up studies that could further explore the implications of your findings.\n   b) Discuss how your experimental approach could be adapted to investigate other aspects of linguistic relativity in AI.\n\nEnsure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and AI principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific rigor and plausibility. Your total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The experimental design effectively tests the influence of {t['language_feature']} on {t['cognitive_domain']} in the context of {t['ai_application']}.",
            "The hypotheses and predictions are clear, specific, and well-reasoned.",
            "The data analysis plan is comprehensive and appropriate for the experimental design.",
            "The implications for AI development are insightful and well-explained.",
            "The human-AI interaction analysis is thoughtful and considers ethical implications.",
            "The proposed future research directions are relevant and innovative.",
            "The response demonstrates a deep understanding of linguistic relativity, cognitive science, and AI principles.",
            "The response is creative and innovative while maintaining scientific rigor and plausibility.",
            "The response follows the specified format with clearly labeled sections and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
