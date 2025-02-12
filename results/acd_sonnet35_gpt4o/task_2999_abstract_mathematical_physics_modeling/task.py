import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        physics_areas = [
            ("Quantum Field Theory", "General Relativity"),
            ("String Theory", "Loop Quantum Gravity"),
            ("Quantum Mechanics", "Thermodynamics"),
            ("Electromagnetism", "Nuclear Forces")
        ]
        algebraic_structures = [
            "Lie Groups",
            "Clifford Algebras",
            "Category Theory",
            "Hopf Algebras"
        ]
        tasks = {}
        for i in range(2):
            areas = random.choice(physics_areas)
            structure = random.choice(algebraic_structures)
            tasks[str(i+1)] = {
                "area1": areas[0],
                "area2": areas[1],
                "structure": structure
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a mathematical model that unifies {t['area1']} and {t['area2']} using the abstract algebraic structure of {t['structure']}. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Briefly explain the key concepts in {t['area1']} and {t['area2']}.
   b) Describe the fundamental properties of {t['structure']}.
   c) Propose a high-level approach for using {t['structure']} to unify these areas.

2. Mathematical Formulation (300-350 words):
   a) Present the core mathematical equations of your unified model.
   b) Explain how your formulation incorporates key aspects of both {t['area1']} and {t['area2']}.
   c) Describe how {t['structure']} is utilized in your mathematical framework.

3. Physical Implications (200-250 words):
   a) Discuss the physical meaning of your unified model.
   b) Explain how it resolves or sheds new light on existing problems in {t['area1']} or {t['area2']}.
   c) Propose a novel prediction or insight arising from your unification.

4. Mathematical Proof or Argument (200-250 words):
   a) Provide a sketch of a mathematical proof or argument for a key result in your model.
   b) Explain the logical steps and any assumptions made.

5. Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations or challenges in your approach.
   b) Suggest areas for future research or expansion of your model.

Ensure your response demonstrates a deep understanding of the relevant areas of physics and mathematics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and mathematical rigor.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the unification of {t['area1']} and {t['area2']} using {t['structure']}",
            "The mathematical formulation should be logically consistent and relevant to the chosen physics areas",
            "The response should demonstrate a deep understanding of the chosen algebraic structure and its applicability to the physics areas",
            "The physical implications and novel predictions should be plausible and insightful",
            "The mathematical proof or argument should be logically sound and relevant to the proposed model",
            "The response should show creativity and original thinking in approaching the unification problem",
            "The limitations and future directions should be thoughtfully considered and relevant to the proposed model"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
