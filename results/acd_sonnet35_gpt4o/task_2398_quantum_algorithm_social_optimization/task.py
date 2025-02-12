import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_problems = [
            {
                "problem": "Urban Traffic Congestion",
                "quantum_concept": "Quantum Annealing",
                "concept_description": "A quantum-mechanical method to find the global minimum of a given objective function over a given set of candidate solutions.",
                "societal_domain": "Transportation and Urban Planning"
            },
            {
                "problem": "Wealth Inequality",
                "quantum_concept": "Quantum Fourier Transform",
                "concept_description": "A linear transformation on qubits, which is the quantum analogue of the discrete Fourier transform.",
                "societal_domain": "Economic Policy"
            },
            {
                "problem": "Fake News Propagation",
                "quantum_concept": "Quantum Walk Algorithms",
                "concept_description": "Quantum analogues of classical random walks, which can provide quadratic speedups for many problems.",
                "societal_domain": "Information and Media"
            },
            {
                "problem": "Healthcare Resource Allocation",
                "quantum_concept": "Quantum Approximate Optimization Algorithm (QAOA)",
                "concept_description": "A hybrid quantum-classical algorithm for finding approximate solutions to combinatorial optimization problems.",
                "societal_domain": "Public Health"
            }
        ]
        return {
            "1": random.choice(social_problems),
            "2": random.choice(social_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm to address the social problem of {t['problem']} using the quantum concept of {t['quantum_concept']}, then analyze its potential societal impacts in the domain of {t['societal_domain']}. 

Brief explanation of {t['quantum_concept']}: {t['concept_description']}

Your response should include the following sections:

1. Problem Analysis (200-250 words):
   a) Describe the key aspects and challenges of the {t['problem']} problem.
   b) Explain why traditional classical algorithms might be insufficient for solving this problem.
   c) Identify the specific optimization or decision-making aspects that could benefit from a quantum approach.

2. Quantum Algorithm Design (300-350 words):
   a) Outline your quantum algorithm using {t['quantum_concept']} to address the {t['problem']} problem.
   b) Explain how your algorithm leverages quantum principles to outperform classical alternatives.
   c) Describe the input, quantum operations, and measurement processes of your algorithm.
   d) Discuss any potential limitations or assumptions of your quantum approach.
   e) Provide a simple pseudocode or diagram of your quantum algorithm.

3. Implementation Considerations (200-250 words):
   a) Describe the quantum hardware requirements for your algorithm.
   b) Discuss any classical pre-processing or post-processing steps needed.
   c) Analyze the scalability of your algorithm for real-world applications.
   d) Propose a hybrid quantum-classical approach if applicable.

4. Societal Impact Analysis (250-300 words):
   a) Predict the potential positive impacts of implementing your quantum algorithm in the {t['societal_domain']} domain.
   b) Identify possible negative consequences or risks associated with the algorithm's implementation.
   c) Discuss how the algorithm might influence policy-making or public perception in the relevant domain.
   d) Analyze potential ethical considerations related to using quantum computing for this social problem.

5. Future Directions (150-200 words):
   a) Propose two potential improvements or extensions to your quantum algorithm.
   b) Suggest a novel application of your algorithm to a different but related social problem.
   c) Discuss how advancements in quantum hardware might impact the effectiveness of your algorithm.

Ensure your response demonstrates a deep understanding of both quantum computing principles and the social problem being addressed. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and considering real-world implications.

Format your response with clear headings for each section and use subheadings (a, b, c, d, e) as outlined above. Your total response should be between 1100-1350 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['problem']} problem and its challenges.",
            f"The quantum algorithm design effectively utilizes the {t['quantum_concept']} concept to address the problem.",
            "The algorithm's quantum operations and measurement processes are clearly explained.",
            "A simple pseudocode or diagram of the quantum algorithm is provided.",
            "The implementation considerations, including hardware requirements and scalability, are thoroughly discussed.",
            f"The societal impact analysis provides insightful predictions for the {t['societal_domain']} domain.",
            "Ethical considerations and potential risks are thoughtfully addressed.",
            "The proposed future directions and improvements are innovative and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
