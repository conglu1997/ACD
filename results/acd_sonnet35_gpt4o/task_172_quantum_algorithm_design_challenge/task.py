import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem": "graph coloring",
                "description": "Assign colors to vertices of a graph such that no two adjacent vertices share the same color",
                "classical_algorithm": "Greedy coloring algorithm"
            },
            {
                "problem": "protein folding prediction",
                "description": "Predict the three-dimensional structure of a protein given its amino acid sequence",
                "classical_algorithm": "Molecular dynamics simulation"
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(problems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm to solve the {t['problem']} problem. Before starting, here's a brief primer on quantum computing:

Quantum computing leverages quantum mechanical phenomena such as superposition (the ability of a quantum system to be in multiple states simultaneously) and entanglement (the correlation between quantum particles) to perform computations. Quantum bits (qubits) are the basic unit of information in quantum computing, analogous to classical bits.

Your task is to:

1. Quantum Algorithm Design (250-300 words):
   - Describe your proposed quantum algorithm for solving the {t['problem']} problem.
   - Explain the key quantum principles or phenomena your algorithm leverages (e.g., superposition, entanglement, quantum Fourier transform).
   - Outline the main steps of your algorithm, including initialization, quantum operations, and measurement.
   - Discuss any quantum gates or subroutines that are crucial to your algorithm's functioning.
   - Provide a simple pseudocode or circuit diagram of your proposed quantum algorithm.

2. Complexity Analysis (150-200 words):
   - Analyze the time and space complexity of your quantum algorithm.
   - Compare its theoretical performance to the classical {t['classical_algorithm']}.
   - Identify the specific instances or conditions where your quantum algorithm would outperform classical methods.

3. Implementation Considerations (150-200 words):
   - Discuss the challenges in implementing your algorithm on current or near-term quantum hardware.
   - Propose methods to mitigate errors or decoherence effects in your algorithm.
   - Suggest a hybrid quantum-classical approach if applicable.

4. Broader Implications (150-200 words):
   - Explain how your algorithm contributes to the field of quantum computing.
   - Discuss potential applications of your algorithm beyond the specific {t['problem']} problem.
   - Speculate on how advances in quantum hardware might impact the viability and performance of your algorithm in the future.

5. Limitations and Future Work (100-150 words):
   - Identify any limitations or potential drawbacks of your proposed quantum algorithm.
   - Suggest directions for future research to improve or extend your algorithm.

Ensure your response is well-structured, using clear headings for each section. Your algorithm should be original and demonstrate a deep understanding of both quantum computing principles and the specific problem domain. Use appropriate technical terminology and provide clear explanations of quantum concepts for a knowledgeable audience."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Quantum Algorithm Design section must propose a novel and plausible quantum approach to the {t['problem']} problem.",
            "The algorithm description should correctly use quantum computing concepts and terminology.",
            "A simple pseudocode or circuit diagram of the proposed quantum algorithm must be included.",
            "The Complexity Analysis must provide a clear comparison between the proposed quantum algorithm and the classical approach.",
            "The Implementation Considerations section should address realistic challenges in quantum computing.",
            "The Broader Implications section must discuss potential applications beyond the given problem.",
            "The response should demonstrate a high level of interdisciplinary knowledge in quantum computing, computer science, and the problem domain."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
