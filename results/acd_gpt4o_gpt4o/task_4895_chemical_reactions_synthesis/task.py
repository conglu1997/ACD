class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Predict the outcome of the following chemical reaction and provide a balanced chemical equation:\n\nC2H4 + H2 -> ?"},
            "2": {"prompt": "Design a chemical reaction to produce water (H2O) from hydrogen (H2) and oxygen (O2). Provide the balanced chemical equation, any necessary conditions for the reaction to occur, and a brief discussion of the reaction mechanism."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves predicting the outcomes of chemical reactions and designing new chemical reactions:\n\nPrompt: {t['prompt']}\n\nFor Task 1: Predict the outcome of the given chemical reaction and provide a balanced chemical equation. Clearly show the reactants, products, and any necessary conditions for the reaction to occur.\n\nResponse Format:\nReactants: [List of reactants]\nProducts: [List of products]\nBalanced Equation: [Balanced chemical equation]\nConditions: [Any necessary conditions]\n\nFor Task 2: Design a chemical reaction to produce water (H2O) from hydrogen (H2) and oxygen (O2). Provide the balanced chemical equation, any necessary conditions for the reaction to occur, and a brief discussion of the reaction mechanism.\n\nResponse Format:\nReactants: [List of reactants]\nProducts: [List of products]\nBalanced Equation: [Balanced chemical equation]\nConditions: [Any necessary conditions]\nMechanism: [Brief discussion of the reaction mechanism]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The predicted outcome for Task 1 should be chemically accurate and the equation should be balanced.", "The designed reaction for Task 2 should correctly produce water (H2O) from hydrogen (H2) and oxygen (O2), with a balanced chemical equation and any necessary conditions clearly stated, along with a brief discussion of the reaction mechanism."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
