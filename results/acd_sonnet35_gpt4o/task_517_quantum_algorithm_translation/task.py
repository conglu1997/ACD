import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_algorithms = [
            {
                "name": "Grover's Algorithm",
                "description": "A quantum algorithm for unstructured search that finds with high probability the unique input to a black box function that produces a particular output value, using O(√N) queries to the black box, where N is the size of the function's domain.",
                "application": "Database searching"
            },
            {
                "name": "Shor's Algorithm",
                "description": "A quantum algorithm for integer factorization that runs in polynomial time, significantly faster than the most efficient known classical factoring algorithm.",
                "application": "Breaking RSA encryption"
            }
        ]
        return {
            "1": random.choice(quantum_algorithms),
            "2": random.choice(quantum_algorithms)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the quantum algorithm '{t['name']}' and complete the following tasks:\n\n1. Explanation (200-250 words):\n   a) Describe the purpose and function of {t['name']}.\n   b) Explain the key quantum principles it utilizes.\n   c) Discuss its significance in the field of {t['application']}.\n\n2. Classical Approximation (250-300 words):\n   a) Design a classical algorithm that approximates the behavior of {t['name']}.\n   b) Explain your algorithm's approach and how it mimics the quantum algorithm.\n   c) Provide pseudocode for your classical algorithm.\n\n3. Complexity Analysis (200-250 words):\n   a) Analyze the time and space complexity of both the quantum and your classical algorithm.\n   b) Compare their efficiencies and discuss the quantum speedup.\n   c) Explain any limitations or trade-offs in your classical approximation.\n\n4. Potential Improvements (100-150 words):\n   a) Suggest potential optimizations for your classical algorithm.\n   b) Discuss any hybrid quantum-classical approaches that could be beneficial.\n\n5. Practical Implementation (150-200 words):\n   a) Describe the challenges in implementing the quantum algorithm on current quantum hardware.\n   b) Discuss the feasibility of implementing your classical approximation on conventional computers.\n   c) Propose a method to verify the correctness of both implementations.\n\nEnsure your response demonstrates a deep understanding of both quantum and classical computing principles. Use appropriate technical terminology and provide explanations where necessary. Be creative in your classical algorithm design while maintaining scientific accuracy."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation accurately describes the quantum algorithm's purpose, function, and underlying quantum principles.",
            "The classical approximation algorithm is well-designed and logically approximates the quantum algorithm's behavior.",
            "The complexity analysis correctly compares the efficiency of both algorithms and explains the quantum speedup.",
            "The response demonstrates creativity in designing the classical approximation while maintaining scientific accuracy.",
            "The practical implementation section addresses real-world challenges and proposes feasible verification methods."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
