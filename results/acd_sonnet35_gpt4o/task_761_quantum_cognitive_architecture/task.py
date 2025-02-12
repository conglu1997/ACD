import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_process': 'decision-making',
                'quantum_principle': 'superposition',
                'information_theory_concept': 'entropy'
            },
            {
                'cognitive_process': 'memory retrieval',
                'quantum_principle': 'entanglement',
                'information_theory_concept': 'mutual information'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum cognitive architecture that models the cognitive process of {t['cognitive_process']} by integrating the quantum principle of {t['quantum_principle']} and the information theory concept of {t['information_theory_concept']}. Your response should include:

1. Architectural Overview (250-300 words):
   a) Describe the key components of your quantum cognitive architecture.
   b) Explain how it incorporates the specified quantum principle and information theory concept.
   c) Discuss how this architecture models the given cognitive process.

2. Quantum-Cognitive Mapping (200-250 words):
   a) Detail how you map quantum states or processes to cognitive states or processes.
   b) Explain how the specified quantum principle enhances the modeling of the cognitive process.
   c) Provide a specific example of how this mapping works in your architecture.

3. Information Processing Mechanism (200-250 words):
   a) Describe how information is processed in your architecture.
   b) Explain how the specified information theory concept is utilized.
   c) Discuss any novel insights this approach might offer about the cognitive process.

4. Mathematical Formulation (150-200 words):
   a) Provide a basic mathematical framework for your architecture.
   b) Include at least one equation that integrates quantum and cognitive elements.
   c) Explain the significance of each term in your equation(s).

5. Experimental Predictions (150-200 words):
   a) Propose two testable predictions that your architecture makes about human cognition.
   b) Describe potential experiments to validate these predictions.

6. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations or challenges of your proposed architecture.
   b) Suggest two future research directions to address these limitations or extend the architecture.

7. Interdisciplinary Implications (100-150 words):
   a) Discuss potential implications of your architecture for quantum physics, cognitive science, and information theory.
   b) Propose how insights from this model could influence other scientific disciplines.

Ensure your response demonstrates a deep understanding of quantum physics, cognitive science, and information theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The architecture successfully integrates principles from quantum physics, information theory, and cognitive science.",
            f"The design effectively models the cognitive process of {t['cognitive_process']}.",
            f"The architecture appropriately incorporates the quantum principle of {t['quantum_principle']}.",
            f"The design effectively utilizes the information theory concept of {t['information_theory_concept']}.",
            "The quantum-cognitive mapping is logically sound and well-explained.",
            "The mathematical formulation is correct and relevant to the proposed architecture.",
            "The experimental predictions are testable and logically follow from the proposed architecture.",
            "The response demonstrates a deep understanding of all three fields: quantum physics, cognitive science, and information theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
