import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            {
                "phenomenon": "Emergence of populist movements",
                "context": "Economic recession and technological disruption"
            },
            {
                "phenomenon": "Shifts in collective cultural values",
                "context": "Rapid climate change and global migration patterns"
            },
            {
                "phenomenon": "Evolution of social trust networks",
                "context": "Widespread misinformation and cybersecurity threats"
            },
            {
                "phenomenon": "Dynamics of social inequality",
                "context": "Automation and the future of work"
            }
        ]
        return {
            "1": random.choice(phenomena),
            "2": random.choice(phenomena)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and predicts the complex social phenomenon of {t['phenomenon']} in the context of {t['context']}. Your system should integrate principles from sociology, network theory, and chaos theory to model and forecast societal dynamics. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain how sociology, network theory, and chaos theory can be combined to understand {t['phenomenon']}.
   b) Describe key concepts from each field that are relevant to analyzing this phenomenon.
   c) Propose a novel theoretical framework that integrates these disciplines for studying {t['phenomenon']}.

2. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system incorporates sociological theories, network analysis, and chaos modeling.
   c) Detail the data inputs your system would require and how it would process them.
   d) Discuss any novel computational approaches in your design that enable complex social predictions.

3. Predictive Modeling Process (250-300 words):
   a) Outline the steps your AI system would take to generate predictions about {t['phenomenon']}.
   b) Explain how your system accounts for the non-linear dynamics and emergent properties of social systems.
   c) Describe how your model handles uncertainty and multiple possible future scenarios.
   d) Provide a specific example of how your system might predict an aspect of {t['phenomenon']} in the context of {t['context']}, including potential outcomes and their likelihoods.

4. Validation and Refinement (200-250 words):
   a) Propose methods to validate your AI system's predictions against real-world data.
   b) Describe how your system could learn and improve its predictive capabilities over time.
   c) Discuss the challenges in assessing the accuracy of long-term social predictions and how your system addresses them.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI to predict social phenomena.
   b) Address concerns about privacy, data use, and potential misuse of the system.
   c) Propose guidelines for the responsible development and application of your AI system.

6. Interdisciplinary Insights (200-250 words):
   a) Explain how your AI system could contribute to our understanding of complex social dynamics.
   b) Discuss potential applications of this technology in fields such as public policy, urban planning, or conflict resolution.
   c) Propose a novel research question in sociology or a related field that could be explored using your AI system.

7. Limitations and Future Work (150-200 words):
   a) Identify and discuss potential limitations of your proposed AI system.
   b) Suggest areas for improvement and future research directions.
   c) Explain how these limitations might impact the system's predictions and applications.

8. Real-World Scenario Analysis (150-200 words):
   a) Present a specific real-world scenario related to {t['phenomenon']} in the context of {t['context']}.
   b) Walk through how your AI system would analyze and predict outcomes for this scenario.
   c) Discuss the potential implications of your system's predictions for decision-makers.

Ensure your response demonstrates a deep understanding of sociology, network theory, chaos theory, and AI systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1650-2050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of sociology, network theory, chaos theory, and AI systems.",
            f"The proposed AI system effectively integrates multiple disciplines to analyze and predict {t['phenomenon']} in the context of {t['context']}.",
            "The conceptual framework and AI system architecture are innovative and scientifically grounded.",
            "The predictive modeling process and validation methods are well-explained and plausible.",
            "Ethical considerations and interdisciplinary insights are thoughtfully addressed.",
            "The limitations of the system are critically analyzed, and future work is proposed.",
            "A specific real-world scenario is presented and analyzed using the proposed AI system.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
