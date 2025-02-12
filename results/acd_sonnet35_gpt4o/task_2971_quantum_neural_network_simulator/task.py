import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'quantum_explanation': 'The ability of a quantum system to exist in multiple states simultaneously',
                'neural_feature': 'Synaptic plasticity',
                'neural_explanation': 'The ability of synapses to strengthen or weaken over time in response to increases or decreases in their activity'
            },
            {
                'quantum_principle': 'Entanglement',
                'quantum_explanation': 'A quantum phenomenon where particles become correlated in such a way that the quantum state of each particle cannot be described independently',
                'neural_feature': 'Neuronal synchronization',
                'neural_explanation': 'The coordinated firing of groups of neurons in the brain, often associated with cognitive processes'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical quantum neural network simulator that integrates principles from quantum computing, neuroscience, and artificial intelligence to model brain-like information processing. Your simulator should focus on the quantum principle of {t['quantum_principle']} ({t['quantum_explanation']}) and the neural feature of {t['neural_feature']} ({t['neural_explanation']}).

Provide your response in the following format:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen quantum principle and neural feature, and their potential relevance to information processing.
   b) Describe how these concepts could be integrated in a quantum neural network model.
   c) Discuss the potential advantages of this integration over classical neural networks.

2. Simulator Architecture (300-350 words):
   a) Outline the main components of your quantum neural network simulator.
   b) Explain how your simulator incorporates the specified quantum principle and neural feature.
   c) Describe the data representation and processing flow in your simulator.
   d) Discuss how your simulator handles the transition between quantum and classical information.

3. Information Processing Model (200-250 words):
   a) Explain how information is encoded, processed, and retrieved in your quantum neural network.
   b) Describe any novel algorithms or methods used in your simulator.
   c) Discuss how your model differs from both classical neural networks and standard quantum computing approaches.

4. Simulation Example (200-250 words):
   a) Provide a specific example of how your simulator would model a simple cognitive task (e.g., pattern recognition, decision making).
   b) Explain step-by-step how the information would flow through your quantum neural network.
   c) Describe the expected output and how it might differ from a classical neural network.

5. Theoretical Performance Analysis (200-250 words):
   a) Analyze the potential advantages of your quantum neural network simulator.
   b) Compare its theoretical performance to classical neural networks and current quantum computing systems.
   c) Discuss any trade-offs or limitations inherent in your approach.

6. Implementation Challenges (150-200 words):
   a) Identify potential technological hurdles in realizing your quantum neural network simulator.
   b) Propose possible solutions or research directions to address these challenges.
   c) Discuss any fundamental physical or computational limits that might constrain your system.

7. Broader Implications (150-200 words):
   a) Explore potential applications of your quantum neural network simulator beyond basic cognitive tasks.
   b) Discuss how this approach might impact our understanding of both quantum computing and neuroscience.
   c) Consider any philosophical implications of your system (e.g., for our concepts of consciousness, intelligence, or the nature of reality).

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence principles.",
            "The proposed quantum neural network simulator is innovative, scientifically plausible, and well-justified.",
            "The simulator architecture effectively integrates the specified quantum principle and neural feature.",
            "The information processing model clearly explains how quantum and neural concepts are combined.",
            "The simulation example provides a clear and logical demonstration of the system's operation.",
            "The theoretical performance analysis is thorough and compares the proposed system to existing approaches.",
            "Implementation challenges and potential solutions are identified and discussed realistically.",
            "The broader implications and philosophical considerations are thoughtfully explored.",
            "The response shows strong integration of knowledge from multiple scientific disciplines.",
            "The response includes creative solutions while maintaining scientific rigor.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
