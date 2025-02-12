import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        algebraic_properties = [
            "commutativity",
            "associativity",
            "distributivity",
            "identity element",
            "inverse elements"
        ]
        applications = [
            "cryptography",
            "quantum mechanics",
            "crystallography",
            "error-correcting codes",
            "particle physics"
        ]
        constraints = [
            "must have a substructure isomorphic to Z_3",
            "must have exactly two maximal proper substructures",
            "must have an automorphism group of order 4",
            "must have a non-trivial center"
        ]
        return {
            "1": {
                "properties": random.sample(algebraic_properties, 4),
                "application": random.choice(applications),
                "constraint": random.choice(constraints)
            },
            "2": {
                "properties": random.sample(algebraic_properties, 4),
                "application": random.choice(applications),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel abstract algebraic structure incorporating the following properties: {', '.join(t['properties'])}. Your structure {t['constraint']}. Then, apply this structure to solve two interconnected problems in the field of {t['application']}. Your response should include:

1. Structure Definition (250-300 words):
   a) Define your abstract algebraic structure, clearly stating its elements and operations.
   b) Prove that your structure satisfies the given properties and the specified constraint.
   c) Discuss any additional properties or interesting features of your structure.
   d) Compare your structure to a well-known algebraic structure, highlighting similarities and differences.

2. Visualization (100-150 words + ASCII art or detailed description):
   Provide a visual representation of your algebraic structure. This could be a Cayley table, a graph, or any other appropriate visualization. Use ASCII art or Unicode characters to create the visualization, and provide a brief explanation of what it represents.

3. Theorem and Proof (200-250 words):
   State and prove a non-trivial theorem about your algebraic structure.

4. Application (300-350 words):
   a) Describe two interconnected problems in {t['application']} that your structure can address.
   b) Explain how your structure models or solves these problems.
   c) Discuss the advantages of using your structure over traditional approaches.
   d) Analyze any potential limitations or challenges in applying your structure to these problems.

5. Generalization and Future Directions (150-200 words):
   a) Discuss possible generalizations or variations of your structure.
   b) Propose a research question or conjecture about your structure that could be explored in future work.

Ensure your response demonstrates a deep understanding of abstract algebra and the ability to apply it creatively to real-world problems. Use appropriate mathematical notation (you may use LaTeX for complex expressions) and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of abstract algebra and group theory.",
            "The algebraic structure is correctly defined, satisfies all given properties and the specified constraint, and is compared insightfully to a known structure.",
            "The visualization effectively represents the structure of the algebraic system.",
            "The theorem and its proof are mathematically sound, non-trivial, and relevant to the structure.",
            f"The application to the two interconnected problems in {t['application']} is creative, well-reasoned, and demonstrates the structure's practical utility.",
            "The discussion of generalizations and future directions shows critical thinking and awareness of the structure's broader implications in mathematics and its applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
