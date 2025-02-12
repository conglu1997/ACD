import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "supply chain management",
                "optimization_problem": "multi-echelon inventory optimization",
                "quantum_principle": "quantum annealing"
            },
            {
                "domain": "financial portfolio management",
                "optimization_problem": "risk-return optimization",
                "quantum_principle": "quantum approximate optimization algorithm (QAOA)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm to solve the complex optimization problem of {t['optimization_problem']} in the domain of {t['domain']}, utilizing the quantum principle of {t['quantum_principle']}. Your response should include:

1. Problem Formulation (200-250 words):
   a) Describe the {t['optimization_problem']} problem in the context of {t['domain']}.
   b) Explain why this problem is challenging for classical algorithms.
   c) Identify the key variables and constraints in the optimization problem.

2. Quantum Algorithm Design (300-350 words):
   a) Outline your quantum algorithm for solving the optimization problem.
   b) Explain how your algorithm utilizes {t['quantum_principle']}.
   c) Describe the quantum circuit or system required for your algorithm.
   d) Discuss how your algorithm achieves a potential quantum advantage.

3. Implementation and Resource Analysis (200-250 words):
   a) Estimate the quantum resources (e.g., qubits, gates) required for your algorithm.
   b) Discuss the scalability of your algorithm for large-scale problems.
   c) Analyze potential error sources and mitigation strategies.

4. Performance Comparison (200-250 words):
   a) Compare the expected performance of your quantum algorithm to classical alternatives.
   b) Provide a theoretical analysis of the speedup or improvement offered by your approach.
   c) Discuss any trade-offs or limitations of your quantum algorithm.

5. Practical Implications (150-200 words):
   a) Explain how your algorithm could impact the field of {t['domain']}.
   b) Discuss potential challenges in adopting this quantum solution in real-world scenarios.
   c) Propose next steps for validating and implementing your algorithm.

6. Interdisciplinary Connections (150-200 words):
   a) Explore how your approach might be adapted to other domains or optimization problems.
   b) Discuss potential collaborations between quantum computing experts and domain specialists.
   c) Suggest future research directions inspired by your algorithm.

Ensure your response demonstrates a deep understanding of quantum computing principles, optimization techniques, and the specific domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical feasibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and its application to {t['optimization_problem']}.",
            f"The quantum algorithm design is innovative and properly utilizes quantum principles to solve the {t['optimization_problem']} in {t['domain']}.",
            "The analysis of implementation challenges, resource requirements, and performance comparison is thorough and realistic.",
            "The response shows interdisciplinary knowledge integration and proposes practical next steps for validation and implementation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
