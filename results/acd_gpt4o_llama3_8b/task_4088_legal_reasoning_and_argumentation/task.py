class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Alice is accused of trespassing on private property. She claims that she entered the property to rescue a child who was in imminent danger. The law states that trespassing is illegal, but there is an exception for emergencies where human life is at risk.",
                "law": "Trespassing is defined as entering someone else's property without permission. However, there is an exception for emergencies where human life is at risk."
            },
            "2": {
                "scenario": "Bob is suing a company for breach of contract. The contract states that the company must deliver goods by December 1st. The company delivered the goods on December 3rd, citing unforeseen shipping delays due to a natural disaster. The law includes a force majeure clause that exempts parties from liability if a delay is caused by an extraordinary event beyond their control.",
                "law": "A force majeure clause exempts parties from liability if a delay or failure to perform is caused by an extraordinary event beyond their control, such as natural disasters, wars, or strikes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following legal scenario and provide a legal argument or solution based on the given law:

Scenario: {t["scenario"]}

Law: {t["law"]}

Your response should demonstrate a clear understanding of the legal principles involved and provide a well-reasoned argument or solution. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should demonstrate a clear understanding of the legal principles involved.",
            "The response should provide a well-reasoned argument or solution based on the given law."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
