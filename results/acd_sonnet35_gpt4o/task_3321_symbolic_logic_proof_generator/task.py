import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'logical_system': 'Propositional Logic',
                'axioms': [
                    'A → (B → A)',
                    '(A → (B → C)) → ((A → B) → (A → C))',
                    '(¬B → ¬A) → ((¬B → A) → B)'
                ],
                'theorem': '(A → B) → (¬B → ¬A)',
                'proof_technique': 'Deduction'
            },
            {
                'logical_system': 'First-Order Logic',
                'axioms': [
                    '∀x(P(x) → Q(x))',
                    '∀x(Q(x) → R(x))',
                    '∃xP(x)'
                ],
                'theorem': '∃xR(x)',
                'proof_technique': 'Natural Deduction'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with generating and verifying a formal proof in symbolic logic, then translating it into a natural language explanation. Use the following parameters:

Logical System: {t['logical_system']}
Axioms: {', '.join(t['axioms'])}
Theorem to Prove: {t['theorem']}
Proof Technique: {t['proof_technique']}

Your response should include the following sections, clearly labeled:

1. Formal Proof (200-300 words):
   a) Construct a step-by-step formal proof of the theorem using the given axioms and standard inference rules.
   b) Use the specified proof technique: {t['proof_technique']}.
   c) Number each step and provide justification (axiom, inference rule, or previous step).
   d) Use standard logical notation (→ for implication, ¬ for negation, ∧ for conjunction, ∨ for disjunction, ∀ for universal quantifier, ∃ for existential quantifier).

2. Proof Verification (100-150 words):
   a) Explain how each step in your proof follows logically from the previous steps or axioms.
   b) Verify that your proof is valid and complete.

3. Natural Language Translation (200-250 words):
   a) Translate your formal proof into a clear, coherent natural language explanation.
   b) Ensure your explanation is accessible to someone with basic knowledge of logic.
   c) Maintain the logical structure and rigor of the original proof in your translation.

4. Meta-Analysis (150-200 words):
   a) Discuss any interesting patterns or insights you noticed while constructing the proof.
   b) Explain how this theorem relates to the broader context of {t['logical_system']}.
   c) Suggest a potential real-world application or implication of this theorem.

Ensure your response demonstrates a deep understanding of symbolic logic, formal proof systems, and the ability to translate between formal and natural language. Adhere to the word limits for each section and use appropriate logical notation throughout."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The formal proof correctly uses the {t['proof_technique']} technique and standard logical notation.",
            "Each step in the proof is properly justified by citing axioms, inference rules, or previous steps.",
            "The proof is valid, complete, and successfully proves the given theorem.",
            "The proof verification demonstrates a clear understanding of the logical steps and their justifications.",
            "The natural language translation accurately represents the formal proof while being clear and accessible.",
            "The meta-analysis shows insight into the logical system and provides a relevant real-world application.",
            "The response adheres to the specified word limits and section structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
