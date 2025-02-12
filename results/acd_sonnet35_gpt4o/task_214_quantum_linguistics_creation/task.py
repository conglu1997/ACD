import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                'concept': 'Quantum Entanglement',
                'description': 'A quantum phenomenon where particles become interconnected and the quantum state of each particle cannot be described independently of the others.'
            },
            {
                'concept': 'Quantum Superposition',
                'description': 'The principle that a quantum system can exist in multiple states simultaneously until measured or observed.'
            }
        ]
        return {str(i+1): task for i, task in enumerate(quantum_concepts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a specialized language for describing quantum phenomena, then use it to explain the concept of {t['concept']}. Your task has three parts:

1. Language Design (150-200 words):
   Create a language specifically tailored for describing quantum phenomena. Include:
   a) At least 3 unique grammatical features that reflect quantum behavior
   b) A brief explanation of how the language's structure mirrors quantum principles
   c) 5 example words or phrases in your language, with their English translations

2. Concept Explanation (100-150 words):
   Use your designed language to explain the concept of {t['concept']}. Provide:
   a) A paragraph in your quantum language
   b) An English translation of your explanation
   c) A brief analysis of how your language enhances the explanation of this quantum concept

3. Language Application (100-150 words):
   Discuss potential applications of your quantum language in:
   a) Scientific research and communication
   b) Education and public understanding of quantum physics
   c) Potential limitations or challenges of using this specialized language

Ensure your response demonstrates a deep understanding of both linguistic principles and quantum mechanics, while showcasing creativity in language design and application.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design is creative and effectively mirrors quantum principles.",
            "The concept explanation in the quantum language is coherent and accurately represents the given quantum concept.",
            "The discussion of language applications demonstrates a nuanced understanding of both linguistics and quantum physics.",
            "The overall response shows a high level of interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
