class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Interpret the following legal scenario and provide a reasoned argument for the plaintiff's position based on contract law principles. Scenario: Alice entered into a contract with Bob to buy a car for $10,000. Bob delivered the car, but Alice refused to pay, claiming that the car was not as described. Provide an argument for why Alice should be held liable for the payment.", "response_format": "Argument for Plaintiff:\n1. [First point]\n2. [Second point]\n3. [Third point]"},
            "2": {"prompt": "Interpret the following legal scenario and provide a reasoned argument for the defendant's position based on tort law principles. Scenario: Carol slipped and fell in Dave's grocery store, sustaining injuries. Carol claims that the store was negligent in maintaining safe conditions. Provide an argument for why Dave should not be held liable for Carol's injuries.", "response_format": "Argument for Defendant:\n1. [First point]\n2. [Second point]\n3. [Third point]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to {t['prompt']}

Provide your response in the following format:\n{t['response_format']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'contract law principles' in instructions:
            criteria = [
                "The argument should correctly interpret contract law principles.",
                "The argument should provide a logical and coherent reasoning.",
                "The argument should address the scenario details.",
                "The argument should be structured and clear."
            ]
        elif 'tort law principles' in instructions:
            criteria = [
                "The argument should correctly interpret tort law principles.",
                "The argument should provide a logical and coherent reasoning.",
                "The argument should address the scenario details.",
                "The argument should be structured and clear."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
