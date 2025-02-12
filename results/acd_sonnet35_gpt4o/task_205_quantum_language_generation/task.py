import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'superposition',
                'linguistic_rule': 'Each sentence must have at least one word that can be interpreted in two different ways simultaneously.',
                'theme': 'A day at the beach'
            },
            {
                'quantum_concept': 'entanglement',
                'linguistic_rule': 'Create pairs of sentences where changing a word in one sentence necessitates a specific change in its paired sentence, regardless of their position in the text.',
                'theme': 'A mysterious library'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short paragraph (4-6 sentences) on the theme of '{t['theme']}' that incorporates the quantum mechanics concept of {t['quantum_concept']} as a linguistic rule.

Quantum Concept: {t['quantum_concept']}
Linguistic Rule: {t['linguistic_rule']}

Your paragraph should:
1. Adhere strictly to the given linguistic rule.
2. Be coherent and meaningful, not just a collection of sentences.
3. Demonstrate a clear understanding of the quantum mechanics concept.
4. Be creative and engaging.

After your paragraph, provide a brief explanation (2-3 sentences) of how your text demonstrates the quantum concept through its linguistic structure.

Format your response as follows:

Paragraph:
[Your paragraph here]

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The paragraph strictly adheres to the linguistic rule: {t['linguistic_rule']}",
            f"The text demonstrates a clear understanding of the quantum concept: {t['quantum_concept']}",
            "The paragraph is coherent, meaningful, and engaging",
            "The explanation clearly describes how the text demonstrates the quantum concept through its linguistic structure"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
