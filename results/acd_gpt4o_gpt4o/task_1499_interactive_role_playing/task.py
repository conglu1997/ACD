class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"character": "Detective", "scenario": "Investigating a mysterious disappearance at an old mansion."},
            "2": {"character": "Teacher", "scenario": "Helping a student understand a difficult math concept."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to engage in a multi-turn role-playing conversation based on the following character and scenario:

Character: {0}
Scenario: {1}

You should respond as the character in a way that is contextually appropriate and maintains coherence throughout the dialogue. Provide your responses as if you are having a conversation, with each response separated by a newline character. The conversation should have a minimum of 5 exchanges (turns).

Example (different context):
Character: Shopkeeper
Scenario: Helping a customer find a specific item in the store.

Customer: Can you help me find the baking aisle?
Shopkeeper: Certainly! The baking aisle is just around the corner, next to the dairy section. Is there anything specific you're looking for?
Customer: Yes, I need some flour and sugar.
Shopkeeper: You can find the flour on the second shelf and the sugar on the third shelf in the baking aisle.
Customer: Thank you! Also, do you have any baking powder?
Shopkeeper: Yes, the baking powder is on the same shelf as the flour. Anything else I can help you with?
Customer: No, that's all. Thanks for your help!
Shopkeeper: You're welcome! Have a great day!""".format(t["character"], t["scenario"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The responses should be coherent and contextually appropriate.",
            "The responses should maintain the character's role consistently.",
            "The conversation should flow logically and naturally.",
            "The conversation should have a minimum of 5 exchanges (turns)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
