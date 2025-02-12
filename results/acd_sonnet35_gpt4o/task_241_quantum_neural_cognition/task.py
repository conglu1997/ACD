import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_property': 'Superposition',
                'neural_process': 'Memory consolidation',
                'cognitive_function': 'Learning and adaptation'
            },
            {
                'quantum_property': 'Entanglement',
                'neural_process': 'Synaptic plasticity',
                'cognitive_function': 'Decision making'
            },
            {
                'quantum_property': 'Quantum tunneling',
                'neural_process': 'Action potential propagation',
                'cognitive_function': 'Sensory perception'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-enhanced neural network that incorporates the quantum property of {t['quantum_property']} into the neural process of {t['neural_process']}, and analyze its potential implications for the cognitive function of {t['cognitive_function']}. Your response should include:

1. Quantum-Neural Architecture (200-250 words):
   a) Describe the key components of your quantum-enhanced neural network.
   b) Explain how it incorporates the specified quantum property into the given neural process.
   c) Discuss how this integration might differ from classical neural network architectures.
   d) Provide a simple diagram or schematic representation of your quantum-neural architecture.

2. Quantum Mechanism (150-200 words):
   a) Provide a detailed explanation of how the quantum property manifests in your neural network.
   b) Include at least one equation or formal representation of the quantum mechanism.
   c) Discuss any assumptions or simplifications in your model.

3. Cognitive Implications (200-250 words):
   a) Analyze how your quantum-enhanced neural network might affect the specified cognitive function.
   b) Propose at least two testable hypotheses about the cognitive effects of your system.
   c) Discuss how these effects might be measured or observed in a theoretical experiment.
   d) Provide a specific example or scenario that illustrates the potential cognitive impact.

4. Comparative Analysis (150-200 words):
   a) Compare your quantum-enhanced model to classical models of the same cognitive function.
   b) Discuss potential advantages and limitations of your approach.
   c) Address any contradictions or alignments with current neuroscientific understanding.

5. Ethical and Philosophical Considerations (150-200 words):
   a) Discuss the ethical implications of developing and using such quantum-enhanced neural systems.
   b) Explore how this technology might impact our understanding of consciousness or free will.
   c) Propose guidelines for responsible research and development in this field.

6. Future Research Directions (100-150 words):
   a) Suggest two potential research projects that could further explore or validate your model.
   b) Briefly describe the methodology and expected outcomes of these projects.

Ensure your response demonstrates a deep understanding of both quantum mechanics and neuroscience. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section. Your total response should be between 1000-1300 words, not including the diagram.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and neuroscience, particularly in relation to the specified quantum property, neural process, and cognitive function.",
            "The quantum-neural architecture is well-designed and clearly incorporates the specified quantum property into the given neural process, including a diagram or schematic representation.",
            "The quantum mechanism is explained in detail, including at least one equation or formal representation.",
            "The cognitive implications are thoroughly analyzed, with at least two testable hypotheses proposed and a specific example or scenario provided.",
            "The comparative analysis provides a thoughtful comparison between the quantum-enhanced model and classical models.",
            "Ethical and philosophical considerations are discussed in depth, including impacts on understanding of consciousness or free will.",
            "Future research directions are proposed with clear methodologies and expected outcomes.",
            "The response is creative while maintaining scientific plausibility.",
            "The response follows the specified format with clear headings for each section.",
            "The response demonstrates interdisciplinary knowledge application, creative problem-solving, scientific reasoning, and speculative technology design.",
            "The total word count is between 1000-1300 words, not including the diagram."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
