import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            {
                'principle': 'superposition',
                'neural_process': 'memory consolidation',
                'interface_type': 'synaptic'
            },
            {
                'principle': 'entanglement',
                'neural_process': 'sensory integration',
                'interface_type': 'dendritic'
            }
        ]
        return {str(i+1): principle for i, principle in enumerate(random.sample(quantum_principles, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum biocomputing system that interfaces directly with neural tissue, focusing on the quantum principle of {t['principle']} and its potential application to the neural process of {t['neural_process']}. Your system should utilize a {t['interface_type']} interface. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum biocomputing system.
   b) Explain how your system incorporates the quantum principle of {t['principle']}.
   c) Detail how the {t['interface_type']} interface interacts with neural tissue.
   d) Discuss how your system models and enhances the {t['neural_process']} process.

2. Quantum-Biological Interface (250-300 words):
   a) Explain the mechanisms by which quantum effects are maintained in a biological environment.
   b) Describe how information is transferred between the quantum and biological components.
   c) Address potential issues of decoherence and propose solutions.

3. Information Processing Capabilities (250-300 words):
   a) Describe the unique information processing capabilities of your system.
   b) Compare its theoretical performance to classical computing and natural neural systems.
   c) Explain how the quantum-biological interface enhances {t['neural_process']}.

4. Experimental Design (300-350 words):
   a) Propose an experiment to test the information processing capabilities of your system.
   b) Describe the methodology, including any novel measurement techniques required.
   c) Predict potential outcomes and their implications.
   d) Discuss ethical considerations and safety protocols for interfacing with neural tissue.

5. Implications and Applications (200-250 words):
   a) Discuss the potential impact of your system on neuroscience and quantum computing.
   b) Propose two potential applications in medicine, AI, or cognitive enhancement.
   c) Address any philosophical implications regarding consciousness or the nature of cognition.

6. Challenges and Future Directions (200-250 words):
   a) Identify key technological or scientific barriers to realizing your system.
   b) Propose approaches to overcome these challenges.
   c) Suggest two directions for future research in quantum biocomputing.

Ensure your response demonstrates a deep understanding of quantum mechanics, neurobiology, and information processing. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum principle of {t['principle']} and its potential application to {t['neural_process']}.",
            f"The proposed {t['interface_type']} interface is described in detail and its interaction with neural tissue is plausibly explained.",
            "The system architecture and quantum-biological interface are innovative yet scientifically grounded.",
            "The experimental design is well-thought-out and addresses potential ethical concerns.",
            "The response shows creative problem-solving and interdisciplinary knowledge integration across quantum physics, neurobiology, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
