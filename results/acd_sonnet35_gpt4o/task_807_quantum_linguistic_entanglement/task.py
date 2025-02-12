import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "linguistic_feature": "Ambiguity",
                "communication_problem": "Conveying multiple meanings simultaneously in a diplomatic message"
            },
            {
                "quantum_principle": "Entanglement",
                "linguistic_feature": "Anaphora",
                "communication_problem": "Creating a secure communication system based on linguistically entangled sentences"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Apply the quantum mechanical principle of {t['quantum_principle']} to analyze and generate linguistically entangled sentences using the linguistic feature of {t['linguistic_feature']}. Then, use this framework to solve the following communication problem: {t['communication_problem']}.

Your task:

1. Quantum-Linguistic Analysis (200-250 words):
   a) Explain the quantum principle of {t['quantum_principle']} and how it can be analogously applied to language.
   b) Describe how the linguistic feature of {t['linguistic_feature']} can be viewed through this quantum lens.
   c) Propose a formal representation or notation for this quantum-linguistic phenomenon.

2. Entangled Sentence Generation (150-200 words):
   a) Create two pairs of linguistically entangled sentences using your proposed framework.
   b) Explain how these sentences demonstrate the principles of both {t['quantum_principle']} and {t['linguistic_feature']}.

3. Communication Problem Solution (250-300 words):
   a) Propose a solution to the given communication problem using your quantum-linguistic framework.
   b) Explain how your solution leverages the principles of {t['quantum_principle']} and {t['linguistic_feature']}.
   c) Discuss potential advantages and limitations of your approach.

4. Quantum-Linguistic Implications (150-200 words):
   a) Discuss how this quantum-linguistic perspective might influence our understanding of language processing or generation.
   b) Propose a potential application of this framework in natural language processing or computational linguistics.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics, and shows creativity in applying these concepts to language and communication. Use appropriate terminology from both fields and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle of {t['quantum_principle']} and its application to language.",
            f"The analysis of the linguistic feature {t['linguistic_feature']} through a quantum lens is insightful and well-explained.",
            "The proposed formal representation or notation for the quantum-linguistic phenomenon is logical and well-defined.",
            "The generated entangled sentences accurately demonstrate the principles of both the quantum concept and the linguistic feature.",
            f"The solution to the communication problem '{t['communication_problem']}' is creative, well-reasoned, and effectively uses the quantum-linguistic framework.",
            "The discussion of implications and potential applications shows depth of understanding and innovative thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
