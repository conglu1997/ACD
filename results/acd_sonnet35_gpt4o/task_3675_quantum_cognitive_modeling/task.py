import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                "process": "ambiguity aversion",
                "quantum_principle": "superposition",
                "decision_context": "financial investment"
            },
            {
                "process": "confirmation bias",
                "quantum_principle": "entanglement",
                "decision_context": "political opinion formation"
            }
        ]
        return {
            "1": random.choice(cognitive_processes),
            "2": random.choice(cognitive_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        quantum_principle_explanation = {
            "superposition": "the principle that a quantum system can exist in multiple states simultaneously until measured",
            "entanglement": "the phenomenon where quantum particles become correlated in such a way that the quantum state of each particle cannot be described independently"
        }
        return f"""Design a theoretical quantum cognitive model for human decision-making under uncertainty, focusing on the cognitive process of {t['process']}. Your model should incorporate the quantum principle of {t['quantum_principle']} ({quantum_principle_explanation[t['quantum_principle']]}) and be applied to the decision context of {t['decision_context']}. Then, analyze the implications of your model for psychology and quantum information theory. Your response should include the following sections:

1. Quantum Cognitive Model Design (300-350 words):
   a) Describe the key components of your quantum cognitive model.
   b) Explain how your model incorporates the specified quantum principle to represent {t['process']}.
   c) Detail how your model simulates decision-making in the context of {t['decision_context']}.
   d) Provide a mathematical formulation of a critical aspect of your model using quantum mechanical notation.

2. Model Behavior and Predictions (250-300 words):
   a) Describe how your model behaves under different decision scenarios.
   b) Explain how the quantum aspects of your model influence the decision-making process.
   c) Provide a specific example of a decision scenario and the prediction your model would make.
   d) Compare your model's predictions with those of classical cognitive models.

3. Psychological Implications (200-250 words):
   a) Analyze how your quantum cognitive model could enhance our understanding of {t['process']}.
   b) Discuss potential insights your model provides into human decision-making under uncertainty.
   c) Explore how your model might inform new approaches to cognitive psychology research.

4. Quantum Information Theory Advancements (200-250 words):
   a) Explain how your model contributes to the field of quantum information theory.
   b) Discuss any novel quantum effects or principles your model exploits or reveals.
   c) Analyze the theoretical advantages of your quantum approach over classical methods for cognitive modeling.

5. Experimental Validation Proposal (150-200 words):
   a) Propose an experiment to test the predictions of your quantum cognitive model.
   b) Describe the methodology and expected outcomes of your proposed experiment.
   c) Discuss potential challenges in experimentally validating quantum effects in cognition.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss the ethical implications of applying quantum principles to model human cognition.
   b) Explore potential societal impacts of quantum cognitive models.
   c) Suggest future research directions or applications stemming from your quantum cognitive model.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The quantum cognitive model effectively incorporates {t['quantum_principle']} to represent {t['process']} in the context of {t['decision_context']}.",
            "The response demonstrates a deep understanding of both quantum mechanics and cognitive science principles.",
            "The model's implications for psychology and quantum information theory are thoroughly analyzed.",
            "The proposed experiment for model validation is well-designed and scientifically sound.",
            "The response shows creativity and interdisciplinary knowledge integration while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
