import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            "working memory",
            "attention",
            "decision making",
            "language processing",
            "emotional regulation",
            "spatial reasoning",
            "pattern recognition",
            "social cognition"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing",
            "quantum interference"
        ]
        tasks = [
            {
                'cognitive_function': random.choice(cognitive_functions),
                'quantum_principle': random.choice(quantum_principles),
                'application_domain': random.choice(['education', 'mental health', 'human-computer interaction', 'artificial general intelligence'])
            },
            {
                'cognitive_function': random.choice(cognitive_functions),
                'quantum_principle': random.choice(quantum_principles),
                'application_domain': random.choice(['neurodegenerative diseases', 'cognitive enhancement', 'brain-computer interfaces', 'artificial consciousness'])
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network architecture that mimics the cognitive function of {t['cognitive_function']}, incorporating the quantum principle of {t['quantum_principle']}. Then, analyze its potential for modeling complex human thought processes, with a focus on applications in {t['application_domain']}. Your response should include:

1. Architecture Design (300-350 words):
   a) Describe the key components and structure of your quantum-inspired neural network.
   b) Explain how it incorporates the specified quantum principle.
   c) Detail how the architecture models the given cognitive function.
   d) Discuss any novel features that distinguish it from classical neural networks.

2. Quantum-Cognitive Mapping (200-250 words):
   a) Explain how quantum states or processes in your network correspond to cognitive states or processes.
   b) Provide a specific example of how this mapping works for the given cognitive function.
   c) Discuss potential advantages of this quantum-inspired approach over classical models.

3. Information Processing Mechanism (200-250 words):
   a) Describe how information flows and is processed in your architecture.
   b) Explain how the quantum principle enhances or alters this processing.
   c) Discuss any emergent properties that might arise from this quantum-cognitive integration.

4. Mathematical Framework (150-200 words):
   a) Provide a basic mathematical description of your architecture.
   b) Include at least one equation that integrates quantum and cognitive elements.
   c) Explain the significance of each term in your equation(s).

5. Potential Applications (200-250 words):
   a) Propose three potential applications of your architecture in the specified domain.
   b) Explain how each application leverages the unique features of your quantum-cognitive model.
   c) Discuss potential impacts and benefits of these applications.

6. Limitations and Challenges (150-200 words):
   a) Identify at least three potential limitations or challenges of your architecture.
   b) Discuss any ethical concerns that may arise from its development or application.
   c) Propose potential solutions or areas for future research to address these issues.

7. Experimental Predictions (150-200 words):
   a) Propose two testable predictions that your architecture makes about human cognition.
   b) Describe potential experiments to validate these predictions.
   c) Discuss how these experiments could contribute to our understanding of quantum effects in cognition.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and cognitive psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, neuroscience, and cognitive psychology.",
            "The architecture design is innovative, logically consistent, and effectively incorporates the specified quantum principle and cognitive function.",
            "The quantum-cognitive mapping is well-explained and provides a clear example.",
            "The information processing mechanism is thoroughly described and highlights the benefits of the quantum-inspired approach.",
            "The mathematical framework is sound and integrates quantum and cognitive elements.",
            "Potential applications are relevant to the specified domain and leverage the unique features of the architecture.",
            "Limitations, challenges, and ethical concerns are thoughtfully considered.",
            "Experimental predictions are testable and relevant to understanding quantum effects in cognition.",
            "The response is creative while maintaining scientific plausibility.",
            "All sections are adequately addressed within the specified word count ranges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
