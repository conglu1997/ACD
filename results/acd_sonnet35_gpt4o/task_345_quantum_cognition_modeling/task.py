import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "decision_context": "Career choice between two job offers",
                "quantum_concept": "Superposition"
            },
            {
                "decision_context": "Ethical dilemma in a medical setting",
                "quantum_concept": "Entanglement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-inspired model of decision-making for the context of {t['decision_context']}, incorporating the quantum concept of {t['quantum_concept']}. Your task has the following parts:

1. Model Design (250-300 words):
   a) Describe the key components of your quantum-inspired decision-making model.
   b) Explain how you incorporate the quantum concept of {t['quantum_concept']} into your model.
   c) Discuss how your model represents and processes information related to {t['decision_context']}.
   d) Include a diagram or mathematical formulation of your model (describe it textually).

2. Cognitive Implications (200-250 words):
   a) Analyze how your model might explain observed phenomena in human decision-making for {t['decision_context']}.
   b) Compare your quantum-inspired model with traditional cognitive models for this type of decision.
   c) Discuss any novel predictions or insights your model generates about human cognition.

3. AI Application (200-250 words):
   a) Propose how your quantum-inspired model could be implemented in an AI system for {t['decision_context']}.
   b) Describe potential advantages and challenges of this approach compared to classical AI methods.
   c) Discuss any ethical considerations in applying this model to AI decision-making.

4. Experimental Design (150-200 words):
   a) Propose an experiment to test a key prediction of your quantum-inspired model in human subjects.
   b) Describe how you would analyze the results to validate or refine your model.

5. Interdisciplinary Connections (100-150 words):
   a) Suggest how your quantum-inspired cognitive model might inform or be applied in fields outside of cognitive science and AI.
   b) Briefly describe potential implications for one of these fields.

Ensure your response demonstrates a deep understanding of quantum physics concepts, cognitive science, and AI principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content and length.",
            f"The model design effectively incorporates the quantum concept of {t['quantum_concept']}.",
            f"The cognitive implications and AI application are well-reasoned and relevant to {t['decision_context']}.",
            "The experimental design is feasible and appropriate for testing the model.",
            "The interdisciplinary connections are insightful and demonstrate broad understanding.",
            "The overall response shows creativity, scientific plausibility, and clear articulation of complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
