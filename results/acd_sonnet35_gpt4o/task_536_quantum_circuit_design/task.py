import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem": "integer factorization",
                "algorithm": "Shor's algorithm",
                "qubits": 7,
                "input": 15
            },
            {
                "problem": "database search",
                "algorithm": "Grover's algorithm",
                "qubits": 4,
                "input": "unsorted database of 16 items"
            },
            {
                "problem": "quantum fourier transform",
                "algorithm": "QFT",
                "qubits": 3,
                "input": "arbitrary 3-qubit state"
            },
            {
                "problem": "quantum teleportation",
                "algorithm": "Teleportation protocol",
                "qubits": 3,
                "input": "arbitrary single-qubit state"
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are a quantum computing expert. Your task is to design and analyze a quantum circuit for the following problem:\n\nProblem: {t['problem']}\nSuggested Algorithm: {t['algorithm']}\nNumber of Qubits: {t['qubits']}\nInput: {t['input']}\n\nYour response should include:\n\n1. A brief explanation of the problem and the suggested algorithm (2-3 sentences)\n2. A detailed description of your quantum circuit design, including the specific gates used and their arrangement (150-200 words)\n3. An analysis of how your circuit implements the algorithm and solves the problem (100-150 words)\n4. A discussion of the circuit's efficiency and any potential optimizations (50-100 words)\n5. One potential challenge in implementing this circuit on current quantum hardware and how you would address it (2-3 sentences)\n6. A creative idea for visualizing or explaining the quantum state evolution in your circuit to a non-expert audience (2-3 sentences)\n\nEnsure your solution is technically accurate and demonstrates a clear understanding of quantum computing principles and the specified algorithm."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['problem']} and {t['algorithm']}.",
            "The quantum circuit design is technically accurate and appropriate for the given problem.",
            f"The circuit design correctly uses {t['qubits']} qubits and addresses the given input: {t['input']}.",
            "The analysis of the circuit's implementation and efficiency is sound and insightful.",
            "The proposed challenge and solution for hardware implementation are relevant and well-reasoned.",
            "The visualization or explanation idea for non-experts is creative and appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
