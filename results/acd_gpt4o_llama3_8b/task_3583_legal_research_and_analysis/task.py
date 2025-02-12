class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A person is accused of theft after being found in possession of stolen goods. The person claims they found the goods abandoned in a public park. Analyze the scenario and provide legal arguments for both the prosecution and defense.", "legal_principles": ["possession", "theft", "burden of proof"]},
            "2": {"scenario": "A company is being sued for breach of contract after failing to deliver goods on time. The company claims that an unforeseen natural disaster prevented timely delivery. Analyze the scenario and provide legal arguments for both the plaintiff and the defendant.", "legal_principles": ["breach of contract", "force majeure", "liability"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following legal scenario: {t['scenario']}. Provide legal arguments for both sides based on the given legal principles: {', '.join(t['legal_principles'])}. Submit your response in the following format:
Prosecution/Plaintiff Argument: [Your argument here]
Defense/Defendant Argument: [Your argument here]

Ensure your arguments are coherent, logically sound, and based on the legal principles provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The arguments must be logically sound and based on the given legal principles.", "Both sides of the argument must be clearly presented."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
