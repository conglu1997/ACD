import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum interference"
        ]
        neural_mechanisms = [
            "Hebbian learning",
            "Spike-timing-dependent plasticity",
            "Lateral inhibition",
            "Neuronal oscillations"
        ]
        nlp_tasks = [
            "Sentiment analysis",
            "Machine translation",
            "Text summarization",
            "Question answering"
        ]
        tasks = [
            {
                "quantum_principle": qp,
                "neural_mechanism": nm,
                "nlp_task": nt
            }
            for qp in quantum_principles
            for nm in neural_mechanisms
            for nt in nlp_tasks
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-neural network architecture for natural language processing, incorporating the quantum principle of {t['quantum_principle']}, the neural mechanism of {t['neural_mechanism']}, and focusing on the NLP task of {t['nlp_task']}. Your response should include the following sections, clearly labeled with headings:

1. Quantum-Neural Architecture (300-350 words):
   a) Describe the overall structure of your quantum-neural network.
   b) Explain how you incorporate the specified quantum principle into the neural architecture.
   c) Detail how the neural mechanism is implemented in your quantum-neural system.
   d) Discuss how classical and quantum components interact in your design.
   e) Include a high-level diagram or pseudocode representing your architecture.

2. Natural Language Processing Integration (250-300 words):
   a) Explain how your quantum-neural architecture is specifically adapted for the given NLP task.
   b) Describe the input and output representations for your system.
   c) Discuss any novel language processing capabilities enabled by the quantum-neural integration.

3. Training and Optimization (200-250 words):
   a) Propose a method for training your quantum-neural NLP system.
   b) Explain how quantum principles might enhance or complicate the learning process.
   c) Discuss potential challenges in optimizing such a system and propose solutions.

4. Performance Analysis (200-250 words):
   a) Hypothesize the potential advantages of your quantum-neural approach over classical NLP systems.
   b) Discuss possible limitations or drawbacks of your approach.
   c) Propose metrics to evaluate the performance of your system, considering both quantum and linguistic aspects.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical concerns related to quantum-enhanced NLP systems.
   b) Explore the broader implications of such technology for society and scientific research.
   c) Propose guidelines for responsible development and use of quantum-neural NLP systems.

Ensure your response demonstrates a deep understanding of quantum computing principles, neuroscience, and computational linguistics. Use appropriate technical terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1350 words. Format your response with clear headings for each section as specified above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately incorporates the quantum principle of {t['quantum_principle']} into the neural architecture",
            f"The neural mechanism of {t['neural_mechanism']} is clearly implemented in the quantum-neural system",
            f"The design is specifically adapted for the NLP task of {t['nlp_task']}",
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and computational linguistics",
            "The proposed architecture is innovative while maintaining scientific plausibility",
            "The response addresses all required sections: architecture, NLP integration, training/optimization, performance analysis, and ethical implications",
            "The response includes a high-level diagram or pseudocode representing the architecture",
            "The response is well-structured with clear headings for each section as specified",
            "The response is within the specified word count range of 1100-1350 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
