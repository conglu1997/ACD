import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'superposition',
                'poetic_element': 'metaphor'
            },
            {
                'quantum_concept': 'entanglement',
                'poetic_element': 'rhythm'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language generation system based on the quantum concept of {t['quantum_concept']}, and use it to create a new form of poetry that incorporates the poetic element of {t['poetic_element']}. Your response should include:

1. System Design (250-300 words):
   a) Explain how your language generation system incorporates the quantum concept of {t['quantum_concept']}.
   b) Describe how it manipulates {t['poetic_element']} to create quantum-like effects in poetry.
   c) Provide 3-4 key rules or principles of your system, relating them to specific quantum phenomena.

2. Quantum Poetry Generation (200-250 words):
   a) Using your system, generate a short poem (4-6 lines) that demonstrates the quantum-linguistic principles you've defined.
   b) Explain how each part of your poem reflects the quantum concept and poetic element.
   c) Discuss how the reader's interpretation might affect the poem's 'quantum state'.

3. Mathematical Formalism (150-200 words):
   a) Provide a mathematical or logical representation of your quantum poetry system.
   b) Explain how this formalism captures both the quantum and linguistic aspects of your system.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum poetry approach with traditional poetic forms.
   b) Discuss potential advantages and limitations of your system for artistic expression.
   c) Explain how your system might provide new insights into the nature of language and quantum phenomena.

5. Potential Applications (150-200 words):
   a) Propose two potential applications of your quantum poetry system outside of creative writing.
   b) Discuss how these applications might contribute to fields such as cognitive science, quantum computing, or linguistics.

Ensure your response demonstrates a deep understanding of both quantum mechanics and poetics. Be creative in your system design and poetry generation while maintaining scientific plausibility. Use appropriate terminology from both fields throughout your answer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a quantum-inspired language generation system based on {t['quantum_concept']} and incorporates {t['poetic_element']}.",
            "The system design clearly explains how it incorporates the specified quantum concept and manipulates the given poetic element.",
            "A short poem is generated using the system, with a clear explanation of how it demonstrates the quantum-linguistic principles.",
            "A mathematical or logical formalism of the quantum poetry system is provided and explained.",
            "The response includes a comparative analysis of the quantum poetry approach with traditional poetic forms.",
            "Potential applications of the quantum poetry system outside of creative writing are proposed and discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
