import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "Optimize supply chain logistics for a global manufacturing company",
            "Enhance the accuracy of weather prediction models",
            "Improve the efficiency of drug discovery processes in pharmaceutical research",
            "Optimize traffic flow in a large metropolitan area",
            "Enhance cryptographic security for sensitive financial transactions"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum interference",
            "Quantum annealing",
            "Quantum Fourier transform"
        ]
        
        tasks = {}
        for i in range(2):
            problem = random.choice(problems)
            concept = random.choice(quantum_concepts)
            tasks[str(i+1)] = {
                "problem": problem,
                "quantum_concept": concept
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm to solve the following real-world problem: {t['problem']}. Your algorithm should specifically leverage the quantum concept of {t['quantum_concept']}. Provide your response in the following format:

1. Problem Analysis (100-150 words):
   Analyze the given problem and explain why a quantum approach might be advantageous compared to classical computing methods.

2. Quantum Algorithm Design (250-300 words):
   a) Describe your proposed quantum algorithm, explaining its key steps and components.
   b) Explain how your algorithm utilizes the specified quantum concept.
   c) Discuss any quantum gates or operations that are crucial to your algorithm.

3. Implementation Considerations (150-200 words):
   a) Describe the quantum resources (e.g., number of qubits, circuit depth) required for your algorithm.
   b) Discuss any potential challenges in implementing your algorithm on current or near-term quantum hardware.
   c) Suggest possible ways to mitigate these challenges.

4. Expected Performance Analysis (150-200 words):
   a) Estimate the potential speedup or improvement your quantum algorithm might offer compared to the best known classical approach.
   b) Discuss any limitations or trade-offs of your quantum approach.
   c) Propose a method to verify the correctness and efficiency of your algorithm.

5. Broader Implications (100-150 words):
   Discuss the potential impact of successfully implementing this quantum algorithm on the industry or field related to the problem. Consider both short-term and long-term implications.

Ensure your response demonstrates a deep understanding of quantum computing principles, creative problem-solving skills, and the ability to apply quantum concepts to real-world challenges. Use clear, precise language and explain any technical terms or concepts you introduce."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the given problem and the potential advantages of a quantum approach",
            f"The proposed quantum algorithm effectively utilizes the concept of {t['quantum_concept']}",
            "The algorithm design is logically sound and aligns with established quantum computing principles",
            "The implementation considerations show an understanding of current quantum computing limitations and challenges",
            "The performance analysis provides a reasonable estimation of the algorithm's potential impact and limitations",
            "The discussion of broader implications demonstrates an understanding of the algorithm's potential real-world impact",
            "The overall response shows creativity in applying quantum computing concepts to solve a complex real-world problem"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
