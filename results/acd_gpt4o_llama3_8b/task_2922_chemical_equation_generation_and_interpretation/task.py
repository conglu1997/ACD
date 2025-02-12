class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Generate a balanced chemical equation for the combustion of propane (C3H8) in oxygen (O2) to form carbon dioxide (CO2) and water (H2O)."},
            "2": {"chemical_equation": "C3H8 + 5O2 -> 3CO2 + 4H2O", "question": "If 2 moles of propane (C3H8) are completely combusted, how many moles of carbon dioxide (CO2) are produced?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "description" in t:
            return f"""Generate a balanced chemical equation based on the following description: {t['description']}. Ensure the equation is balanced and follows the law of conservation of mass. Submit your equation as a plain text string in the format:

Balanced Chemical Equation: [Your equation]"""
        else:
            return f"""Interpret the following chemical equation and answer the accompanying question:

Chemical Equation: {t['chemical_equation']}

Question: {t['question']}

Ensure your answer is precise, based on the given chemical equation, and clearly addresses the question. Submit your answer as a plain text string in the format:

Answer: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "description" in t:
            criteria = ["The chemical equation should be balanced.", "The equation should follow the law of conservation of mass."]
        else:
            criteria = ["The answer should be precise and based on the provided chemical equation.", "The answer should clearly address the question of moles of carbon dioxide produced."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
