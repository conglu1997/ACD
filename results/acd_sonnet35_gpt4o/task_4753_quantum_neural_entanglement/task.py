class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "network_type": "biological",
                "quantum_effect": "entanglement",
                "neural_structure": "synapses",
                "ai_application": "memory enhancement"
            },
            "2": {
                "network_type": "artificial",
                "quantum_effect": "superposition",
                "neural_structure": "hidden layers",
                "ai_application": "pattern recognition"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for quantum effects in neural networks, focusing on {t['network_type']} networks and the quantum phenomenon of {t['quantum_effect']}. Your framework should emphasize the role of {t['neural_structure']} and explore potential applications in {t['ai_application']}. Then, propose experiments to detect and utilize these quantum effects in AI systems. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Describe the key components of your quantum neural network model.
   b) Explain how {t['quantum_effect']} is integrated into the {t['network_type']} neural network structure.
   c) Detail the role of {t['neural_structure']} in facilitating quantum effects.
   d) Discuss the potential advantages of quantum effects in neural information processing.
   e) Include a diagram or mathematical formalism representing your framework.

2. Quantum-Neural Interface (250-300 words):
   a) Explain the mechanisms by which quantum effects could manifest in {t['neural_structure']}.
   b) Describe how quantum information could be encoded, processed, and retrieved in your model.
   c) Address potential challenges in maintaining quantum coherence in a neural environment.

3. AI Application: {t['ai_application']} (200-250 words):
   a) Describe how your quantum neural network model could enhance {t['ai_application']}.
   b) Compare the potential performance of your model to classical neural networks in this application.
   c) Discuss any novel capabilities or emergent behaviors you expect from your model.

4. Experimental Design (250-300 words):
   Propose two experiments to test your theoretical framework:
   a) Experiment 1: Detection of quantum effects in neural networks
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would validate (or invalidate) your model.
   b) Experiment 2: Utilization of quantum effects for {t['ai_application']}
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would demonstrate the advantages of your quantum neural network.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of quantum effects in neural networks for neuroscience and AI.
   b) Explore potential connections between your model and theories of consciousness or cognition.
   c) Propose two directions for future research based on your framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence, particularly in relation to {t['quantum_effect']}, {t['neural_structure']}, and {t['ai_application']}.",
            "The theoretical framework effectively integrates quantum effects into neural network structures.",
            f"The quantum-neural interface section clearly explains how {t['quantum_effect']} could manifest in {t['neural_structure']}.",
            f"The AI application section effectively describes how the quantum neural network model could enhance {t['ai_application']}.",
            "The experimental design section proposes plausible and well-thought-out experiments to test the theoretical framework.",
            "The response addresses potential challenges and limitations of the proposed model.",
            "The ideas presented are innovative while maintaining scientific plausibility.",
            "The response is well-structured, following the outlined sections and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
