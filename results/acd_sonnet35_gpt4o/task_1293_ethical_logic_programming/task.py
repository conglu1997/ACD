import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'philosophical_framework': 'Utilitarianism',
                'ethical_dilemma': 'Trolley problem'
            },
            {
                'philosophical_framework': 'Kantian deontology',
                'ethical_dilemma': 'Lying to protect someone'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a formal logical system for ethical reasoning based on {t['philosophical_framework']}, then implement it as a simple programming language or extension of an existing language. Use your system to analyze the ethical dilemma of the {t['ethical_dilemma']}. Your response should include:

1. Logical System Design (200-250 words):
   a) Outline the key principles of {t['philosophical_framework']}.
   b) Define the basic elements of your logical system (e.g., predicates, operators, rules of inference).
   c) Explain how your system captures the essence of {t['philosophical_framework']}.

2. Programming Language Implementation (250-300 words):
   a) Describe the syntax and semantics of your ethical programming language or language extension.
   b) Provide example code that demonstrates key features of your language.
   c) Explain how your implementation translates the logical system into computable form.

3. Ethical Dilemma Analysis (200-250 words):
   a) Use your ethical programming language to represent the {t['ethical_dilemma']}.
   b) Show how your system would process and evaluate this dilemma.
   c) Discuss the outcome and any insights gained from this computational ethical reasoning.

4. Reflection and Critique (150-200 words):
   a) Analyze the strengths and limitations of your ethical logic programming system.
   b) Discuss potential real-world applications or implications of such a system.
   c) Consider possible extensions or refinements to your system.

Ensure your response demonstrates a deep understanding of formal logic, {t['philosophical_framework']}, and programming concepts. Be creative in your design while maintaining philosophical and computational rigor.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The logical system accurately represents the key principles of {t['philosophical_framework']}.",
            "The programming language implementation is coherent and demonstrates key features of the ethical logic system.",
            f"The analysis of the {t['ethical_dilemma']} using the implemented system is thorough and insightful.",
            "The reflection demonstrates a critical understanding of the system's strengths, limitations, and potential applications.",
            "The overall response shows a deep integration of formal logic, ethical philosophy, and programming concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
