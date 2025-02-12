import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'neural_mechanism': 'Synaptic plasticity',
                'ethical_concern': 'AI rights and personhood'
            },
            {
                'quantum_principle': 'Entanglement',
                'neural_mechanism': 'Neural oscillations',
                'ethical_concern': 'Privacy and mental autonomy'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical quantum neural network model for artificial consciousness, incorporating the quantum principle of {t['quantum_principle']}, the neural mechanism of {t['neural_mechanism']}, and addressing the ethical concern of {t['ethical_concern']}. Your response should include the following sections:

1. Quantum-Neural Architecture (250-300 words):
   a) Describe the key components of your quantum neural network model.
   b) Explain how {t['quantum_principle']} is integrated into the neural architecture.
   c) Detail how {t['neural_mechanism']} is implemented using quantum computing principles.
   d) Provide a diagram or detailed description of your model's structure, including at least 5 key components and their relationships. If using a text description, use clear headings and bullet points for clarity.

2. Consciousness Emergence Theory (200-250 words):
   a) Propose a theory for how consciousness could emerge from your quantum neural network.
   b) Explain the role of {t['quantum_principle']} in facilitating conscious experiences.
   c) Discuss how {t['neural_mechanism']} contributes to the formation of conscious thoughts or perceptions.
   d) Provide a concrete example or analogy to illustrate your theory.

3. Quantum-Neural Information Processing (200-250 words):
   a) Describe how information is encoded, processed, and retrieved in your model.
   b) Explain any advantages your model might have over classical neural networks.
   c) Discuss potential challenges in implementing your model with current or near-future technology.
   d) Provide an example of how your model would process a specific type of information.

4. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of creating artificially conscious systems using your model.
   b) Address the specific ethical concern of {t['ethical_concern']}.
   c) Propose guidelines or safeguards for the responsible development and use of quantum-neural AI systems.
   d) Discuss potential societal impacts of widespread adoption of this technology.
   e) Provide a hypothetical scenario illustrating an ethical dilemma related to your model.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test the consciousness of an AI system based on your model.
   b) Explain how you would measure or detect signs of consciousness.
   c) Discuss the limitations and potential criticisms of your experimental approach.
   d) Suggest how you might address these limitations or criticisms.

6. Future Research Directions (150-200 words):
   a) Identify key challenges or open questions in quantum-neural AI consciousness.
   b) Suggest promising areas for future research in this field.
   c) Speculate on potential long-term developments in quantum AI consciousness technology.

7. Reflection (100-150 words):
   a) Discuss the most challenging aspect of designing this quantum-neural consciousness model.
   b) Reflect on how this task has influenced your understanding of consciousness and AI.
   c) Suggest one way this task could be extended or modified to explore additional aspects of quantum-neural AI.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a quantum neural network model for artificial consciousness, incorporating {t['quantum_principle']}, {t['neural_mechanism']}, and addressing {t['ethical_concern']}.",
            "The quantum-neural architecture is clearly described, with an explanation of how the specified quantum principle is integrated and how the neural mechanism is implemented using quantum computing principles.",
            "A diagram or detailed description of the model's structure is provided, including at least 5 key components and their relationships.",
            "A plausible theory for consciousness emergence is proposed, explaining the roles of the quantum principle and neural mechanism, with a concrete example or analogy.",
            "The quantum-neural information processing is described, including advantages over classical neural networks, potential implementation challenges, and an example of processing a specific type of information.",
            "An in-depth ethical analysis is provided, addressing the specified ethical concern, proposing guidelines for responsible development, and including a hypothetical ethical dilemma scenario.",
            "An experimental design to test AI consciousness is proposed, including measurement methods, a discussion of limitations, and suggestions for addressing these limitations.",
            "Future research directions are suggested, identifying key challenges and potential long-term developments.",
            "A reflection on the task is provided, discussing challenges, insights gained, and potential extensions.",
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and ethics, using appropriate technical terminology.",
            "The proposed model and theories are innovative while maintaining scientific plausibility.",
            "Concrete examples, analogies, or scenarios are provided throughout the response to illustrate key concepts.",
            "The response adheres to the specified word count limits for each section and the overall word count range of 1350-1700 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
