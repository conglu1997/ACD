import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "syntax",
            "semantics",
            "phonology",
            "morphology"
        ]
        cognitive_processes = [
            "memory consolidation",
            "attention allocation",
            "conceptual blending",
            "decision making"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum interference",
            "quantum tunneling"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate and analyze language evolution and cognitive processes. Your system should focus on the linguistic feature of {t['linguistic_feature']}, the cognitive process of {t['cognitive_process']}, and utilize the quantum principle of {t['quantum_principle']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum linguistic evolution simulator.
   b) Explain how it incorporates the specified quantum principle into its design.
   c) Detail how the architecture models the given linguistic feature and cognitive process.
   d) Provide a visual representation or schematic of your system (use ASCII art or Unicode characters).

2. Quantum-Linguistic Integration (200-250 words):
   a) Explain how quantum computations are used to model language evolution.
   b) Describe how the specified linguistic feature is represented in your quantum system.
   c) Discuss any novel approaches to quantum-linguistic modeling in your design.

3. Cognitive Process Simulation (200-250 words):
   a) Detail how your system simulates the specified cognitive process.
   b) Explain how this simulation interacts with the linguistic feature and quantum principle.
   c) Discuss potential insights into cognition that could be gained from this approach.

4. Evolution Dynamics (150-200 words):
   a) Describe how your system models language change over time.
   b) Explain how the quantum principle contributes to simulating evolutionary processes.
   c) Propose a hypothesis about language evolution that could be tested using your system.

5. Experimental Design (150-200 words):
   a) Propose an experiment using your system to investigate a specific aspect of language evolution or cognitive processing.
   b) Describe the variables, methodology, and expected outcomes of your experiment.
   c) Discuss how the results could contribute to our understanding of linguistics or cognitive science.

6. Limitations and Future Directions (100-150 words):
   a) Identify potential limitations or challenges in your quantum linguistic evolution simulator.
   b) Suggest improvements or extensions to address these limitations.
   c) Propose future research directions that could build upon your system.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and cognitive science. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle of {t['quantum_principle']} and how it can be applied to linguistic and cognitive modeling.",
            f"The system effectively integrates the linguistic feature of {t['linguistic_feature']} with quantum computing concepts.",
            f"The simulation of the cognitive process of {t['cognitive_process']} is well-explained and plausibly connected to both linguistic and quantum aspects of the system.",
            "The proposed experiment is well-designed and could potentially yield meaningful insights into language evolution or cognitive processing.",
            "The response shows creativity and innovation in combining quantum computing, linguistics, and cognitive science, while maintaining scientific plausibility.",
            "The limitations and future directions discussed demonstrate a nuanced understanding of the challenges and potential of this interdisciplinary approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
