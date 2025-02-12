import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            {
                "function": "Memory formation and retrieval",
                "quantum_concept": "Quantum superposition",
                "brain_region": "Hippocampus"
            },
            {
                "function": "Decision making",
                "quantum_concept": "Quantum entanglement",
                "brain_region": "Prefrontal cortex"
            }
        ]
        return {
            "1": random.choice(cognitive_functions),
            "2": random.choice(cognitive_functions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for artificial intelligence, focusing on the cognitive function of {t['function']}. Your architecture should integrate the quantum computing concept of {t['quantum_concept']} and be inspired by the functionality of the {t['brain_region']}. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain how the chosen quantum concept ({t['quantum_concept']}) relates to the specified cognitive function.
   b) Describe how the functionality of the given brain region informs your architecture design.
   c) Discuss the potential advantages of a quantum-inspired approach for this cognitive function.

2. Architecture Design (300-350 words):
   a) Present a detailed design of your quantum-inspired cognitive architecture.
   b) Explain how your design incorporates the quantum concept and neural inspiration.
   c) Describe the key components and their interactions within your architecture.
   d) Include a high-level diagram or flowchart of your architecture (describe it textually).
   e) Provide at least two specific examples or use cases that demonstrate how your architecture would process information.

3. Quantum-Classical Interface (200-250 words):
   a) Explain how your architecture interfaces between quantum and classical computing elements.
   b) Discuss any novel approaches you've developed to handle this interface.
   c) Address potential challenges in implementing this interface and propose solutions.

4. Learning and Adaptation (200-250 words):
   a) Describe how your architecture learns and adapts over time.
   b) Explain how the quantum-inspired elements contribute to learning capabilities.
   c) Compare your approach to learning with traditional AI architectures.

5. Performance Analysis (150-200 words):
   a) Propose metrics to evaluate the performance of your architecture.
   b) Predict potential advantages and limitations compared to classical AI architectures.
   c) Suggest an experiment to test the efficacy of your architecture for the given cognitive function.

6. Ethical Implications and Future Directions (150-200 words):
   a) Discuss potential ethical considerations of implementing your architecture.
   b) Explore possible societal impacts of AI systems with quantum-inspired cognition.
   c) Suggest two future research directions to enhance or expand your architecture.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum concept and its relation to the cognitive function.",
            "The architecture design is innovative, well-explained, and integrates quantum and neural principles effectively.",
            "The quantum-classical interface is addressed thoroughly with consideration of implementation challenges.",
            "The learning and adaptation mechanisms are clearly explained and compared to traditional AI approaches.",
            "The performance analysis and proposed experiment are well-reasoned and appropriate for the architecture.",
            "Ethical implications and future directions are thoughtfully considered and discussed.",
            "The overall response shows strong interdisciplinary knowledge integration and creative problem-solving.",
            "The response includes specific examples or use cases that demonstrate how the architecture would process information."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
