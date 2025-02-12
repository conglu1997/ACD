class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "urban_problem": "Traffic flow optimization",
                "quantum_algorithm": "Quantum approximate optimization algorithm (QAOA)"
            },
            "2": {
                "urban_problem": "Energy distribution efficiency",
                "quantum_algorithm": "Quantum annealing"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing solution for the urban planning problem of {t['urban_problem']} using the {t['quantum_algorithm']}. 

Quantum computing is a form of computation that harnesses the principles of quantum mechanics, such as superposition and entanglement, to perform certain calculations exponentially faster than classical computers.

Your response should include:

1. Problem Analysis (200-250 words):
   a) Describe the urban planning problem in detail.
   b) Explain why this problem is challenging for classical computing methods.
   c) Identify key variables and constraints in the problem.

2. Quantum Algorithm Design (250-300 words):
   a) Explain the basics of the {t['quantum_algorithm']} and why it's suitable for this problem.
   b) Describe how you would map the urban planning problem onto the quantum algorithm.
   c) Outline the steps of your quantum algorithm, including initialization, quantum operations, and measurement.

3. Implementation Considerations (200-250 words):
   a) Discuss the quantum hardware requirements for your solution.
   b) Explain how you would handle noise and errors in the quantum system.
   c) Describe any classical pre-processing or post-processing steps needed.

4. Performance Analysis (200-250 words):
   a) Estimate the potential speedup or efficiency gain compared to classical methods.
   b) Discuss the scalability of your solution for larger urban areas.
   c) Identify potential limitations or challenges in practical implementation.

5. Urban Planning Impact (150-200 words):
   a) Explain how your quantum solution could transform urban planning practices.
   b) Discuss potential secondary effects on city development and citizen life.
   c) Address any ethical considerations or potential negative consequences.

6. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your quantum urban planning solution.
   b) Propose a related urban planning problem that could benefit from quantum computing.

Ensure your response demonstrates a deep understanding of both quantum computing principles and urban planning challenges. Use technical terminology appropriately and provide clear explanations for non-experts where necessary. Be creative in your approach while maintaining scientific and practical plausibility. Address all sections and stay within the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum algorithm and its application to the given urban planning problem.",
            "The quantum algorithm design is well-explained, logically sound, and appropriately mapped to the urban planning problem.",
            "The implementation considerations show awareness of real-world quantum computing challenges and limitations.",
            "The performance analysis provides reasonable estimates and identifies relevant scalability issues.",
            "The urban planning impact discussion is insightful and considers broader societal implications.",
            "The response is creative yet maintains scientific and practical plausibility throughout.",
            "All required sections are addressed within the specified word limits.",
            "Technical concepts are explained clearly for non-experts while maintaining accuracy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
