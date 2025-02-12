import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'quantum superposition',
                'neural_network_type': 'recurrent neural network',
                'bci_application': 'motor control for paralyzed patients'
            },
            {
                'quantum_concept': 'quantum entanglement',
                'neural_network_type': 'convolutional neural network',
                'bci_application': 'direct brain-to-brain communication'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired neural network system for enhancing brain-computer interfaces (BCIs), focusing on the quantum concept of {t['quantum_concept']}, using a {t['neural_network_type']} architecture, and applying it to {t['bci_application']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired neural network BCI system.
   b) Explain how you incorporate {t['quantum_concept']} into the {t['neural_network_type']} architecture.
   c) Detail how your system interfaces with the brain and external devices.
   d) Discuss any novel algorithms or techniques used in your design.
   e) Provide a visual representation or diagram of your system architecture using ASCII art or Unicode characters (max 20 lines x 80 characters).
   f) Briefly explain your diagram (50-75 words).

2. Quantum-Neural Integration (300-350 words):
   a) Explain how {t['quantum_concept']} enhances the capabilities of the {t['neural_network_type']}.
   b) Discuss the challenges in implementing quantum-inspired algorithms in a biological context.
   c) Provide a mathematical formulation of a key aspect of your quantum-neural integration.
   d) Include a small code snippet (10-15 lines) demonstrating a crucial part of your quantum-neural integration.

3. BCI Application Analysis (200-250 words):
   a) Describe how your system would be applied to {t['bci_application']}.
   b) Analyze the potential advantages of your quantum-inspired approach over classical BCIs for this application.
   c) Discuss any limitations or challenges specific to this application.

4. Performance Evaluation (200-250 words):
   a) Propose methods to evaluate the performance of your quantum-inspired BCI system.
   b) Suggest metrics for comparing your system to classical BCI approaches.
   c) Describe a hypothetical experiment to test your system's effectiveness.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of using quantum-inspired neural networks for BCIs.
   b) Analyze potential societal impacts of your system, both positive and negative.
   c) Propose guidelines for responsible development and use of this technology.

6. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how these extensions could enhance its capabilities or address limitations.
   c) Speculate on the long-term implications of quantum-inspired BCIs for human-machine interaction.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_concept']}, {t['neural_network_type']}, and brain-computer interfaces.",
            f"The system design effectively integrates {t['quantum_concept']} with {t['neural_network_type']} for {t['bci_application']}.",
            "The response includes innovative ideas while maintaining scientific plausibility.",
            "The response includes a clear ASCII art diagram with explanation, mathematical formulation, and code snippet as requested.",
            "The ethical implications and future directions are thoroughly discussed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
