import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        computational_problems = [
            "Graph coloring",
            "Integer factorization",
            "Database search",
            "Optimization of financial portfolios"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum annealing"
        ]
        
        tasks = {
            "1": {
                "problem": random.choice(computational_problems),
                "principle": random.choice(quantum_principles)
            },
            "2": {
                "problem": random.choice(computational_problems),
                "principle": random.choice(quantum_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and optimize a quantum algorithm for the computational problem of {t['problem']}, leveraging the quantum principle of {t['principle']}. Your response should include the following sections:

1. Problem Analysis (150-200 words):
   a) Describe the computational problem and its significance.
   b) Explain why this problem is well-suited for a quantum approach.
   c) Discuss any existing classical algorithms for this problem and their limitations.

2. Quantum Algorithm Design (250-300 words):
   a) Outline your quantum algorithm, explaining how it solves the given problem.
   b) Describe how your algorithm leverages the specified quantum principle.
   c) Provide a high-level circuit diagram or pseudocode for your algorithm.
   d) Explain any novel or innovative aspects of your design.

3. Quantum Resources Analysis (150-200 words):
   a) Estimate the number of qubits required for your algorithm.
   b) Analyze the depth of your quantum circuit.
   c) Discuss any specific quantum gates or operations crucial to your algorithm.

4. Algorithm Optimization (200-250 words):
   a) Propose at least two methods to optimize your quantum algorithm.
   b) Explain how these optimizations improve the algorithm's performance or resource usage.
   c) Discuss any trade-offs involved in these optimizations.

5. Performance Comparison (200-250 words):
   a) Compare the theoretical performance of your quantum algorithm to the best known classical algorithm.
   b) Analyze the potential speedup or other advantages offered by your quantum approach.
   c) Discuss any limitations or constraints of your quantum algorithm.

6. Error Correction and Noise Mitigation (150-200 words):
   a) Discuss potential sources of errors and noise in your quantum algorithm.
   b) Propose at least one error correction or noise mitigation technique for your algorithm.
   c) Analyze the impact of error correction on the algorithm's performance and resource requirements.

7. Practical Implementation and Future Directions (150-200 words):
   a) Provide a specific example or use case for your quantum algorithm.
   b) Discuss challenges in implementing your algorithm on current or near-term quantum hardware.
   c) Propose a method to validate your algorithm using quantum simulation on classical hardware.
   d) Suggest potential improvements or extensions to your algorithm for future research.

Ensure your response demonstrates a deep understanding of both quantum computing principles and the specified computational problem. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, including the word count for each section in parentheses at the end. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed quantum algorithm for {t['problem']} that leverages {t['principle']}",
            "The quantum algorithm design is clearly explained and includes innovative aspects",
            "The quantum resources required for the algorithm are thoroughly analyzed",
            "The response includes at least two methods to optimize the quantum algorithm",
            "The performance comparison between the quantum and classical approaches is comprehensive",
            "The response addresses error correction and noise mitigation techniques",
            "A specific example or use case for the quantum algorithm is provided",
            "The response addresses practical implementation challenges and future research directions",
            "The response demonstrates deep understanding of quantum computing principles and the computational problem",
            "The response adheres to the specified format and word count requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
