import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "superposition",
                "linguistic_application": "ambiguous word meanings"
            },
            {
                "concept": "entanglement",
                "linguistic_application": "contextual dependencies"
            }
        ]
        return {
            "1": random.choice(quantum_concepts),
            "2": random.choice(quantum_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model that incorporates the quantum concept of {t['concept']} to handle {t['linguistic_application']} in natural language processing. Your task has the following parts:

1. Quantum-Linguistic Framework (250-300 words):
   a) Explain how the quantum concept of {t['concept']} can be applied to language processing.
   b) Describe the key components of your quantum-inspired language model.
   c) Explain how your model handles {t['linguistic_application']} using quantum principles.

2. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of your quantum-linguistic model.
   b) Explain how quantum states are represented and manipulated in your model.
   c) Describe how measurements or observations are performed on your quantum-linguistic states.

3. AI Implementation (200-250 words):
   a) Outline the architecture of an AI system that implements your quantum-linguistic model.
   b) Explain how classical NLP techniques are integrated with quantum-inspired algorithms.
   c) Discuss any potential computational challenges and how they might be addressed.

4. Application Scenario (150-200 words):
   Provide a specific example of how your quantum-linguistic AI model would process and interpret a given text or phrase, demonstrating its handling of {t['linguistic_application']}.

5. Comparative Analysis (150-200 words):
   Compare your quantum-inspired model to traditional NLP approaches, discussing potential advantages and limitations.

6. Implications and Future Directions (100-150 words):
   a) Discuss the potential implications of your model for our understanding of language and cognition.
   b) Propose future research directions or extensions of your quantum-linguistic AI model.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum concept of {t['concept']} and its application to {t['linguistic_application']}.",
            "The quantum-linguistic framework is well-explained and scientifically plausible.",
            "The mathematical formulation is coherent and correctly applies quantum principles to linguistics.",
            "The AI implementation is feasible and integrates quantum-inspired algorithms with classical NLP techniques.",
            "The application scenario clearly demonstrates the model's ability to handle the specified linguistic challenge.",
            "The comparative analysis provides insightful comparisons between the quantum-inspired model and traditional NLP approaches."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
