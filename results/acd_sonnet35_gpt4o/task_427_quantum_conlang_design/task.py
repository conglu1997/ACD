import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "wave-particle duality",
            "quantum tunneling"
        ]
        classical_concepts = [
            "The cat sat on the mat.",
            "Time flies like an arrow."
        ]
        tasks = {
            str(i+1): {
                "quantum_concept": random.choice(quantum_concepts),
                "classical_concept": random.choice(classical_concepts)
            } for i in range(2)
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) based on principles of quantum mechanics, with a focus on the concept of {t['quantum_concept']}. Your task has five parts:

1. Language Design (250-300 words):
   a) Describe the key features of your quantum-inspired conlang, including its phonology, morphology, and syntax.
   b) Explain how these features incorporate the principles of quantum mechanics, especially {t['quantum_concept']}.
   c) Provide at least 5 example words or phrases in your conlang, with their meanings and explanations of how they embody quantum concepts.

2. Grammar Rules (200-250 words):
   a) Outline the main grammatical rules of your conlang.
   b) Explain how these rules parallel concepts in quantum mechanics, particularly {t['quantum_concept']}.
   c) Provide an example sentence demonstrating these rules.

3. Quantum Phenomenon Description (150-200 words):
   a) Describe the quantum phenomenon of {t['quantum_concept']} using your conlang.
   b) Provide a translation and explain how your language captures the essence of this phenomenon.

4. Classical to Quantum Translation (150-200 words):
   Translate the following classical concept into your quantum-inspired conlang:
   "{t['classical_concept']}"
   Provide a word-for-word gloss and explain how the translation incorporates quantum principles.

5. Analysis and Implications (200-250 words):
   a) Discuss the strengths and limitations of your conlang in expressing quantum concepts.
   b) Explain how this conlang might influence thinking about quantum phenomena.
   c) Propose a potential application of this language in quantum physics education or research.

Ensure your response demonstrates a deep understanding of both linguistics and quantum mechanics. Be creative in your language design while maintaining logical consistency with quantum principles.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang should clearly incorporate principles of quantum mechanics, especially {t['quantum_concept']}.",
            "The language design should be creative, coherent, and well-explained.",
            "The grammar rules should be logically consistent and parallel quantum mechanical concepts.",
            f"The description of {t['quantum_concept']} in the conlang should be provided and adequately explained.",
            f"The translation of '{t['classical_concept']}' should incorporate quantum principles and be well-explained.",
            "The analysis should offer insightful reflections on the conlang's properties and potential applications in quantum physics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
