class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Customer Support",
                "requirements": "Design a chatbot for a company's customer support that can handle common queries about order status, product information, and return policies. The chatbot should be able to escalate issues to a human representative if it cannot resolve the query. Include example dialogues for each type of query, demonstrating how the chatbot handles the interaction and when it decides to escalate."
            },
            "2": {
                "scenario": "Personal Assistant",
                "requirements": "Design a chatbot that acts as a personal assistant, helping users with schedule management, reminders, setting alarms, and providing weather updates. The chatbot should also be able to handle follow-up questions and manage multiple tasks simultaneously. Include example dialogues demonstrating these functionalities and how the chatbot handles follow-up interactions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an interactive dialogue system or chatbot based on the following scenario and requirements:

Scenario: {t['scenario']}

Requirements: {t['requirements']}

Your response should include a description of the chatbot's functionalities, the dialogue flow, and example dialogues that demonstrate how the chatbot handles different types of interactions. Submit your design as a plain text string with the following sections:

1. Functionality Description: [Describe the chatbot's functionalities]
2. Dialogue Flow: [Describe the dialogue flow and how the chatbot handles different interactions]
3. Example Dialogues: [Provide example dialogues demonstrating the chatbot's responses for each type of interaction]

Example Format:

Functionality Description: [Your description here]
Dialogue Flow: [Your dialogue flow here]
Example Dialogues: [Your example dialogues here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The design should meet the specified requirements.",
            "The example dialogues should be coherent and relevant to the scenario.",
            "The dialogue flow should logically handle different types of interactions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
