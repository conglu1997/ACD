import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ai_tasks = [
            {
                'task': 'image classification',
                'quantum_property': 'superposition',
                'classical_limitation': 'high computational complexity for large datasets'
            },
            {
                'task': 'natural language processing',
                'quantum_property': 'entanglement',
                'classical_limitation': 'difficulty in capturing long-range dependencies'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(ai_tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm for enhancing the AI task of {t['task']}, leveraging the quantum property of {t['quantum_property']}. Your algorithm should address the classical limitation of {t['classical_limitation']}. Provide your response in the following format:

1. Algorithm Overview (200-250 words):
   a) Provide a high-level description of your quantum AI algorithm.
   b) Explain how it incorporates the specified quantum property.
   c) Describe how it addresses the given classical limitation.

2. Quantum Computing Principles (250-300 words):
   a) Explain the relevant quantum computing principles underlying your algorithm.
   b) Discuss how these principles contribute to enhancing the AI task.
   c) Provide a mathematical representation of a key quantum operation in your algorithm, using Dirac notation or quantum circuit notation. Explain the significance of each component.

3. Algorithm Implementation (300-350 words):
   a) Describe the step-by-step process of your algorithm's operation.
   b) Explain how classical and quantum components interact in your hybrid algorithm.
   c) Discuss any required quantum hardware or technologies for implementing your algorithm.
   d) Include pseudocode or a quantum circuit diagram illustrating the key steps of your algorithm.

4. Theoretical Analysis (250-300 words):
   a) Analyze the theoretical advantages of your quantum AI algorithm over classical approaches.
   b) Provide a computational complexity analysis, comparing your algorithm to the best known classical algorithm for the task.
   c) Discuss any potential limitations or challenges in your approach.

5. Experimental Setup (200-250 words):
   a) Propose an experimental setup to demonstrate the superiority of your quantum AI algorithm.
   b) Describe the dataset, quantum hardware, and classical computing resources required.
   c) Explain how you would measure and compare the performance of your algorithm against classical benchmarks.

6. Potential Impact (150-200 words):
   a) Discuss the potential impact of your quantum AI algorithm on the field of artificial intelligence.
   b) Explore possible applications or adaptations of your algorithm to other AI tasks.
   c) Address any ethical considerations related to the development and use of quantum-enhanced AI.

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your algorithm.
   b) Propose a research question that could further the development of quantum AI algorithms in this area.

Ensure your response demonstrates a deep understanding of both quantum computing and artificial intelligence. Be creative in your algorithm design while maintaining scientific plausibility and addressing real-world applicability. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing principles and AI algorithms.",
            "The proposed quantum AI algorithm is novel and creative while maintaining scientific plausibility.",
            "The algorithm effectively incorporates the specified quantum property and addresses the given classical limitation.",
            "The mathematical representation and pseudocode/circuit diagram are correct and well-explained.",
            "The theoretical analysis provides a convincing argument for the algorithm's advantages over classical approaches.",
            "The experimental setup is well-designed and feasible for demonstrating the algorithm's superiority.",
            "The response addresses all required sections with appropriate depth and clarity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
