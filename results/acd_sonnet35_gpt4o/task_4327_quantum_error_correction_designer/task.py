import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        architectures = ['superconducting qubits', 'trapped ions', 'topological qubits']
        error_types = ['bit flip', 'phase flip', 'depolarizing', 'amplitude damping']
        code_types = ['surface code', 'color code', 'stabilizer code']
        
        tasks = {
            "1": {
                "architecture": random.choice(architectures),
                "primary_error": random.choice(error_types),
                "code_inspiration": random.choice(code_types),
                "qubit_count": random.randint(5, 20)
            },
            "2": {
                "architecture": random.choice(architectures),
                "primary_error": random.choice(error_types),
                "code_inspiration": random.choice(code_types),
                "qubit_count": random.randint(5, 20)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a novel quantum error correction code for a {t['architecture']} quantum computing architecture with {t['qubit_count']} qubits, focusing on mitigating {t['primary_error']} errors. Draw inspiration from {t['code_inspiration']} concepts, but develop a unique approach. Then, propose an experiment to validate its effectiveness. Your response should include:

1. Quantum Error Correction Code Design (300-350 words):
   a) Describe the key principles and structure of your novel quantum error correction code.
   b) Explain how it addresses the specific challenges of the given quantum computing architecture.
   c) Detail how your code mitigates the primary error type while considering other potential error sources.
   d) Discuss any trade-offs or limitations in your design.

2. Mathematical Framework (250-300 words):
   a) Provide a mathematical representation of your quantum error correction code.
   b) Include relevant equations, matrices, or diagrams to illustrate the code's structure and operation.
   c) Explain how your mathematical framework captures the error correction process.

3. Error Correction Protocol (200-250 words):
   a) Describe the step-by-step protocol for implementing your error correction code.
   b) Explain how errors are detected and corrected in your system.
   c) Discuss any novel techniques or algorithms used in your protocol.

4. Performance Analysis (200-250 words):
   a) Theoretically analyze the performance of your quantum error correction code.
   b) Compare its expected performance to existing codes for similar architectures.
   c) Discuss the code's efficiency in terms of resource usage and error correction capability.

5. Experimental Validation Proposal (250-300 words):
   a) Design an experiment to test and validate your quantum error correction code.
   b) Describe the experimental setup, including required equipment and measurements.
   c) Explain how you would analyze the results to confirm the code's effectiveness.
   d) Discuss potential challenges in implementing the experiment and how to address them.

6. Implications and Future Work (150-200 words):
   a) Discuss the potential impact of your quantum error correction code on quantum computing.
   b) Explore possible applications or extensions of your approach.
   c) Suggest directions for future research to enhance or expand upon your code.

Ensure your response demonstrates a deep understanding of quantum mechanics, error correction principles, and the specific challenges of the given quantum computing architecture. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1350-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, error correction principles, and the specific challenges of the given quantum computing architecture.",
            f"The quantum error correction code design effectively addresses the challenges of {t['architecture']} and mitigates {t['primary_error']} errors.",
            "The mathematical framework is well-developed and accurately represents the quantum error correction code.",
            "The error correction protocol is clearly explained and includes novel techniques or algorithms.",
            "The performance analysis provides a thorough theoretical evaluation of the code's effectiveness.",
            "The experimental validation proposal is well-designed and feasible for testing the code's performance.",
            "The response discusses implications and future work in a thoughtful and insightful manner.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The approach is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified word counts and format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
