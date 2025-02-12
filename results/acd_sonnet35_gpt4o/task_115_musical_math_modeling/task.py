class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "musical_structure": "12-bar blues progression",
                "mathematical_concept": "Cyclic group theory"
            },
            "2": {
                "musical_structure": "Fibonacci sequence in musical composition",
                "mathematical_concept": "Golden ratio and recursive sequences"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the musical structure of {t['musical_structure']} using the mathematical concept of {t['mathematical_concept']}. Your analysis should include:

1. Musical Structure Description (150-200 words):
   - Explain the chosen musical structure, including its key components and significance in music theory.
   - Provide a specific example of how this structure is used in a well-known musical piece.

2. Mathematical Concept Overview (150-200 words):
   - Describe the relevant mathematical concept and its key properties.
   - Explain why this concept is appropriate for analyzing the given musical structure.

3. Mathematical Model (250-300 words):
   - Develop a mathematical model that represents the musical structure using the given mathematical concept.
   - Explain how your model captures the essential features of the musical structure.
   - Provide at least one equation or formal representation of your model.

4. Analysis of Model Properties (200-250 words):
   - Analyze the properties of your mathematical model.
   - Discuss how these properties relate to musical characteristics or phenomena.
   - Identify any limitations or assumptions in your model.

5. Creative Application (200-250 words):
   - Propose a novel application of your mathematical model in music composition, analysis, or technology.
   - Explain how this application could benefit musicians, composers, or music theorists.
   - Describe a potential experiment or prototype that could test your application.

Ensure your response demonstrates a deep understanding of both music theory and mathematics, and their interdisciplinary applications. Use technical terminology appropriately and provide explanations where necessary. Be creative in your analysis and proposed application while maintaining scientific rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides accurate and detailed explanations of both the musical structure and the mathematical concept, including relevant examples and key properties.",
            "The mathematical model effectively represents the musical structure, with clear explanations and at least one formal equation or representation.",
            "The analysis of model properties demonstrates a deep understanding of both mathematical and musical concepts, including a discussion of limitations or assumptions.",
            "The proposed creative application is innovative, feasible, and clearly demonstrates how it could benefit the field of music.",
            "The response adheres to the specified word count ranges for each section and demonstrates a sophisticated understanding of music theory, mathematics, and their interdisciplinary applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
