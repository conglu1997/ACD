import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'scenario': 'Medical diagnosis',
                'options': ['Treatment A', 'Treatment B'],
                'context': 'A doctor must decide between two treatments for a patient with a rare disease.'
            },
            {
                'scenario': 'Financial investment',
                'options': ['Stock market', 'Real estate'],
                'context': 'An investor must choose between two investment opportunities with uncertain outcomes.'
            },
            {
                'scenario': 'Career choice',
                'options': ['Academia', 'Industry'],
                'context': 'A recent PhD graduate must decide between pursuing a career in academia or industry.'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model for decision-making in the following scenario: {t['scenario']}. The decision is between {t['options'][0]} and {t['options'][1]}. Context: {t['context']}

Your task has the following components:

1. Quantum Cognitive Model (250-300 words):
   a) Describe your quantum-inspired cognitive model for decision-making.
   b) Explain how it incorporates quantum principles (e.g., superposition, entanglement, interference).
   c) Discuss how your model represents the decision-making process for the given scenario.

2. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of your model using quantum formalism.
   b) Explain the key equations or operators in your model.
   c) Describe how you calculate the probabilities of different decision outcomes.

3. Simulation Design (250-300 words):
   a) Outline a simulation procedure to test your quantum cognitive model.
   b) Explain how you would set up the initial conditions and parameters.
   c) Describe how you would run multiple trials and collect data.
   d) Provide a simple pseudocode or code snippet (about 10-15 lines) illustrating a key part of your simulation.

4. Comparative Analysis (200-250 words):
   a) Propose a classical (non-quantum) model for the same decision-making scenario.
   b) Compare the predictions of your quantum model with the classical model.
   c) Discuss potential experimental methods to distinguish between the two models.

5. Implications and Limitations (150-200 words):
   a) Discuss the implications of your quantum cognitive model for understanding human decision-making.
   b) Address potential criticisms or limitations of applying quantum concepts to cognition.
   c) Suggest future research directions or extensions of your model.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and cognitive science principles.",
            "The quantum cognitive model is creative, scientifically plausible, and clearly explained.",
            "The mathematical formulation accurately represents the proposed model using quantum formalism.",
            "The simulation design is well-thought-out, and the provided pseudocode or code snippet is relevant and implementable.",
            "The comparative analysis between quantum and classical models is scientifically sound and insightful.",
            "The response addresses implications and limitations of the quantum cognitive approach thoughtfully.",
            "The response adheres to the specified word count for each section and the overall submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
