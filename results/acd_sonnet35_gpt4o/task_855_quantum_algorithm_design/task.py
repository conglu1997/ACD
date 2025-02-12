import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem": "Graph Coloring",
                "description": "Assign colors to vertices of a graph such that no two adjacent vertices share the same color",
                "classical_algorithm": "Backtracking"
            },
            {
                "problem": "Integer Factorization",
                "description": "Find the prime factors of a large integer",
                "classical_algorithm": "General Number Field Sieve"
            },
            {
                "problem": "Travelling Salesman Problem",
                "description": "Find the shortest possible route that visits each city exactly once and returns to the origin city",
                "classical_algorithm": "Dynamic Programming"
            },
            {
                "problem": "Database Search",
                "description": "Find a specific item in an unsorted database",
                "classical_algorithm": "Linear Search"
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm to solve the {t['problem']} problem. Your task is to leverage quantum computing principles to potentially outperform classical algorithms for this problem. Provide a detailed response addressing the following points:

1. Problem Analysis (100-150 words):
   a) Briefly explain the {t['problem']} problem and its significance.
   b) Discuss why this problem might be suitable for a quantum approach.

2. Quantum Algorithm Design (250-300 words):
   a) Describe your proposed quantum algorithm in detail.
   b) Explain the quantum principles or phenomena your algorithm exploits (e.g., superposition, entanglement, quantum Fourier transform).
   c) Provide a step-by-step breakdown of how your algorithm works.
   d) Include a high-level pseudocode or quantum circuit diagram for your algorithm.

3. Complexity Analysis (150-200 words):
   a) Analyze the time and space complexity of your quantum algorithm.
   b) Compare its complexity to the classical {t['classical_algorithm']} algorithm for this problem.
   c) Discuss any potential speedup or advantage over classical methods.

4. Implementation Considerations (150-200 words):
   a) Describe the quantum resources (e.g., qubits, quantum gates) required for your algorithm.
   b) Discuss any challenges in implementing your algorithm on current or near-term quantum hardware.
   c) Suggest potential optimizations or variations of your algorithm.

5. Limitations and Future Work (100-150 words):
   a) Identify any limitations or potential drawbacks of your quantum algorithm.
   b) Propose ideas for future research to improve or extend your algorithm.

Ensure your response demonstrates a deep understanding of both quantum computing principles and the specific problem domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 750-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the {t['problem']} problem and quantum computing principles.",
            "The proposed quantum algorithm should be novel, well-explained, and leverage quantum phenomena appropriately.",
            "The complexity analysis should be thorough and compare the quantum approach to the classical {t['classical_algorithm']} algorithm.",
            "Implementation considerations should address quantum resources and practical challenges realistically.",
            "Limitations and future work should be thoughtfully considered and relevant to the proposed algorithm.",
            "The overall response should be well-structured, adhere to the word count guidelines, and demonstrate interdisciplinary knowledge and creative problem-solving in quantum computing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
