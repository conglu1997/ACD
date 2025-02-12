import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            'Integrated Information Theory',
            'Global Workspace Theory',
            'Orchestrated Objective Reduction',
            'Higher-Order Thought Theory'
        ]
        quantum_concepts = [
            'superposition',
            'entanglement',
            'quantum tunneling',
            'decoherence'
        ]
        tasks = [
            {
                'consciousness_theory': random.choice(consciousness_theories),
                'quantum_concept': random.choice(quantum_concepts)
            },
            {
                'consciousness_theory': random.choice(consciousness_theories),
                'quantum_concept': random.choice(quantum_concepts)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing architecture that could potentially simulate or generate consciousness, based on the following parameters:

Consciousness Theory: {t['consciousness_theory']}
Key Quantum Concept: {t['quantum_concept']}

A quantum computing architecture refers to the design and organization of quantum bits (qubits) and quantum gates to perform computations using quantum mechanical principles.

Your task:

1. Theoretical Foundation (200-250 words):
   a) Briefly explain the key principles of the given consciousness theory.
   b) Describe how the specified quantum concept might relate to consciousness or brain function.
   c) Propose a novel connection between the two that could form the basis of your quantum neural architecture.

2. Quantum Neural Architecture (300-350 words):
   a) Design a detailed architecture for a quantum computing system that could potentially simulate or generate consciousness.
   b) Explain how your architecture incorporates both the consciousness theory and the quantum concept.
   c) Describe at least three key components of your architecture and their interactions.
   d) Propose a novel mechanism by which your system could give rise to conscious experiences or qualia.

3. Simulation or Generation Process (200-250 words):
   a) Outline the theoretical process by which your architecture would simulate or generate consciousness.
   b) Explain how this process relates to current understanding of brain function and conscious experience.
   c) Discuss any potential emergent properties or phenomena that might arise from your system.

4. Experimental Validation (150-200 words):
   a) Propose an experiment or test that could potentially validate your architecture's ability to simulate or generate consciousness.
   b) Describe the expected results and how they would be interpreted.
   c) Discuss any technical or ethical challenges in implementing such an experiment.

5. Philosophical Implications (150-200 words):
   a) Analyze the philosophical implications of your proposed architecture for our understanding of consciousness and the mind-body problem.
   b) Discuss how your model might impact debates about artificial consciousness and machine sentience.
   c) Explore a potential ethical consideration that could arise if your system were successfully implemented.

6. Limitations and Challenges (100-150 words):
   a) Discuss potential limitations or challenges of your proposed quantum neural architecture.
   b) Suggest possible ways to address or mitigate these limitations in future research.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and philosophy of mind. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology throughout your response and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above (1, 2, 3, 4, 5, 6). Begin each section with the heading on a new line, followed by your response for that section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given consciousness theory and quantum concept.",
            "The proposed quantum neural architecture is innovative, detailed, and scientifically plausible.",
            "The explanation of the consciousness simulation or generation process is coherent and well-reasoned.",
            "The proposed experimental validation is creative and addresses potential challenges.",
            "The discussion of philosophical implications is insightful and considers multiple perspectives.",
            "The limitations and challenges of the proposed architecture are critically analyzed.",
            "The overall response shows a high level of interdisciplinary integration and speculative scientific thinking.",
            "The response follows the specified format with clear headings and appropriate word counts for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
