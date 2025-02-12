class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A self-driving car must decide between hitting a pedestrian who suddenly steps into the road, or swerving and potentially harming its passengers. The pedestrian is jaywalking, but the passengers include a child and an elderly person. What should the car do? Explain your decision using ethical principles.",
                "instructions": "Analyze the given ethical dilemma and provide a reasoned decision. Justify your decision based on ethical principles such as utilitarianism, deontology, and virtue ethics. Submit your response as a plain text string with two sections: 'Decision' and 'Justification'."
            },
            "2": {
                "scenario": "A company discovers that its product, which is widely used, has a defect that could potentially cause harm to a small percentage of users. The company must decide whether to issue a costly recall or to continue selling the product with a warning label. The defect has already caused minor injuries to a few users, and the recall would financially strain the company. What should the company do? Explain your decision using ethical principles.",
                "instructions": "Analyze the given ethical dilemma and provide a reasoned decision. Justify your decision based on ethical principles such as utilitarianism, deontology, and virtue ethics. Submit your response as a plain text string with two sections: 'Decision' and 'Justification'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following ethical dilemma and provide a reasoned decision. Justify your decision based on ethical principles such as utilitarianism, deontology, and virtue ethics. Scenario: {t['scenario']} Submit your response as a plain text string with two sections: 'Decision' and 'Justification'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a clear and reasoned decision based on the ethical dilemma.",
            "The justification should reference relevant ethical principles such as utilitarianism, deontology, and virtue ethics.",
            "The explanation should be coherent and logically structured.",
            "The response should consider multiple perspectives and implications of the decision."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
