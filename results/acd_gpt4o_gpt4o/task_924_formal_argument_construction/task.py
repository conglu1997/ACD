class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["All humans are mortal.", "Socrates is a human.", "All mortals eventually die."]},
            "2": {"premises": ["If it rains, the ground gets wet.", "It is raining.", "Wet ground can be slippery."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        premises = t["premises"]
        instructions = f"""Your task is to construct a formal argument based on the given premises. Ensure that your argument is logically coherent and that the conclusion follows necessarily from the premises.

Premises:
"""
        for premise in premises:
            instructions += f"- {premise}\n"
        instructions += "\nProvide a detailed explanation of your argument, including the logical steps that lead from the premises to the conclusion. Your response should be in the following format:\n\nConclusion: [Your conclusion]\nExplanation: [Detailed explanation of the logical steps]\n\nEnsure that your response is clear, logical, and well-structured."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be logically coherent.",
            "The conclusion should follow necessarily from the premises.",
            "The explanation should be clear and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
