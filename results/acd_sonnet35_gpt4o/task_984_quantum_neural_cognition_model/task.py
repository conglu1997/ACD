import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_aspects = [
            {
                'aspect': 'Decision-making under uncertainty',
                'quantum_property': 'Superposition',
                'brain_region': 'Prefrontal cortex'
            },
            {
                'aspect': 'Memory formation and retrieval',
                'quantum_property': 'Entanglement',
                'brain_region': 'Hippocampus'
            }
        ]
        return {str(i+1): aspect for i, aspect in enumerate(cognitive_aspects)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum neural network model that mimics the cognitive aspect of {t['aspect']} in the human brain. Your model should incorporate the quantum property of {t['quantum_property']} and focus on the {t['brain_region']}. Provide your response in the following format:

1. Quantum Neural Network Architecture (300-350 words):
   a) Describe the key components of your quantum neural network model.
   b) Explain how it incorporates the specified quantum property.
   c) Detail how your model represents and processes information related to the given cognitive aspect.
   d) Include a diagram or mathematical representation of your model's architecture (using ASCII art or equations).

2. Quantum-Classical Interface (200-250 words):
   a) Explain how your model bridges quantum and classical information processing.
   b) Discuss how it accounts for decoherence in the biological environment.
   c) Describe any emergent properties arising from this quantum-classical interface.

3. Cognitive Simulation (250-300 words):
   a) Provide a detailed example of how your model would simulate the specified cognitive aspect.
   b) Compare your model's approach to classical neural network models for the same cognitive function.
   c) Discuss potential advantages and limitations of your quantum approach.

4. Neuroscientific Implications (200-250 words):
   a) Analyze how your model aligns with current neuroscientific understanding of the specified brain region and cognitive aspect.
   b) Propose two testable predictions your model makes about brain function or cognition.
   c) Suggest experiments that could validate these predictions.

5. AI and Cognitive Science Applications (150-200 words):
   a) Discuss potential applications of your model in AI development.
   b) Explain how your model could contribute to our understanding of human cognition.
   c) Propose a novel research direction combining quantum computing, neuroscience, and AI based on your model.

6. Ethical Considerations (100-150 words):
   Discuss potential ethical implications or concerns related to the development and application of quantum neural networks that mimic human cognition.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Be creative and innovative while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence.",
            "The quantum neural network architecture is well-explained and incorporates the specified quantum property.",
            "The model's approach to simulating the given cognitive aspect is creative, plausible, and clearly explained.",
            "The discussion of neuroscientific implications and proposed experiments is thoughtful and well-reasoned.",
            "The proposed applications and research directions show innovative thinking in combining quantum computing, neuroscience, and AI.",
            "The ethical considerations are comprehensive and demonstrate foresight."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
