class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            "ocean currents",
            "atmospheric turbulence",
            "blood flow in the heart",
            "magma convection in Earth's mantle",
            "air flow around an airplane wing"
        ]
        import random
        selected = random.sample(phenomena, 2)
        return {
            "1": {"phenomenon": selected[0]},
            "2": {"phenomenon": selected[1]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language based on principles of fluid dynamics, then use it to describe the phenomenon of {t['phenomenon']}. Finally, analyze how using this language might impact cognition and problem-solving in related fields.

        Fluid dynamics is the study of how fluids (liquids and gases) move and interact under various forces and conditions. It involves concepts such as flow, pressure, viscosity, and turbulence.

        Complete the following tasks:

        1. Fluid Dynamics Language Design (250-300 words):
           a) Create a basic structure for your fluid dynamics-based language, including:
              - A system for representing fluid properties (e.g., velocity, pressure, viscosity)
              - A method for describing fluid behavior and interactions
              - At least one unique linguistic feature inspired by a specific fluid dynamics concept
           b) Explain the rationale behind your language design, drawing from both linguistics and fluid dynamics.
           c) Provide a small lexicon (5-7 terms) of basic fluid dynamics concepts in your language, with explanations.
           d) Include an example sentence or phrase in your designed language, along with its translation and explanation.

        2. Phenomenon Description (200-250 words):
           a) Use your fluid dynamics language to describe the given phenomenon ({t['phenomenon']}).
           b) Provide a detailed explanation of your description, including how different aspects of the phenomenon are represented.
           c) Discuss how your language captures nuances of fluid behavior that might be difficult to express in natural languages.

        3. Cognitive Impact Analysis (200-250 words):
           a) Hypothesize how using this fluid dynamics-based language might affect cognition and problem-solving in related scientific fields.
           b) Discuss potential advantages or challenges in understanding and describing fluid systems using your language compared to traditional scientific language.
           c) Propose a specific experiment to test whether using your language improves problem-solving or conceptual understanding in a fluid dynamics-related task.

        4. Interdisciplinary Applications (150-200 words):
           a) Suggest two potential applications of your fluid dynamics language in fields other than physics or engineering.
           b) Explain how the unique features of your language might provide new insights or approaches in these fields.

        Ensure your response demonstrates a deep understanding of both fluid dynamics and linguistics. Be creative in your language design while maintaining scientific accuracy. Use appropriate technical terminology from both fields and provide clear explanations of your reasoning throughout.

        Format your response with clear headings for each section and number your answers according to the structure provided. Your total response should be between 800-1000 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of fluid dynamics principles and linguistic structures.",
            "The designed language effectively incorporates fluid dynamics concepts and provides a unique way to describe fluid phenomena.",
            "The language design includes an example sentence or phrase with translation and explanation.",
            "The phenomenon description using the new language is coherent and captures the complexity of fluid behavior.",
            "The cognitive impact analysis provides insightful hypotheses and a well-designed experiment proposal.",
            "The interdisciplinary applications are creative and well-explained.",
            "The overall response is well-structured, coherent, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
