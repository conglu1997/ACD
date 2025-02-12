import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'focus_area': 'black hole information paradox',
                'quantum_principle': 'quantum entanglement',
                'cosmological_scale': 'galaxy cluster'
            },
            {
                'focus_area': 'cosmic microwave background',
                'quantum_principle': 'quantum tunneling',
                'cosmological_scale': 'observable universe'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As a theoretical physicist specializing in quantum cosmology, your task is to design a model and simulation of a holographic universe, incorporating principles from quantum physics, information theory, and cosmology. Focus on the {t['focus_area']}, the quantum principle of {t['quantum_principle']}, and apply your model to the {t['cosmological_scale']} scale. Provide your response in the following format:

1. Theoretical Model (300-350 words):
   a) Describe your holographic universe model, explaining how it incorporates the specified quantum principle and addresses the focus area.
   b) Explain how your model accounts for known cosmological observations.
   c) Discuss how your model differs from classical cosmological models.
   d) Provide a conceptual diagram or detailed description of your model's key components and interactions.

2. Quantum-Cosmological Mechanisms (200-250 words):
   a) Explain in detail how the specified quantum principle manifests in your holographic universe model.
   b) Describe the potential advantages of your model in addressing the focus area.
   c) Address potential criticisms regarding the plausibility of applying quantum effects at cosmological scales.

3. Simulation Design (200-250 words):
   a) Outline the key components and algorithms of a simulation that could model your holographic universe theory.
   b) Explain how your simulation would handle the vast scale differences between quantum and cosmological phenomena.
   c) Describe any novel computational approaches needed to implement your simulation effectively.

4. Predictions and Testable Hypotheses (200-250 words):
   a) Derive at least two specific, testable predictions from your model.
   b) Explain how these predictions differ from those of standard cosmological models.
   c) Propose experiments or observational tests to verify these predictions, considering both current and near-future technological capabilities.

5. Implications for Our Understanding of Reality (150-200 words):
   a) Discuss how your holographic universe model could inform or change our understanding of the nature of reality and information.
   b) Speculate on the potential implications for other areas of physics if your model is correct.

6. Philosophical and Ethical Considerations (100-150 words):
   a) Discuss the philosophical implications of a holographic universe model.
   b) Consider potential ethical concerns or societal impacts if such a model were proven correct.
   c) Propose guidelines for responsible research and communication in this field.

Ensure your response demonstrates a deep understanding of quantum mechanics, cosmology, and information theory. Be creative and original in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, cosmology, and information theory.",
            "The holographic universe model is creative, original, and scientifically plausible.",
            "The simulation design effectively bridges quantum and cosmological scales.",
            "The predictions and proposed experiments are specific, testable, and distinct from standard models.",
            "The implications for our understanding of reality are thoughtfully explored.",
            "The philosophical and ethical considerations are insightful and well-reasoned.",
            "The response uses appropriate technical terminology and provides clear explanations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
