import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_structures = [
            {
                "structure": "Group theory",
                "concept": "Symmetry",
                "example": "The rotational symmetry of a square"
            },
            {
                "structure": "Topology",
                "concept": "Continuity",
                "example": "The properties of a Möbius strip"
            }
        ]
        return {
            "1": random.choice(mathematical_structures),
            "2": random.choice(mathematical_structures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a linguistic expression that is isomorphic to the mathematical structure of {t['structure']}, focusing on the concept of {t['concept']}. Use {t['example']} as a reference point. Your response should include:

1. Linguistic Isomorphism (200-250 words):
   a) Create a novel linguistic expression or mini-language that mirrors the structure and properties of the given mathematical concept.
   b) Explain how your linguistic construction corresponds to key elements of the mathematical structure.
   c) Provide at least two examples of how operations or transformations in the mathematical domain are reflected in your linguistic expression.

2. Formal Analysis (150-200 words):
   a) Define the 'grammar' or rules of your linguistic isomorphism using formal notation (e.g., BNF or mathematical notation).
   b) Explain how this formal representation captures the essential properties of the mathematical structure.

3. Cognitive Implications (200-250 words):
   a) Discuss how your linguistic isomorphism might influence or reflect cognitive processing of the mathematical concept.
   b) Analyze potential advantages or limitations of using your linguistic framework to reason about the mathematical structure.
   c) Propose an experiment to test whether exposure to your linguistic isomorphism improves understanding or problem-solving related to the mathematical concept.

4. Cross-domain Application (150-200 words):
   a) Suggest how your linguistic isomorphism could be applied to a domain outside of mathematics (e.g., in art, music, or social systems).
   b) Explain how this application might provide new insights or perspectives in the chosen domain.

5. Limitations and Extensions (100-150 words):
   a) Discuss any limitations of your linguistic isomorphism in fully capturing the mathematical structure.
   b) Propose at least one way to extend or refine your linguistic framework to address these limitations.

Ensure your response demonstrates a deep understanding of both the mathematical structure and linguistic principles. Be creative in your linguistic construction while maintaining a rigorous correspondence to the mathematical concept. Use appropriate terminology from both mathematics and linguistics."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['structure']} and the concept of {t['concept']}.",
            "The linguistic isomorphism created is novel, well-defined, and accurately mirrors the given mathematical structure.",
            "The formal analysis uses appropriate notation and effectively captures the properties of the mathematical structure.",
            "The discussion of cognitive implications is insightful and proposes a plausible experiment.",
            "The cross-domain application is creative and well-reasoned.",
            "The response acknowledges limitations and proposes meaningful extensions to the linguistic isomorphism.",
            "The overall response shows strong interdisciplinary thinking, connecting concepts from mathematics, linguistics, and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
