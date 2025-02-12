import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                'problem': 'Graph Isomorphism',
                'quantum_paradigm': 'Adiabatic Quantum Computing',
                'qubit_type': 'Superconducting qubits'
            },
            {
                'problem': 'Protein Folding Simulation',
                'quantum_paradigm': 'Quantum Annealing',
                'qubit_type': 'Trapped ion qubits'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(problems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a novel quantum algorithm for the {t['problem']} problem using the {t['quantum_paradigm']} paradigm, then propose a physical implementation using {t['qubit_type']}. Your response should include:

1. Algorithm Design (300-350 words):
   a) Describe your novel quantum algorithm for solving the {t['problem']} problem.
   b) Explain how your algorithm leverages quantum principles to achieve a potential speedup over classical algorithms.
   c) Provide a high-level pseudocode or quantum circuit diagram of your algorithm.
   d) Discuss the expected computational complexity and how it compares to the best known classical algorithm.

2. Quantum Mechanical Analysis (250-300 words):
   a) Explain the key quantum mechanical principles utilized in your algorithm.
   b) Describe how the {t['quantum_paradigm']} paradigm is specifically applied in your approach.
   c) Discuss any quantum phenomena (e.g., superposition, entanglement) that play a crucial role in your algorithm.

3. Algorithm Simulation (200-250 words):
   a) Describe how you would simulate your algorithm on a classical computer.
   b) Discuss the challenges in simulating your quantum algorithm and how you would address them.
   c) Propose a method to verify the correctness of your algorithm through simulation.

4. Physical Implementation (250-300 words):
   a) Describe how your algorithm could be implemented using {t['qubit_type']}.
   b) Discuss the specific challenges of using this qubit type and how your implementation addresses them.
   c) Explain any required quantum gates or operations and how they would be realized in this physical system.
   d) Address the scalability of your implementation as the problem size increases.

5. Error Analysis and Mitigation (200-250 words):
   a) Discuss potential sources of errors in your quantum algorithm and its physical implementation.
   b) Propose error mitigation techniques specific to your algorithm and the chosen qubit type.
   c) Analyze the trade-offs between algorithm performance and error rates.

6. Comparative Analysis (150-200 words):
   a) Compare your approach to existing quantum or classical algorithms for the {t['problem']} problem.
   b) Discuss the potential advantages and limitations of your algorithm.
   c) Suggest possible improvements or variations of your algorithm.

Ensure your response demonstrates a deep understanding of quantum computing principles, algorithm design, and the specific problem domain. Be innovative in your approach while maintaining scientific accuracy. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately applies principles of {t['quantum_paradigm']} to the {t['problem']} problem.",
            f"The physical implementation using {t['qubit_type']} is plausible and well-explained.",
            "The algorithm design is novel and leverages quantum principles effectively.",
            "The analysis of computational complexity and comparison to classical algorithms is sound.",
            "The error analysis and mitigation strategies are appropriate and well-reasoned.",
            "All sections (Algorithm Design, Quantum Mechanical Analysis, Algorithm Simulation, Physical Implementation, Error Analysis and Mitigation, and Comparative Analysis) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
