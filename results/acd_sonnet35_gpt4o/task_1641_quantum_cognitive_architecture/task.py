import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        cognitive_processes = [
            "working memory",
            "long-term memory consolidation",
            "attention",
            "decision-making"
        ]
        learning_paradigms = [
            "reinforcement learning",
            "unsupervised learning",
            "transfer learning",
            "meta-learning"
        ]
        
        tasks = [
            {
                "quantum_concept": random.choice(quantum_concepts),
                "cognitive_process": random.choice(cognitive_processes),
                "learning_paradigm": random.choice(learning_paradigms)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for an AI system that models human {t['cognitive_process']} using the quantum computing principle of {t['quantum_concept']}. Your architecture should also incorporate the learning paradigm of {t['learning_paradigm']}. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain how {t['quantum_concept']} can be used to model {t['cognitive_process']}.
   b) Describe how {t['learning_paradigm']} can be integrated into this quantum-cognitive model.
   c) Discuss the potential advantages of this approach over classical cognitive architectures.

2. Architecture Design (300-350 words):
   a) Provide a high-level overview of your quantum-inspired cognitive architecture.
   b) Explain how {t['quantum_concept']}, {t['cognitive_process']}, and {t['learning_paradigm']} are integrated into the architecture.
   c) Describe the key components and their interactions within the system.
   d) Include a visual representation (ASCII diagram) of your architecture, showing the main components and their relationships. Use at least 10 lines for your ASCII diagram, with appropriate labels and connections.

3. Quantum-Cognitive Processes (250-300 words):
   a) Detail how your architecture would approach a specific cognitive task related to {t['cognitive_process']}.
   b) Explain the role of {t['quantum_concept']} in this task.
   c) Describe how {t['learning_paradigm']} is applied in this context.
   d) Provide a step-by-step example of the system processing information for this task.

4. Mathematical Formalism (200-250 words):
   a) Present a mathematical or formal representation of a key aspect of your quantum-cognitive architecture.
   b) Explain how this formalism captures both the quantum and cognitive aspects of your system.
   c) Discuss how this formalism could be used to make predictions or generate hypotheses about cognitive processes.

5. Empirical Predictions and Validation (200-250 words):
   a) Propose an experiment to test a specific prediction made by your quantum-cognitive model.
   b) Describe how you would measure and analyze the results.
   c) Discuss potential challenges in validating quantum effects in cognitive processes.

6. Ethical Implications and Societal Impact (150-200 words):
   a) Discuss potential ethical concerns related to modeling human cognition using quantum principles.
   b) Address issues of interpretability and explainability in quantum-inspired AI systems.
   c) Speculate on the long-term societal impacts of such technology.

Ensure your response demonstrates a deep understanding of both quantum computing and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section and include the ASCII diagram in the Architecture Design section. Your total response should be between 1350-1650 words, excluding the ASCII diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a quantum-inspired cognitive architecture based on {t['quantum_concept']} and focusing on {t['cognitive_process']}",
            f"The architecture must incorporate {t['learning_paradigm']} as a learning paradigm",
            "The proposed architecture should be scientifically plausible and clearly explained",
            "The response should demonstrate interdisciplinary knowledge integration across quantum computing and cognitive science",
            "The mathematical formalism should accurately represent a key aspect of the quantum-cognitive architecture",
            "The empirical predictions and validation approach should be well-reasoned and feasible",
            "The ethical implications and societal impact should be thoroughly considered",
            "The response should follow the specified format with clear headings for each section",
            "The response should include an ASCII diagram of at least 10 lines with appropriate labels and connections",
            "The response should be within the specified word count range (1350-1650 words, excluding ASCII diagram)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
