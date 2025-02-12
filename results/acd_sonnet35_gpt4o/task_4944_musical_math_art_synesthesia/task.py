class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            "Fibonacci sequence",
            "Mandelbrot set",
            "Euler's identity",
            "Riemann hypothesis"
        ]
        import random
        selected = random.sample(math_concepts, 2)
        return {
            "1": {"concept": selected[0]},
            "2": {"concept": selected[1]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a system that translates mathematical equations into musical compositions and visual art, then use it to represent the mathematical concept: {t['concept']}. Your task has four parts:

        1. System Design (250-300 words):
           a) Describe your system for translating mathematical equations into music and visual art.
           b) Explain how mathematical properties (e.g., variables, operations, functions) are mapped to musical elements (e.g., pitch, rhythm, harmony) and visual elements (e.g., color, shape, position).
           c) Discuss how your system maintains the logical structure and relationships present in the mathematical equations.

        2. Concept Translation (300-350 words):
           a) Apply your system to translate the given mathematical concept ({t['concept']}) into a musical composition and a piece of visual art.
           b) Describe the resulting musical composition in detail, including its structure, key elements, and how it represents the mathematical concept.
           c) Describe the resulting visual artwork, explaining how its various elements represent different aspects of the mathematical concept.
           d) Explain how the musical and visual representations complement each other in expressing the mathematical concept.

        3. Analysis and Interpretation (200-250 words):
           a) Analyze how your translation captures the essence and complexity of the mathematical concept.
           b) Discuss any insights or new perspectives on the concept that emerge from its musical and visual representations.
           c) Explain how this interdisciplinary approach might enhance understanding or appreciation of the mathematical concept.

        4. Cognitive and Educational Implications (150-200 words):
           a) Discuss how this synesthetic approach to representing mathematical concepts might affect cognitive processes and learning.
           b) Propose an experiment to test the educational effectiveness of your system in teaching complex mathematical concepts.
           c) Suggest potential applications of your system in fields such as mathematics education, data visualization, or artistic creation.

        Ensure your response demonstrates a deep understanding of mathematics, music theory, and visual art principles. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and logical rigor.

        Format your response with clear headings for each section. Your total response should be between 900-1100 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear and creative system for translating mathematical equations into music and visual art.",
            "The translation of the given mathematical concept into music and visual art is detailed, coherent, and logically sound.",
            "The analysis shows insight into how the interdisciplinary representation enhances understanding of the mathematical concept.",
            "The discussion of cognitive and educational implications is thoughtful and includes a well-designed experiment proposal.",
            "The overall response shows a deep understanding of mathematics, music theory, and visual art principles.",
            "The response is well-structured, coherent, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
