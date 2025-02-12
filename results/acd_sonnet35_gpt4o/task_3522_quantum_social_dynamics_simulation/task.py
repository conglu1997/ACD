import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_phenomena = [
            "political polarization",
            "cultural diffusion",
            "economic bubbles",
            "social movements",
            "technological adoption"
        ]
        quantum_concepts = [
            "superposition",
            "entanglement",
            "interference",
            "quantum tunneling",
            "quantum walks"
        ]
        return {
            "1": {"phenomenon": random.choice(social_phenomena), "quantum_concept": random.choice(quantum_concepts)},
            "2": {"phenomenon": random.choice(social_phenomena), "quantum_concept": random.choice(quantum_concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired model to simulate and analyze the social phenomenon of {t['phenomenon']}, focusing on how the quantum concept of {t['quantum_concept']} might influence collective decision-making and societal dynamics. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain the social phenomenon of {t['phenomenon']} and its key characteristics.
   b) Describe the quantum concept of {t['quantum_concept']} and how it might be analogous to social dynamics.
   c) Propose a novel way to apply {t['quantum_concept']} to model {t['phenomenon']}.

2. Mathematical Model (250-300 words):
   a) Develop a mathematical model that incorporates both quantum and social elements to describe {t['phenomenon']}.
   b) Explain the key variables, parameters, and equations in your model.
   c) Discuss any assumptions or simplifications made in your model.

3. Simulation Design (200-250 words):
   a) Outline the steps to implement your model in a computational simulation.
   b) Describe how you would initialize the simulation and what data inputs it would require.
   c) Explain how you would measure and analyze the outcomes of the simulation.

4. Predictions and Implications (200-250 words):
   a) Use your model to make specific predictions about how {t['quantum_concept']} might affect {t['phenomenon']}.
   b) Discuss potential societal implications if your model's predictions are accurate.
   c) Propose an experiment or data collection method that could validate your model's predictions.

5. Comparative Analysis (150-200 words):
   a) Compare your quantum-inspired model with a classical model of {t['phenomenon']}.
   b) Discuss the key differences in predictions or explanatory power between the two models.
   c) Analyze the conditions under which quantum effects would be most relevant or negligible in your model.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of applying quantum concepts to social phenomena.
   b) Address limitations of your approach and potential misuse of the model.
   c) Propose guidelines for responsible development and application of quantum social science models.

7. Conclusion (50-100 words):
   Summarize the key points of your quantum social dynamics model and its potential impact on our understanding of {t['phenomenon']}.

Ensure your response demonstrates a deep understanding of quantum mechanics, social psychology, and complex systems theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['phenomenon']} and {t['quantum_concept']}.",
            "The mathematical model effectively integrates quantum and social elements.",
            "The simulation design is well-explained and implementable.",
            "The predictions and implications are logical and insightful.",
            "The comparative analysis shows a deep understanding of both quantum and classical approaches.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The response is creative, scientifically plausible, and well-structured.",
            "The response adheres to the specified word count ranges for each section.",
            "A concise conclusion summarizing the key points is provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
