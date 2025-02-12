class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "equation": "H2 + O2 -> H2O"
            },
            "2": {
                "equation": "C3H8 + O2 -> CO2 + H2O"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        equation = t["equation"]
        instructions = f"""Your task is to balance the following chemical equation. Ensure that the number of atoms for each element is equal on both the reactant and product sides.

Chemical Equation:
{equation}

Submit your balanced equation in the format: Reactants -> Products
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The balanced equation must have the same number of each type of atom on both sides.",
            "The format must be 'Reactants -> Products'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
