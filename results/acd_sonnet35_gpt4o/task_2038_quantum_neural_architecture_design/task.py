import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "neural_process": "Memory consolidation",
                "quantum_concept": "Quantum superposition",
                "ai_technique": "Reinforcement learning"
            },
            {
                "neural_process": "Sensory integration",
                "quantum_concept": "Quantum entanglement",
                "ai_technique": "Generative adversarial networks"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid quantum-classical neural network architecture for brain-inspired computing, focusing on the neural process of {t['neural_process']}, incorporating the quantum concept of {t['quantum_concept']}, and utilizing the AI technique of {t['ai_technique']}. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain the chosen neural process and its significance in brain function.
   b) Describe how the quantum concept can be applied to enhance this neural process.
   c) Discuss how the AI technique can be integrated into this quantum-neural framework.

2. Architecture Design (300-350 words):
   a) Provide a detailed description of your hybrid quantum-classical neural network architecture.
   b) Explain how classical and quantum components interact in your design.
   c) Describe how your architecture models the chosen neural process.
   d) Include a diagram or schematic representation of your architecture (describe it textually).

3. Quantum-Neural Interface (200-250 words):
   a) Explain how quantum operations are implemented in your neural network.
   b) Discuss potential advantages of using quantum computing in this context.
   c) Address challenges in maintaining quantum coherence in a neural network setting.

4. Learning and Adaptation (200-250 words):
   a) Describe how your architecture learns and adapts, incorporating the specified AI technique.
   b) Explain how quantum processes contribute to learning in your model.
   c) Discuss potential improvements in learning efficiency or capabilities compared to classical approaches.

5. Potential Applications (150-200 words):
   a) Propose two potential real-world applications of your quantum-neural architecture.
   b) Explain how these applications leverage the unique features of your design.

6. Ethical Implications (150-200 words):
   a) Discuss potential ethical concerns related to the development and use of quantum-neural computing systems.
   b) Propose guidelines for responsible research and application in this field.

7. Future Directions (150-200 words):
   a) Suggest potential extensions or improvements to your architecture.
   b) Discuss how advancements in quantum hardware might impact your design.
   c) Propose experiments to validate your architecture's performance and capabilities.

Ensure your response demonstrates a deep understanding of neuroscience, quantum computing, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1400-1750 words.

Include at least 5 relevant scientific citations throughout your response to support your design choices and theoretical foundations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and length.",
            f"The architecture effectively incorporates the neural process of {t['neural_process']}, the quantum concept of {t['quantum_concept']}, and the AI technique of {t['ai_technique']}.",
            "The design demonstrates a deep understanding of neuroscience, quantum computing, and artificial intelligence principles.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The ethical implications and future directions are thoughtfully considered.",
            "The response includes at least 5 relevant scientific citations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
