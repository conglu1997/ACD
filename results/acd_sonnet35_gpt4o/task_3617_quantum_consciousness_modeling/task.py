import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_phenomenon': 'Quantum entanglement',
                'brain_region': 'Prefrontal cortex',
                'cognitive_function': 'Decision making',
                'consciousness_aspect': 'Self-awareness'
            },
            {
                'quantum_phenomenon': 'Quantum superposition',
                'brain_region': 'Hippocampus',
                'cognitive_function': 'Memory formation',
                'consciousness_aspect': 'Temporal continuity of experience'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model that bridges quantum mechanics and consciousness, proposing a mechanism for how quantum phenomena might influence or give rise to conscious experience. Your model should focus on the quantum phenomenon of {t['quantum_phenomenon']}, primarily involve the {t['brain_region']}, and address the cognitive function of {t['cognitive_function']} and the consciousness aspect of {t['consciousness_aspect']}.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain the key principles of quantum mechanics relevant to your model, focusing on {t['quantum_phenomenon']}.
   b) Describe current understanding of the neural correlates of consciousness, particularly in relation to the {t['brain_region']}.
   c) Discuss existing theories or models that attempt to link quantum phenomena to consciousness.
   d) Explain how your model builds upon or differs from these existing approaches.

2. Model Architecture (250-300 words):
   a) Describe the key components and mechanisms of your quantum consciousness model.
   b) Explain how {t['quantum_phenomenon']} is integrated into your model of brain function.
   c) Detail how your model accounts for the cognitive function of {t['cognitive_function']}.
   d) Discuss how your model addresses the consciousness aspect of {t['consciousness_aspect']}.

3. Quantum-Neural Interface (200-250 words):
   a) Propose a mechanism for how quantum effects could influence neural activity in the {t['brain_region']}.
   b) Explain how this interface might give rise to or influence conscious experience.
   c) Address potential criticisms regarding the scale disparity between quantum and neural phenomena.

4. Predictions and Testability (200-250 words):
   a) Describe specific, testable predictions that your model makes about consciousness or brain function.
   b) Propose experiments or observations that could potentially validate or refute your model.
   c) Discuss any technological limitations that might hinder testing your model and how they might be overcome.

5. Philosophical and Ethical Implications (200-250 words):
   a) Discuss the philosophical implications of your model for our understanding of consciousness and free will.
   b) Consider potential ethical concerns or societal impacts if your model were to be validated.
   c) Reflect on how your model might influence our conception of human identity and cognition.

6. Limitations and Future Directions (150-200 words):
   a) Acknowledge potential weaknesses or limitations of your proposed model.
   b) Suggest areas for future research or refinement of your quantum consciousness model.
   c) Speculate on how advances in quantum technology might impact future investigations in this field.

Ensure your response demonstrates a deep understanding of both quantum mechanics and neuroscience. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering strictly to the word limits provided. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The theoretical framework effectively explains {t['quantum_phenomenon']} and its potential relevance to consciousness, particularly in the {t['brain_region']}.",
            f"The model architecture clearly integrates {t['quantum_phenomenon']} with neural processes and addresses {t['cognitive_function']} and {t['consciousness_aspect']}.",
            f"The quantum-neural interface proposes a plausible mechanism for quantum effects influencing neural activity in the {t['brain_region']}.",
            "The response includes specific, testable predictions and proposed experiments to validate the model.",
            "The philosophical and ethical implications of the model are thoroughly discussed.",
            "The response acknowledges limitations of the proposed model and suggests future research directions.",
            "The overall response demonstrates deep understanding and creative integration of quantum mechanics and neuroscience concepts, while adhering to scientific plausibility and the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
