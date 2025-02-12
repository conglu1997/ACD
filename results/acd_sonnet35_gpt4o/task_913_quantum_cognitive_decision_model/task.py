import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "interference",
            "measurement"
        ]
        cognitive_processes = [
            "attention",
            "memory",
            "reasoning",
            "perception"
        ]
        decision_contexts = [
            "financial investment",
            "medical diagnosis",
            "environmental policy",
            "career choice"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "decision_context": random.choice(decision_contexts)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "decision_context": random.choice(decision_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive model for decision-making under uncertainty, focusing on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and applied to the decision context of {t['decision_context']}. Your response should include the following sections:

1. Model Overview (200-250 words):
   a) Describe the key components of your quantum-inspired cognitive model.
   b) Explain how it incorporates the quantum principle of {t['quantum_principle']}.
   c) Discuss how it models the cognitive process of {t['cognitive_process']}.
   d) Outline how the model addresses uncertainty in decision-making.

2. Mathematical Framework (250-300 words):
   a) Provide a mathematical representation of your model, using appropriate quantum mechanical formalism.
   b) Explain how your mathematical framework captures the cognitive process of {t['cognitive_process']}.
   c) Describe how your model quantifies and processes uncertainty.
   d) Include at least one equation or algorithm central to your model's functioning.

3. Application to {t['decision_context']} (200-250 words):
   a) Explain how your model would be applied to decision-making in the context of {t['decision_context']}.
   b) Provide a specific example scenario and demonstrate how your model would process it.
   c) Discuss any unique insights or advantages your model might offer in this context.

4. Empirical Predictions (150-200 words):
   a) Describe at least two testable predictions that your model makes about human decision-making behavior.
   b) Explain how these predictions differ from those of classical decision-making models.
   c) Propose an experimental setup to test one of these predictions.

5. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations or challenges of your quantum-inspired cognitive model.
   b) Propose at least two ways to address these limitations or extend the model in future research.
   c) Suggest how your model might contribute to our understanding of human cognition and decision-making processes.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 950-1200 words. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model clearly incorporates the quantum principle of {t['quantum_principle']} and the cognitive process of {t['cognitive_process']}",
            "The mathematical framework uses appropriate quantum mechanical formalism",
            f"The model is applied convincingly to the decision context of {t['decision_context']}",
            "The response includes at least one relevant equation or algorithm",
            "The model makes at least two testable predictions that differ from classical models",
            "The limitations and future directions are thoughtfully discussed",
            "The response demonstrates a deep understanding of both quantum mechanics and cognitive science",
            "The proposed model is creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
