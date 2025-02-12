import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                'concept': 'free will',
                'language': 'Python',
                'paradigm': 'object-oriented'
            },
            {
                'concept': 'determinism',
                'language': 'Haskell',
                'paradigm': 'functional'
            },
            {
                'concept': 'emergent complexity',
                'language': 'Rust',
                'paradigm': 'systems'
            },
            {
                'concept': 'dualism',
                'language': 'Prolog',
                'paradigm': 'logic'
            }
        ]
        selected_concepts = random.sample(concepts, 2)
        return {str(i+1): concept for i, concept in enumerate(selected_concepts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the abstract philosophical concept of '{t['concept']}' into functional code using {t['language']} and adhering to the {t['paradigm']} programming paradigm. Your response should include:

1. Conceptual Analysis (200-250 words):
   a) Define and explain the philosophical concept of {t['concept']}.
   b) Identify key aspects or properties of this concept that could be represented in code.
   c) Discuss any challenges in translating this abstract idea into a concrete implementation.
   d) Cite at least one relevant philosophical source to support your analysis.

2. System Architecture (250-300 words):
   a) Describe the main components of your translation system.
   b) Explain how these components interact to process the concept and generate code.
   c) Discuss how your system incorporates principles from cognitive science and linguistics.
   d) Provide a high-level pseudocode or flowchart of your system's operation.
   e) Reference at least one relevant computer science or cognitive science paper that informs your design.

3. Code Generation (300-350 words):
   a) Present a sample of generated {t['language']} code that represents the concept of {t['concept']}.
   b) Explain how your code captures the essence of the philosophical idea.
   c) Describe how your implementation adheres to the {t['paradigm']} paradigm.
   d) Discuss any trade-offs or limitations in your representation.

4. Evaluation Method (150-200 words):
   a) Propose a method to evaluate the accuracy and effectiveness of your concept-to-code translation.
   b) Describe potential metrics or criteria for assessing the quality of the generated code.
   c) Suggest how you might validate that the code truly represents the original concept.

5. Potential Applications and Ethical Implications (200-250 words):
   a) Discuss potential applications of your concept-to-code translation system in fields such as AI ethics, cognitive modeling, or computer-assisted philosophy.
   b) Propose an innovative use case that combines philosophical inquiry with practical software development.
   c) Analyze potential ethical implications or concerns arising from translating philosophical concepts into code, and suggest ways to address these issues.

Ensure your response demonstrates a deep understanding of philosophy, cognitive science, linguistics, and computer science. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and philosophical rigor.

Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the philosophical concept of {t['concept']} and its translation into code.",
            f"The system architecture and code generation process are well-explained and appropriate for {t['language']} and the {t['paradigm']} paradigm.",
            "The generated code sample effectively represents the philosophical concept while adhering to the specified programming paradigm.",
            "The evaluation method and potential applications are innovative and well-reasoned.",
            "The response shows interdisciplinary knowledge integration across philosophy, cognitive science, linguistics, and computer science.",
            "The response includes relevant citations to philosophical and computer science literature.",
            "The ethical implications of translating philosophical concepts into code are thoughtfully analyzed.",
            "The total word count falls within the specified range of 1100-1350 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
