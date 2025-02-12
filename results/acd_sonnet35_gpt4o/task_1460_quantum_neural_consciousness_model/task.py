import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = [
            {
                "aspect": "Self-awareness",
                "quantum_concept": "Quantum superposition",
                "neural_correlate": "Default mode network"
            },
            {
                "aspect": "Attention",
                "quantum_concept": "Quantum entanglement",
                "neural_correlate": "Thalamo-cortical loops"
            },
            {
                "aspect": "Memory formation",
                "quantum_concept": "Quantum tunneling",
                "neural_correlate": "Hippocampal-cortical interactions"
            },
            {
                "aspect": "Decision-making",
                "quantum_concept": "Quantum measurement",
                "neural_correlate": "Prefrontal cortex activity"
            }
        ]
        return {
            "1": random.choice(consciousness_aspects),
            "2": random.choice(consciousness_aspects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired neural network model that mimics the aspect of human consciousness: {t['aspect']}. Your model should incorporate the quantum concept of {t['quantum_concept']} and consider the neural correlate of {t['neural_correlate']}. Your response should include:

1. Model Architecture (250-300 words):
   a) Describe the overall structure of your quantum-inspired neural network model.
   b) Explain how it incorporates principles from quantum mechanics, neuroscience, and artificial intelligence.
   c) Detail how your model addresses the specific aspect of consciousness.

2. Quantum-Neural Integration (200-250 words):
   a) Explain how the quantum concept of {t['quantum_concept']} is implemented in your model.
   b) Describe how this quantum feature interacts with the neural network components.
   c) Discuss how this integration contributes to modeling the {t['aspect']} aspect of consciousness.

3. Neuroscientific Basis (200-250 words):
   a) Explain how your model incorporates current neuroscientific understanding of {t['neural_correlate']}.
   b) Discuss how your model's architecture reflects known brain structures or processes related to {t['aspect']}.
   c) Address any simplifications or assumptions your model makes about brain function.

4. Consciousness Simulation (200-250 words):
   a) Describe how your model would simulate or represent the {t['aspect']} aspect of consciousness.
   b) Provide a specific example or scenario demonstrating your model's operation.
   c) Discuss any limitations or challenges in modeling this aspect of consciousness.

5. Implications and Applications (150-200 words):
   a) Discuss potential implications of your model for our understanding of consciousness.
   b) Propose two potential applications of your model in AI or neuroscience research.
   c) Speculate on how this approach could contribute to the development of more human-like AI systems.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to modeling aspects of human consciousness.
   b) Propose guidelines for responsible development and use of such models.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all six sections as specified in the instructions.",
            "The model design incorporates principles from quantum mechanics, neuroscience, and artificial intelligence.",
            "The quantum concept and neural correlate are meaningfully integrated into the model.",
            "The response demonstrates a deep understanding of the specified aspect of consciousness.",
            "The model description is innovative while maintaining scientific plausibility.",
            "The response uses appropriate terminology and provides clear explanations of complex concepts.",
            "The ethical considerations are thoughtfully addressed.",
            "The total response is between 1100-1400 words."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
