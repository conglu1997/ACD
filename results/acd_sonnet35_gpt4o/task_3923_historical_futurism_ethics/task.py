import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_periods = [
            {
                "period": "Ancient Rome",
                "focus": "Political structure"
            },
            {
                "period": "Renaissance Italy",
                "focus": "Artistic and scientific advancement"
            },
            {
                "period": "Industrial Revolution Britain",
                "focus": "Economic system"
            },
            {
                "period": "Edo Period Japan",
                "focus": "Social hierarchy"
            }
        ]
        return {
            "1": random.choice(historical_periods),
            "2": random.choice(historical_periods)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a hypothetical future society based on the {t['focus']} of {t['period']}, then analyze its ethical implications and potential societal impacts. Your task has the following components:\n\n1. Historical Analysis (200-250 words):\n   a) Briefly describe the key characteristics of the {t['focus']} in {t['period']}.\n   b) Explain how these characteristics influenced society during that time.\n   c) Identify any lasting impacts or modern parallels of this historical model.\n\n2. Future Society Design (300-350 words):\n   a) Outline the structure and key features of your hypothetical future society, based on the {t['focus']} of {t['period']}.\n   b) Explain how you've adapted historical elements to a futuristic context.\n   c) Describe the technological and social advancements that support this societal model.\n   d) Discuss how this society addresses current global challenges (e.g., climate change, resource scarcity, inequality).\n\n3. Ethical Analysis (250-300 words):\n   a) Identify and analyze at least three potential ethical issues arising from your proposed society.\n   b) Discuss how these ethical concerns relate to current philosophical debates.\n   c) Propose potential solutions or mitigations for these ethical challenges.\n\n4. Societal Impact Assessment (200-250 words):\n   a) Predict potential positive and negative consequences of implementing this societal model.\n   b) Analyze how this society might affect human rights, individual freedoms, and social justice.\n   c) Discuss potential resistance or opposition to this societal structure and how it might be addressed.\n\n5. Comparative Analysis (150-200 words):\n   a) Compare your proposed society to at least two other historical or fictional societal models.\n   b) Discuss the relative strengths and weaknesses of your approach.\n   c) Explain how your model contributes to our understanding of societal development and organization.\n\n6. Reflection and Implications (150-200 words):\n   a) Reflect on the challenges and insights gained from this exercise in historical futurism.\n   b) Discuss the potential value of such thought experiments for addressing real-world societal issues.\n   c) Propose a framework for ethically evaluating potential future societal models.\n\nEnsure your response demonstrates a deep understanding of historical context, ethical reasoning, and societal dynamics. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining logical consistency and plausibility.\n\nFormat your response using the following structure:\n1. Historical Analysis\n   a) ...\n   b) ...\n   c) ...\n2. Future Society Design\n   a) ...\n   b) ...\n   c) ...\n   d) ...\n(Continue with the remaining sections and subsections)\n\nUse in-text citations or references to support your historical analysis and ethical reasoning. Your total response should be between 1250-1550 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['focus']} in {t['period']} and creatively adapts it to a future context.",
            "The proposed future society is well-structured, internally consistent, and addresses current global challenges.",
            "The ethical analysis is thorough, identifying multiple issues and relating them to current philosophical debates.",
            "The societal impact assessment considers both positive and negative consequences, including effects on human rights and social justice.",
            "The comparative analysis and reflection demonstrate critical thinking and provide valuable insights into societal development.",
            "The response follows the required format, including all specified sections and subsections.",
            "The submission includes appropriate in-text citations or references to support historical analysis and ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
