import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            "protein folding",
            "gene regulatory networks",
            "neurotransmitter dynamics",
            "cellular metabolism",
            "immune system response"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing",
            "quantum walk"
        ]
        return {
            "1": {
                "biological_system": random.choice(biological_systems),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired artificial neural network architecture for modeling the complex biological system of {t['biological_system']}, incorporating the quantum principle of {t['quantum_principle']}. A quantum-inspired neural network is a classical neural network that incorporates ideas or algorithms inspired by quantum computing to potentially enhance its performance or capabilities.

Your response should include the following sections:

1. Quantum-Biological System Analysis (200-250 words):
   a) Briefly explain the key features and challenges of modeling the given biological system.
   b) Describe how the specified quantum principle could be relevant or beneficial in this context.
   c) Discuss potential analogies between quantum phenomena and biological processes in this system.

2. Quantum-Inspired Neural Network Architecture (250-300 words):
   a) Design a novel neural network architecture that incorporates quantum-inspired elements.
   b) Explain how your architecture leverages the specified quantum principle.
   c) Describe the key components, layers, and connections in your network.
   d) Include a simple ASCII art diagram illustrating the main features of your architecture.

3. Training and Optimization Strategy (200-250 words):
   a) Propose a training method for your quantum-inspired neural network.
   b) Explain how this method differs from classical neural network training.
   c) Discuss potential challenges in training and how to address them.

4. Performance Analysis and Comparison (200-250 words):
   a) Predict the potential advantages of your quantum-inspired architecture over classical approaches.
   b) Discuss any trade-offs or limitations of your approach.
   c) Propose metrics to evaluate the performance of your model in the context of the biological system.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how your architecture might contribute to advancements in computational biology or quantum computing.
   b) Explore potential applications beyond the given biological system.
   c) Propose a research question that could be investigated using your architecture.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to the development or application of your quantum-inspired neural network.
   b) Propose guidelines for responsible use and development of such architectures in biological modeling.

Ensure your response demonstrates a deep understanding of neural network architectures, quantum computing principles, and the specified biological system. Be creative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words. Please adhere to the word count limits for each section as specified above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_system']} and how it can be modeled using neural networks.",
            f"The quantum-inspired neural network architecture creatively incorporates the principle of {t['quantum_principle']}.",
            "The design is innovative yet scientifically plausible, showing a strong grasp of both quantum computing and neural network principles.",
            "The response addresses all required sections with appropriate depth and insight.",
            "The ethical considerations and interdisciplinary implications are thoughtfully discussed.",
            "The response includes an ASCII art diagram illustrating the main features of the architecture.",
            "The total word count is between 1100-1400 words, with each section adhering to its specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
