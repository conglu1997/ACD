import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        neural_mechanisms = [
            "spike-timing-dependent plasticity",
            "neuromodulation",
            "dendritic computation",
            "neural oscillations"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "neural_mechanism": random.choice(neural_mechanisms)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "neural_mechanism": random.choice(neural_mechanisms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-inspired neural network architecture for AI that incorporates the quantum principle of {t['quantum_principle']} and the neural mechanism of {t['neural_mechanism']}. Then, analyze its potential capabilities and limitations. Your response should include:

1. Architecture Design (300-350 words):
   a) Describe the key components of your quantum-inspired neural network architecture.
   b) Explain how you integrate {t['quantum_principle']} into the neural network structure.
   c) Detail how {t['neural_mechanism']} is implemented in your architecture.
   d) Discuss any novel computational units or processes that emerge from this integration.

2. Theoretical Framework (250-300 words):
   a) Provide a mathematical or formal description of a key process in your architecture.
   b) Explain how this formalism captures both quantum and neural aspects.
   c) Discuss any assumptions or approximations made in your theoretical framework.

3. Potential Capabilities (250-300 words):
   a) Describe three potential advantages of your architecture over classical neural networks.
   b) Explain how these advantages arise from the quantum-neural integration.
   c) Propose a specific AI task or problem where your architecture might excel.

4. Limitations and Challenges (200-250 words):
   a) Identify at least two significant limitations or challenges of your proposed architecture.
   b) Discuss any potential trade-offs between quantum and neural aspects.
   c) Propose potential solutions or research directions to address these limitations.

5. Implementation Considerations (200-250 words):
   a) Describe the hardware requirements for implementing your architecture.
   b) Discuss any software or algorithmic challenges in realizing your design.
   c) Propose a roadmap for developing and testing a prototype of your architecture.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical considerations related to your architecture.
   b) Analyze possible societal impacts if such an AI system were developed.
   c) Propose guidelines for responsible development and use of your architecture.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Include a word count at the end of your response.

Note: You may use hypothetical references or citations to support your ideas, but this is not required. Focus on presenting a coherent and well-reasoned design and analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive design of a quantum-inspired neural network architecture incorporating {t['quantum_principle']} and {t['neural_mechanism']}.",
            "The theoretical framework provides a clear mathematical or formal description of a key process in the architecture.",
            "The analysis of potential capabilities includes three advantages and a specific AI task where the architecture might excel.",
            "At least two significant limitations or challenges are identified and discussed, with proposed solutions or research directions.",
            "Implementation considerations, including hardware requirements and a development roadmap, are thoughtfully discussed.",
            "Ethical and societal implications are analyzed, with proposed guidelines for responsible development and use.",
            "The overall response demonstrates creativity, interdisciplinary knowledge integration, and speculative scientific reasoning within the given word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
