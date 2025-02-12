import random
from typing import List, Tuple

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "nlp_task": "semantic_similarity",
                "quantum_concept": "superposition",
                "evolutionary_mechanism": "mutation"
            },
            {
                "nlp_task": "text_generation",
                "quantum_concept": "entanglement",
                "evolutionary_mechanism": "crossover"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired evolutionary algorithm for the NLP task of {t['nlp_task']}, incorporating the quantum concept of {t['quantum_concept']} and the evolutionary mechanism of {t['evolutionary_mechanism']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen NLP task and its challenges.
   b) Describe how the quantum concept can be applied to this task.
   c) Discuss how the evolutionary mechanism can be integrated into the algorithm.

2. Algorithm Design (300-350 words):
   a) Provide a high-level description of your quantum-inspired evolutionary algorithm.
   b) Explain how it incorporates the specified quantum concept and evolutionary mechanism.
   c) Describe the representation of linguistic data in your quantum-inspired system.
   d) Include pseudocode or a flowchart illustrating the key steps of your algorithm.

3. Implementation Details (200-250 words):
   a) Describe how you would implement the quantum-inspired components of your algorithm.
   b) Explain how you would handle the evolutionary processes in the context of the NLP task.
   c) Discuss any technical challenges in implementing this algorithm and propose solutions.

4. Performance Analysis (200-250 words):
   a) Propose a method to evaluate the performance of your algorithm on the specified NLP task.
   b) Discuss potential advantages and limitations compared to classical NLP approaches.
   c) Suggest how the algorithm's performance might scale with problem size or complexity.

5. Practical Applications (150-200 words):
   a) Propose two potential real-world applications of your quantum-inspired evolutionary NLP algorithm.
   b) Discuss how these applications might benefit from the quantum and evolutionary aspects of your approach.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of using quantum-inspired evolutionary algorithms in NLP.
   b) Suggest two directions for future research to enhance or expand your algorithm.

Ensure your response demonstrates a deep understanding of quantum computing principles, evolutionary algorithms, and natural language processing. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the NLP task of {t['nlp_task']}",
            f"The response incorporates the quantum concept of {t['quantum_concept']}",
            f"The response integrates the evolutionary mechanism of {t['evolutionary_mechanism']}",
            "The response includes all required sections with appropriate content",
            "The response demonstrates a deep understanding of quantum computing, evolutionary algorithms, and NLP",
            "The proposed algorithm is innovative while maintaining scientific plausibility",
            "The response is well-structured and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
