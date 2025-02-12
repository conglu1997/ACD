import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Quantum coherence",
                "biological_process": "Photosynthesis",
                "evolutionary_mechanism": "Natural selection",
                "information_theory_concept": "Channel capacity"
            },
            {
                "quantum_principle": "Quantum entanglement",
                "biological_process": "Enzyme catalysis",
                "evolutionary_mechanism": "Genetic drift",
                "information_theory_concept": "Mutual information"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel computational paradigm that integrates principles from quantum biology, information theory, and evolutionary computation. Your paradigm should incorporate the following elements:

1. Quantum Principle: {t['quantum_principle']}
2. Biological Process: {t['biological_process']}
3. Evolutionary Mechanism: {t['evolutionary_mechanism']}
4. Information Theory Concept: {t['information_theory_concept']}

Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain how your computational paradigm integrates the specified elements.
   b) Describe the key principles and mechanisms of your proposed system.
   c) Discuss how this integration creates a novel approach to computation.

2. System Architecture (300-350 words):
   a) Detail the components and structure of your computational system.
   b) Explain how each specified element is implemented in the architecture.
   c) Describe the information flow and processing within your system.
   d) Include a high-level diagram or pseudocode to illustrate your architecture (describe it textually).

3. Computational Capabilities (250-300 words):
   a) Analyze the unique computational properties of your paradigm.
   b) Compare its potential capabilities to classical and quantum computing systems.
   c) Propose a specific computational problem that your system might be particularly well-suited to solve.

4. Theoretical Implications (200-250 words):
   a) Discuss the theoretical implications of your paradigm for our understanding of computation, biology, and quantum mechanics.
   b) Propose a novel hypothesis about the nature of information processing in biological systems based on your paradigm.
   c) Suggest an experiment that could test this hypothesis.

5. Practical Applications (200-250 words):
   a) Propose two potential real-world applications of your computational paradigm.
   b) Explain how these applications leverage the unique features of your system.
   c) Discuss any potential societal or ethical implications of these applications.

6. Challenges and Future Directions (150-200 words):
   a) Identify major challenges in realizing your proposed computational paradigm.
   b) Suggest approaches to overcome these challenges.
   c) Propose two directions for future research that could extend or improve your paradigm.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, information theory, and evolutionary computation. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates {t['quantum_principle']}, {t['biological_process']}, {t['evolutionary_mechanism']}, and {t['information_theory_concept']} into a novel computational paradigm.",
            "The proposed system demonstrates a deep understanding of quantum mechanics, biology, information theory, and evolutionary computation.",
            "The computational paradigm is innovative while maintaining scientific plausibility.",
            "The response includes a clear and logical system architecture with well-explained components and information flow.",
            "The analysis of computational capabilities and comparison to existing systems is thorough and insightful.",
            "The theoretical implications and proposed hypothesis show creative scientific reasoning.",
            "The practical applications are well-thought-out and leverage the unique features of the system.",
            "Challenges and future directions are realistically assessed and addressed.",
            "The response maintains coherence and logical consistency across all sections.",
            "The proposed computational paradigm offers a significant advancement over existing quantum computing approaches."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
