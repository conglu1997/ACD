import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'superposition',
                'linguistic_feature': 'polysemy',
                'programming_paradigm': 'functional',
                'quantum_problem': 'quantum state tomography'
            },
            {
                'quantum_concept': 'entanglement',
                'linguistic_feature': 'agreement',
                'programming_paradigm': 'object-oriented',
                'quantum_problem': 'quantum error correction'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on the quantum computing concept of {t['quantum_concept']} and use it to encode the linguistic feature of {t['linguistic_feature']}. Your language should follow the {t['programming_paradigm']} programming paradigm. Provide your response in the following format:

1. Language Overview (100-150 words):
   Briefly describe your quantum-inspired programming language, explaining how it incorporates the given quantum concept and linguistic feature.

2. Key Language Features (list 4-5 points, 30-50 words each):
   Describe the main features of your language, explaining how each relates to quantum computing, linguistics, and the specified programming paradigm.

3. Syntax and Structure (100-150 words):
   Explain the basic syntax and structure of your language, providing examples of how it represents quantum states and linguistic elements.

4. Code Example (10-15 lines of code):
   Provide a sample code snippet in your language that demonstrates the encoding of the specified linguistic feature using quantum-inspired constructs.

5. Execution Model (100-150 words):
   Describe how code in your language would be executed, explaining any quantum-inspired processing or linguistic interpretation steps.

6. Practical Application (100-150 words):
   Propose a practical application of your language in fields such as natural language processing, cryptography, or artificial intelligence.

7. Quantum Problem Solving (100-150 words):
   Explain how your language could be used to approach the quantum computing problem of {t['quantum_problem']}. Provide a high-level description of how the language's features would be particularly suited to addressing this problem.

8. Limitations and Future Directions (100-150 words):
   Discuss potential limitations of your language and suggest areas for future development or research.

Ensure your language design is innovative, theoretically grounded in both quantum computing and linguistics, and clearly demonstrates how it could potentially enhance our understanding or application of these fields."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language effectively incorporates the quantum concept of {t['quantum_concept']}.",
            f"The language successfully encodes the linguistic feature of {t['linguistic_feature']}.",
            f"The language adheres to the principles of {t['programming_paradigm']} programming.",
            "The response demonstrates a deep understanding of both quantum computing and linguistics.",
            "The language design is innovative and theoretically sound.",
            "The code example clearly illustrates the language's quantum-inspired encoding of linguistic features.",
            "The proposed practical application is feasible and demonstrates potential real-world value.",
            f"The explanation of how the language could be used to approach {t['quantum_problem']} is logical and demonstrates understanding of both the language's capabilities and the quantum problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
