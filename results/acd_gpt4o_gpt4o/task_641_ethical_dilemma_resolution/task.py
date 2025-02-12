class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "You are a doctor with a limited number of life-saving medications. You have to choose between saving a young child or an elderly person. Both have equal chances of recovery."},
            "2": {"dilemma": "You are a train conductor and you see a runaway train heading towards five people tied to the tracks. You can switch the train to another track where there is one person tied. What should you do?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dilemma = t["dilemma"]
        instructions = f"""Your task is to analyze the following ethical dilemma and provide a reasoned resolution:

Dilemma: {dilemma}

Your resolution should be based on established ethical principles such as utilitarianism, deontology, and virtue ethics. Ensure that your response is logical, empathetic, and considers the potential consequences of the decision. Provide your resolution in plain text format with a clear explanation of your reasoning. Structure your response in the following format:

1. Identify and explain the ethical principles relevant to the dilemma.
2. Present your resolution to the dilemma.
3. Justify your resolution with a detailed explanation of your reasoning."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The resolution should identify and explain the relevant ethical principles.",
            "The resolution should be logical and empathetic.",
            "The resolution should consider the potential consequences.",
            "The reasoning should be clearly explained and justified."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
