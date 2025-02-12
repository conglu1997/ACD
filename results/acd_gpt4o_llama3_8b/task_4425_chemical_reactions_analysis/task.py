class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "reaction": "Combustion of methane",
                "reactants": "CH4 + 2 O2",
                "products": "CO2 + 2 H2O"
            },
            "2": {
                "reaction": "Neutralization of hydrochloric acid with sodium hydroxide",
                "reactants": "HCl + NaOH",
                "products": "NaCl + H2O"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following chemical reaction, analyze and explain the reaction in detail. Your response should include:

1. A balanced chemical equation for the reaction.
2. The type of reaction (e.g., combustion, neutralization, etc.).
3. The reactants involved and their roles in the reaction.
4. The products formed and their significance.
5. The conditions required for the reaction to occur (e.g., temperature, pressure, catalysts).
6. Any relevant safety considerations or hazards associated with the reaction.

Submit your response as a plain text string in the following format:

Reaction: {t['reaction']}

Balanced Equation: [Your balanced equation]
Type of Reaction: [Your analysis]
Reactants: [Your analysis]
Products: [Your analysis]
Conditions: [Your analysis]
Safety Considerations: [Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a balanced chemical equation for the reaction.",
            "The response should correctly identify the type of reaction.",
            "The response should accurately describe the reactants and their roles.",
            "The response should accurately describe the products and their significance.",
            "The response should specify the conditions required for the reaction to occur.",
            "The response should include any relevant safety considerations or hazards."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0