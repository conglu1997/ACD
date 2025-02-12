import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "atomic_number": 119,
                "block": "s",
                "group": 1
            },
            {
                "atomic_number": 126,
                "block": "p",
                "group": 16
            },
            {
                "atomic_number": 134,
                "block": "d",
                "group": 4
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fictional element that would occupy the position of atomic number {t['atomic_number']} in an extended periodic table. This element would be in the {t['block']}-block and group {t['group']}.

Your task is to:

1. Name the element and provide its chemical symbol (2-3 letter abbreviation).

2. Describe its expected physical properties (appearance, state of matter at room temperature, density, etc.) based on its position in the periodic table (3-4 sentences).

3. Predict its electronic configuration and explain how this influences its chemical behavior (2-3 sentences).

4. Propose a unique chemical reaction or compound involving this element, explaining the scientific reasoning behind it (3-4 sentences).

5. Describe a potential practical application for this element or its compounds, considering its properties (2-3 sentences).

6. Create a simple ASCII art representation of the element's atomic structure, showing protons, neutrons, and electron shells.

Ensure your response is creative yet grounded in scientific principles and periodic table trends. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The element must have atomic number {t['atomic_number']} and be in the {t['block']}-block and group {t['group']}",
            "The name and chemical symbol should be unique and appropriate",
            "Physical properties should be consistent with periodic table trends",
            "Electronic configuration and chemical behavior should be scientifically plausible",
            "The proposed chemical reaction or compound should be creative yet scientifically grounded",
            "The practical application should be innovative and relate to the element's properties",
            "The ASCII art should represent the atomic structure accurately",
            "The response should be well-organized with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
