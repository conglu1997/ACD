class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon1": "Center-embedding in English sentences",
                "phenomenon2": "Crossed dependencies in Dutch subordinate clauses",
                "formal_concept": "Context-free grammars and mildly context-sensitive grammars"
            },
            "2": {
                "phenomenon1": "Tonal patterns in Mandarin Chinese",
                "phenomenon2": "Vowel harmony in Turkish",
                "formal_concept": "Finite-state transducers and two-level morphology"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and compare the linguistic phenomena of {t['phenomenon1']} and {t['phenomenon2']} using the formal language theory concepts of {t['formal_concept']}. Your analysis should include:

1. Phenomenon Description (200-250 words):
   - Explain both linguistic phenomena, including examples and cross-linguistic comparisons.
   - Highlight key similarities and differences between the two phenomena.

2. Formal Concepts (200-250 words):
   - Describe the relevant formal language theory concepts, their relationships, and key properties.
   - Explain why these concepts are appropriate for analyzing the given phenomena.

3. Formal Analysis (300-350 words):
   - Apply the formal concepts to model or explain both linguistic phenomena.
   - Compare and contrast how well the formal concepts capture each phenomenon.
   - Discuss limitations, challenges, or alternative approaches in this analysis.

4. Formal Representation:
   - Provide a formal representation (e.g., grammar rules, automaton descriptions, or mathematical formulas) for each phenomenon.
   - Explain your representations and how they capture key aspects of each phenomenon.

5. Novel Application (200-250 words):
   - Propose an innovative application that leverages your comparative analysis in natural language processing, linguistic research, or another field of your choice.
   - Describe how it could be implemented and its potential impact.
   - Explain how your application benefits from the comparative approach.

Ensure your response demonstrates a deep understanding of linguistics, formal language theory, and their interdisciplinary applications. Use technical terminology appropriately and provide explanations where necessary. Be creative in your analysis and proposed application while maintaining scientific rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides detailed and accurate explanations of both linguistic phenomena and the formal language theory concepts, including relevant examples and comparisons.",
            "The analysis effectively applies the formal concepts to both linguistic phenomena, thoroughly comparing and contrasting their applicability, and discussing limitations and challenges.",
            "Valid and well-explained formal representations are provided for both phenomena, accurately capturing their key aspects.",
            "The proposed novel application is creative, feasible, and clearly demonstrates how it benefits from the comparative analysis.",
            "The response adheres to the specified word count ranges for each section and demonstrates a sophisticated understanding of linguistics, formal language theory, and their interdisciplinary applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
