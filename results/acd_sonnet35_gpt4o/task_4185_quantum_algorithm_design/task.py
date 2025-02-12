import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "problem_domain": "cryptography",
                "specific_problem": "breaking RSA encryption",
                "quantum_resource": "quantum Fourier transform"
            },
            {
                "problem_domain": "optimization",
                "specific_problem": "solving the traveling salesman problem",
                "quantum_resource": "quantum annealing"
            },
            {
                "problem_domain": "machine learning",
                "specific_problem": "training neural networks",
                "quantum_resource": "quantum variational circuits"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm to address the problem of {t['specific_problem']} in the domain of {t['problem_domain']}, utilizing {t['quantum_resource']} as a key quantum resource. Your response should include the following sections:

1. Problem Analysis (200-250 words):
   a) Describe the chosen problem and its significance in the {t['problem_domain']} domain.
   b) Explain why quantum computing might offer advantages over classical approaches for this problem.
   c) Discuss any existing classical or quantum approaches to this problem.

2. Quantum Algorithm Design (300-350 words):
   a) Provide a high-level description of your quantum algorithm.
   b) Explain how your algorithm utilizes {t['quantum_resource']} and any other quantum computing principles.
   c) Describe the step-by-step process of your algorithm, including initialization, quantum operations, and measurement.
   d) Discuss how your algorithm addresses the specific challenges of {t['specific_problem']}.

3. Complexity Analysis (200-250 words):
   a) Analyze the time and space complexity of your quantum algorithm.
   b) Compare the complexity of your algorithm to the best known classical algorithm for this problem.
   c) Discuss any potential speedups or advantages offered by your quantum approach.

4. Implementation Considerations (200-250 words):
   a) Describe the quantum hardware requirements for implementing your algorithm.
   b) Discuss any challenges in implementing your algorithm on current or near-term quantum devices.
   c) Propose methods to mitigate errors or decoherence effects in your implementation.

5. Potential Impact and Applications (150-200 words):
   a) Discuss the potential impact of your algorithm on the field of {t['problem_domain']}.
   b) Propose at least two other applications or domains where your algorithm or its principles could be applied.
   c) Speculate on how advances in quantum computing might further improve your algorithm in the future.

6. Ethical Considerations (100-150 words):
   a) Discuss any potential ethical implications or concerns related to the application of your quantum algorithm.
   b) Propose guidelines for the responsible development and use of quantum algorithms in {t['problem_domain']}.

Glossary of key terms:
- Qubit: The fundamental unit of quantum information.
- Superposition: The ability of a quantum system to be in multiple states simultaneously.
- Entanglement: A quantum phenomenon where particles become correlated and share properties.
- Quantum gate: A basic quantum circuit operating on a small number of qubits.
- Decoherence: The loss of quantum information due to interaction with the environment.

Ensure your response demonstrates a deep understanding of quantum computing principles, algorithm design, and the specific problem domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific accuracy and plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a solid understanding of basic quantum computing principles and algorithm design.",
            "The proposed quantum algorithm is creative and addresses the given problem in a logical manner.",
            "The complexity analysis and comparison with classical approaches show reasonable reasoning.",
            "The implementation considerations and potential impact are thoughtfully discussed.",
            "The response shows interdisciplinary knowledge integration and problem-solving skills.",
            "The ethical considerations are addressed and relevant to the problem domain."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
