import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neural_processes = [
            {
                "process": "Synaptic transmission",
                "quantum_effect": "Quantum tunneling",
                "cognitive_function": "Memory formation"
            },
            {
                "process": "Action potential propagation",
                "quantum_effect": "Quantum coherence",
                "cognitive_function": "Information processing speed"
            },
            {
                "process": "Neurotransmitter release",
                "quantum_effect": "Quantum entanglement",
                "cognitive_function": "Decision making"
            },
            {
                "process": "Dendritic integration",
                "quantum_effect": "Quantum superposition",
                "cognitive_function": "Pattern recognition"
            }
        ]
        return {
            "1": random.choice(neural_processes),
            "2": random.choice(neural_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model that incorporates quantum effects in neural signaling and cognition, focusing on {t['process']} and the quantum phenomenon of {t['quantum_effect']}. Analyze how this model might influence our understanding of {t['cognitive_function']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain the key aspects of {t['process']} and {t['quantum_effect']} relevant to your model.
   b) Describe how your model integrates these quantum effects into neural signaling.
   c) Discuss any novel mathematical or physical formulations required for your model.

2. Model Architecture (250-300 words):
   a) Outline the basic structure and components of your quantum neural signaling model.
   b) Explain how information is encoded, processed, and transmitted in your model.
   c) Describe how your model differs from classical neural signaling models.

3. Cognitive Implications (200-250 words):
   a) Analyze how your quantum neural signaling model might influence {t['cognitive_function']}.
   b) Compare the potential capabilities of your model to classical neural models in this cognitive domain.
   c) Discuss any unique cognitive phenomena your model might be particularly suited to explain.

4. Experimental Design (250-300 words):
   a) Propose two experiments that could test the predictions of your quantum neural signaling model.
   b) For each experiment, describe the methodology, expected results, and how they would support or refute your model.
   c) Discuss any technical challenges in performing these experiments and how they might be overcome.

5. Implications for AI and Consciousness (200-250 words):
   a) Explore how your model might influence the development of quantum-inspired artificial neural networks.
   b) Discuss any implications for our understanding of consciousness and the hard problem of qualia.
   c) Consider potential ethical considerations related to the development and application of quantum neural technologies.

Ensure your response demonstrates a deep understanding of quantum mechanics, neurobiology, and cognitive science. Be creative in your approach while maintaining scientific rigor and plausibility. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience.

Format your response using clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['process']} and {t['quantum_effect']} and how they might interact in neural signaling.",
            f"The model provides a plausible mechanism for how quantum effects could influence {t['cognitive_function']}.",
            "The proposed experiments are well-designed and directly test the model's predictions.",
            "The response shows creativity and interdisciplinary thinking while maintaining scientific plausibility.",
            "The implications for AI and consciousness are thoughtfully explored and grounded in the proposed model."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
