import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_algorithms = [
            {
                "name": "Shor's Algorithm",
                "description": "A quantum algorithm for integer factorization",
                "application_field": "Cryptography"
            },
            {
                "name": "Grover's Algorithm",
                "description": "A quantum algorithm for unstructured search",
                "application_field": "Drug Discovery"
            }
        ]
        return {
            "1": quantum_algorithms[0],
            "2": quantum_algorithms[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Quantum computing is revolutionizing various fields of science and technology. Your task is to demonstrate your understanding of quantum algorithms and their potential applications.

Explain the quantum algorithm '{t['name']}' ({t['description']}) and propose a novel application in the field of {t['application_field']}. Your response should include:

1. Simple Explanation (150-200 words):
   Explain the key concepts and workings of the quantum algorithm in terms that a high school student could understand. Use analogies or real-world examples to illustrate the main ideas.

2. Quantum Advantage (100-150 words):
   Describe how this quantum algorithm provides an advantage over classical algorithms. Quantify the improvement if possible (e.g., in terms of speed or efficiency).

3. Novel Application (200-250 words):
   Propose an innovative application of this quantum algorithm in the field of {t['application_field']}. Your proposal should:
   a) Describe a specific problem or challenge in the field that the algorithm could address.
   b) Explain how the algorithm would be applied to solve this problem.
   c) Discuss the potential impact and benefits of using this quantum approach.

4. Implementation Challenges (100-150 words):
   Identify and briefly discuss two potential challenges in implementing your proposed application, considering current limitations in quantum computing technology.

Ensure your explanation is clear, accurate, and demonstrates a deep understanding of both the quantum algorithm and the application field. Be creative in your proposed application while maintaining scientific and technological plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation of {t['name']} is accurate and easily understandable by a high school student.",
            "The quantum advantage is clearly explained and quantified if possible.",
            f"The proposed application in {t['application_field']} is novel, feasible, and well-explained.",
            "The implementation challenges identified are relevant and well-reasoned.",
            "The response demonstrates a deep understanding of both quantum computing and the application field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
