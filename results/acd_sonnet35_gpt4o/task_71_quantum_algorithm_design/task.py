import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "name": "Integer Factorization",
                "description": "Given a large composite number N, find its prime factors.",
                "classical_algorithm": "Trial division or more advanced classical algorithms like the Quadratic Sieve.",
                "quantum_hint": "Consider using Shor's algorithm or a variation of it."
            },
            {
                "name": "Database Search",
                "description": "Search an unsorted database of N items to find a specific item.",
                "classical_algorithm": "Linear search, which takes O(N) time.",
                "quantum_hint": "Consider using Grover's algorithm or a variation of it."
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum algorithm to solve the following classical computing problem:\n\nProblem: {t['name']}\nDescription: {t['description']}\n\nClassical Approach: {t['classical_algorithm']}\n\nYour task:\n1. Design a quantum algorithm to solve this problem. {t['quantum_hint']}\n2. Describe your quantum algorithm in detail, including:\n   a) The quantum gates and operations used\n   b) The number of qubits required\n   c) The overall structure and steps of the algorithm\n3. Analyze the time complexity of your quantum algorithm and compare it to the classical approach.\n4. Discuss any potential advantages or limitations of your quantum approach compared to classical methods.\n5. Suggest a potential real-world application where your quantum algorithm could provide a significant advantage.\n6. Provide a simple example or simulation of your quantum algorithm for a small instance of the problem. This can be a step-by-step breakdown of the algorithm's execution or a description of the quantum states at key points in the computation.\n\nEnsure your response is well-structured, scientifically accurate, and demonstrates a deep understanding of both quantum computing principles and the problem at hand."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The quantum algorithm design is scientifically sound and correctly applies quantum computing principles.",
            "The algorithm description is detailed, including specific quantum gates, qubit requirements, and clear steps.",
            "The complexity analysis accurately compares the quantum approach to classical methods.",
            "The response demonstrates a deep understanding of both quantum computing and the given problem.",
            "The suggested real-world application is relevant and showcases a significant potential advantage of the quantum approach.",
            "The provided example or simulation accurately represents the algorithm's execution for a small instance of the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
