import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'psychological_phenomenon': 'Decision-making under uncertainty'
            },
            {
                'quantum_principle': 'Entanglement',
                'psychological_phenomenon': 'Cognitive dissonance'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive model based on the quantum mechanics principle of {t['quantum_principle']} and apply it to explain the psychological phenomenon of {t['psychological_phenomenon']}. Your task has the following parts:

1. Quantum Principle Explanation (100-150 words):
   Explain the quantum principle of {t['quantum_principle']} in simple terms. Discuss its key features and how it challenges classical intuitions.

2. Psychological Phenomenon Description (100-150 words):
   Describe the psychological phenomenon of {t['psychological_phenomenon']}. Explain its main characteristics and why it's challenging to explain using classical cognitive models.

3. Quantum Cognitive Model Design (200-300 words):
   a) Propose a cognitive model that applies the quantum principle to explain the psychological phenomenon.
   b) Describe the key components of your model and how they map to both the quantum principle and the psychological phenomenon.
   c) Explain how your model accounts for aspects of the phenomenon that classical models struggle with.

4. Mathematical Formulation (100-200 words):
   Provide a basic mathematical formulation of your model. Use appropriate notation from both quantum mechanics and cognitive science. Explain the meaning of each term or operator in your formulation.

5. Testable Predictions (100-150 words):
   Describe two specific, testable predictions that your quantum cognitive model makes about human behavior or cognition. Explain how these predictions differ from what classical models would predict.

6. Limitations and Future Directions (100-150 words):
   Discuss potential limitations of your model and propose two future research directions that could address these limitations or extend the model's applicability.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Avoid direct quotations from existing literature and focus on original, well-reasoned ideas.

Balance creativity with scientific rigor throughout your response. Your model should be innovative yet grounded in established principles from both quantum mechanics and cognitive science.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the quantum principle is accurate and clear.",
            "The description of the psychological phenomenon is comprehensive and accurate.",
            "The proposed quantum cognitive model creatively and logically applies the quantum principle to explain the psychological phenomenon.",
            "The mathematical formulation is appropriate and well-explained.",
            "The testable predictions are specific, novel, and logically derived from the model.",
            "The discussion of limitations and future directions shows critical thinking and insight.",
            "The overall response demonstrates a deep understanding of both quantum mechanics and cognitive science, and their potential integration.",
            "The response shows originality and avoids direct quotations from existing literature.",
            "The model balances creativity with scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
