import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            {
                "process": "Decision Making",
                "description": "The cognitive process of selecting a logical choice from available options",
                "quantum_concept": "Quantum superposition",
                "classical_approach": "Bayesian decision theory"
            },
            {
                "process": "Memory Formation",
                "description": "The cognitive process of encoding, storing, and retrieving information",
                "quantum_concept": "Quantum entanglement",
                "classical_approach": "Neural network models"
            }
        ]
        return {
            "1": random.choice(cognitive_processes),
            "2": random.choice(cognitive_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing architecture for modeling the cognitive process of {t['process']}. Your response should adhere to the following structure and guidelines:

1. Quantum Architecture Design (350-400 words):
   a) Describe the key components of your quantum cognitive architecture.
   b) Explain how quantum principles, particularly {t['quantum_concept']}, are utilized to model {t['process']}.
   c) Detail how your architecture integrates classical and quantum computing elements.
   d) Include a high-level diagram or pseudocode illustrating a core aspect of your architecture (describe it textually).

2. Quantum-Cognitive Mapping (300-350 words):
   a) Explain how you map {t['process']} onto quantum states and operations.
   b) Describe any novel quantum algorithms or protocols developed for this cognitive process.
   c) Discuss how quantum phenomena (e.g., superposition, entanglement) are leveraged in your model.
   d) Provide a specific example of how your architecture would handle a simple {t['process']} task.

3. Comparative Analysis (250-300 words):
   a) Compare your quantum cognitive architecture to the classical approach of {t['classical_approach']} for modeling {t['process']}.
   b) Analyze at least three potential advantages and two limitations of your quantum approach.
   c) Discuss how your architecture might provide new insights into human cognition.

4. Implementation Challenges (200-250 words):
   a) Identify at least three key technical challenges in implementing your quantum cognitive architecture.
   b) Propose potential solutions or areas for future research to address these challenges.
   c) Discuss any ethical considerations related to quantum modeling of cognitive processes.

5. Experimental Design (300-350 words):
   Propose two experiments to test the efficacy and potential advantages of your quantum cognitive architecture:
   a) Experiment 1: Design an experiment to compare the performance of your quantum architecture against {t['classical_approach']} for {t['process']}.
      - Describe the experimental setup, methodology, and expected results.
   b) Experiment 2: Design an experiment to test a unique feature or prediction of your quantum cognitive model.
      - Describe the experimental setup, methodology, and expected results.

Ensure your response demonstrates a deep understanding of both quantum computing and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1650 words. Each section should adhere to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both quantum computing (particularly {t['quantum_concept']}) and cognitive science principles related to {t['process']}.",
            "The proposed quantum cognitive architecture is innovative, scientifically plausible, and clearly described with all key components explained.",
            f"The quantum-cognitive mapping is clearly explained, leverages quantum phenomena appropriately, and includes a specific example for {t['process']}.",
            f"The comparative analysis provides at least three insightful advantages and two limitations of the quantum approach compared to {t['classical_approach']}.",
            "The implementation challenges section identifies at least three key technical challenges and proposes potential solutions or research directions.",
            "The experimental designs are well-thought-out, appropriate for testing the architecture's efficacy, and include clear methodologies and expected results.",
            "The response adheres to the specified structure and word count guidelines for each section.",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
