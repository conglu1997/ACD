import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_concept": "Superposition",
                "linguistic_application": "Word sense disambiguation",
                "example_word": "bank"
            },
            {
                "quantum_concept": "Entanglement",
                "linguistic_application": "Semantic coherence in text generation",
                "example_word": "quantum"
            },
            {
                "quantum_concept": "Quantum tunneling",
                "linguistic_application": "Metaphor comprehension",
                "example_word": "breakthrough"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop a quantum-inspired linguistic model based on the quantum concept of {t['quantum_concept']} and apply it to the linguistic task of {t['linguistic_application']}. Use the word "{t['example_word']}" as an example in your explanation.

Quantum mechanics is a fundamental theory in physics that describes nature at the smallest scales of energy levels of atoms and subatomic particles. It introduces concepts that challenge our everyday understanding of reality, such as superposition, entanglement, and quantum tunneling.

Your task is to creatively apply these quantum concepts to linguistics. While this task is speculative in nature, strive to ground your ideas in scientific principles and logical reasoning.

Your response should include:

1. Quantum Concept Explanation (100-150 words):
   Explain the quantum concept and its key properties.

2. Linguistic Application (150-200 words):
   Describe how the quantum concept could be applied to the given linguistic task.
   Explain the potential benefits and challenges of this approach.

3. Quantum Linguistic Model (250-300 words):
   Propose a specific model that incorporates the quantum concept into linguistic analysis or generation.
   Describe its components, mechanisms, and how it would process language.

4. Example Application (150-200 words):
   Demonstrate how your model would analyze or generate text using the example word.
   Explain the quantum-inspired aspects of this process.

5. Implications and Future Directions (100-150 words):
   Discuss potential implications of your model for linguistics and natural language processing.
   Suggest future research directions or potential applications.

Ensure your response is creative yet grounded in both quantum mechanics and linguistics. Use appropriate terminology from both fields and provide clear explanations of complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should explain the quantum concept of {t['quantum_concept']} accurately",
            f"The response should describe a plausible application of {t['quantum_concept']} to {t['linguistic_application']}",
            "The proposed quantum linguistic model should be innovative yet logically consistent",
            f"The example application should use the word '{t['example_word']}' and demonstrate the model's quantum-inspired aspects",
            "The response should discuss implications and future directions for quantum-inspired linguistics",
            "The response should demonstrate a clear understanding of both quantum mechanics and linguistics",
            "The response should follow the specified format and word count guidelines",
            "The response should balance creativity with scientific grounding"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
