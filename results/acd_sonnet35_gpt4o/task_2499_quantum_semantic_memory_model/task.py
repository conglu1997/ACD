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
        cognitive_processes = [
            "semantic clustering",
            "spreading activation",
            "contextual priming",
            "conceptual blending"
        ]
        nlp_techniques = [
            "transformer architecture",
            "word embeddings",
            "attention mechanisms",
            "recurrent neural networks"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "nlp_technique": random.choice(nlp_techniques)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "nlp_technique": random.choice(nlp_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model that simulates human semantic memory formation and retrieval, integrating principles from quantum computing, natural language processing, and cognitive neuroscience. Your model should specifically incorporate the quantum principle of {t['quantum_principle']}, focus on the cognitive process of {t['cognitive_process']}, and utilize the NLP technique of {t['nlp_technique']}.

Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain how the specified quantum principle can be applied to model semantic memory.
   b) Describe how the chosen cognitive process is represented in your model.
   c) Discuss how the NLP technique is integrated with quantum-inspired elements.
   d) Propose a novel feature that enhances your model's ability to simulate human-like semantic processing.

2. Model Architecture (300-350 words):
   a) Design a detailed architecture for your quantum-inspired language model.
   b) Explain the key components and their interactions within the model.
   c) Describe how semantic information is encoded, stored, and retrieved in your model.
   d) Include a simple ASCII art diagram illustrating the main features of your architecture.

3. Learning and Adaptation (200-250 words):
   a) Propose a method for training your model on semantic information.
   b) Explain how your model adapts to new information and updates its semantic representations.
   c) Discuss any challenges in training and how to address them.

4. Simulating Cognitive Phenomena (250-300 words):
   a) Describe how your model simulates at least two specific cognitive phenomena related to semantic memory (e.g., semantic priming, false memories, tip-of-the-tongue states).
   b) Explain how these simulations leverage the quantum-inspired aspects of your model.
   c) Propose an experiment to test your model's performance in replicating human semantic memory behaviors.

5. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired model to traditional language models in terms of semantic processing capabilities.
   b) Discuss potential advantages and limitations of your approach.
   c) Propose metrics to evaluate your model's performance in semantic memory tasks.

6. Ethical Implications and Future Directions (150-200 words):
   a) Discuss ethical considerations in developing models that simulate human cognitive processes.
   b) Propose two potential applications of your model in cognitive science or AI research.
   c) Suggest future research directions to further develop quantum-inspired approaches in language modeling and cognitive simulation.

Ensure your response demonstrates a deep understanding of quantum computing principles, natural language processing techniques, and theories of cognitive neuroscience, particularly related to semantic memory. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed design of a quantum-inspired language model that incorporates {t['quantum_principle']} to simulate semantic memory, focusing on {t['cognitive_process']} and utilizing {t['nlp_technique']}.",
            "The model should demonstrate a novel integration of quantum computing principles, NLP techniques, and cognitive neuroscience theories.",
            "The response should showcase creative problem-solving in designing the model architecture and simulating cognitive phenomena.",
            "The proposed model should be scientifically plausible and demonstrate a deep understanding of the relevant fields.",
            "The response should include a comparative analysis, ethical considerations, and future research directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
