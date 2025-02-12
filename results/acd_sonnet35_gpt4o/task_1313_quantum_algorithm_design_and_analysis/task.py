import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        classical_problems = [
            {
                'problem': 'Graph Coloring',
                'description': 'Assign colors to vertices of a graph such that no two adjacent vertices share the same color.',
                'application': 'Network optimization'
            },
            {
                'problem': 'Protein Folding',
                'description': 'Predict the three-dimensional structure of a protein from its amino acid sequence.',
                'application': 'Drug discovery'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(classical_problems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm to solve the classical problem of {t['problem']}. Your response should include the following sections:

1. Problem Analysis (150-200 words):
   a) Briefly explain the {t['problem']} problem and its significance in {t['application']}.
   b) Discuss why this problem is challenging for classical computers.

2. Quantum Algorithm Design (300-350 words):
   a) Describe your proposed quantum algorithm to solve the {t['problem']} problem.
   b) Explain the key quantum mechanics principles your algorithm leverages (e.g., superposition, entanglement, quantum interference).
   c) Provide a high-level pseudocode or step-by-step description of your algorithm.

3. Quantum Circuit Representation (200-250 words):
   a) Describe how your algorithm would be implemented on a quantum circuit.
   b) Explain the types and approximate number of qubits and quantum gates required.
   c) Discuss any error correction or mitigation strategies necessary for your algorithm.
   d) If needed, use ASCII art or text-based diagrams to illustrate your circuit design.

4. Algorithm Analysis (250-300 words):
   a) Analyze the time and space complexity of your quantum algorithm.
   b) Compare its performance to the best known classical algorithms for this problem.
   c) Discuss any limitations or constraints of your approach.

5. Potential Impact (200-250 words):
   a) Explain how your algorithm could advance the field of {t['application']}.
   b) Discuss potential applications of your algorithm in other domains.
   c) Analyze any ethical considerations or potential negative consequences of your algorithm.

6. Future Research Directions (150-200 words):
   a) Propose at least two ways your algorithm could be improved or extended.
   b) Suggest experiments that could be conducted to validate your algorithm's performance.

Ensure your response demonstrates a deep understanding of both quantum computing principles and the chosen classical problem. Use appropriate technical terminology, but provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words, not including the headings.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and the chosen classical problem.",
            "The proposed quantum algorithm is novel, well-explained, and plausibly addresses the given problem.",
            "The quantum circuit representation is coherent and aligns with the proposed algorithm.",
            "The algorithm analysis provides a meaningful comparison to classical approaches.",
            "The potential impact and future research directions are thoughtfully considered and well-reasoned.",
            "The response is well-structured, clear, and uses appropriate technical terminology.",
            "The response adheres to the specified word limit and format guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
