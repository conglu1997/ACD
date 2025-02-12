import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling"
        ]
        neural_processes = [
            "synaptic transmission",
            "neural plasticity",
            "pattern recognition"
        ]
        information_concepts = [
            "error correction",
            "data compression",
            "information entropy"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "neural_process": random.choice(neural_processes),
                "information_concept": random.choice(information_concepts)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "neural_process": random.choice(neural_processes),
                "information_concept": random.choice(information_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model for quantum information processing in neural networks, incorporating the following elements:

Quantum Principle: {t['quantum_principle']}
Neural Process: {t['neural_process']}
Information Concept: {t['information_concept']}

Your response should include:

1. Theoretical Framework (300-350 words):
   a) Describe the key components of your quantum neural information processing model.
   b) Explain how you integrate the given quantum principle into neural information processing.
   c) Discuss how your model incorporates the specified neural process.
   d) Elaborate on how the given information concept is applied in your model.

2. Quantum-Neural Interface (250-300 words):
   a) Propose a mechanism for how quantum effects could influence or interact with neural processes at a cellular or subcellular level.
   b) Discuss potential challenges in maintaining quantum coherence in a biological system and how your model addresses them.
   c) Explain how classical neural activity might be transduced into quantum states or vice versa in your model.

3. Information Processing Dynamics (250-300 words):
   a) Describe how information is encoded, processed, and retrieved in your quantum neural network model.
   b) Explain any advantages your model might have over classical neural networks in terms of information processing capabilities.
   c) Discuss how the integration of quantum principles might affect learning, memory, or other cognitive processes.

4. Mathematical Formulation (200-250 words):
   a) Provide a basic mathematical or formal description of your model, using appropriate notation from quantum mechanics and neuroscience.
   b) Explain the key equations or formalisms and how they capture the integration of quantum and neural processes.

5. Experimental Predictions (200-250 words):
   a) Propose two specific, testable predictions that your model makes about neural information processing.
   b) Describe potential experiments or observations that could validate or refute these predictions.
   c) Discuss any technological limitations in testing your model and how they might be overcome.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your model for our understanding of consciousness, cognition, or artificial intelligence.
   b) Propose two potential applications of your quantum neural information processing model in fields such as neurotechnology, quantum computing, or brain-computer interfaces.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and information theory.",
            "The proposed model creatively and plausibly integrates the given quantum principle, neural process, and information concept.",
            "The quantum-neural interface is well-explained and addresses potential challenges.",
            "The mathematical formulation is appropriate and clearly explained.",
            "The experimental predictions are specific, testable, and well-reasoned.",
            "The implications and applications are insightful and demonstrate an understanding of the model's potential impact."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
