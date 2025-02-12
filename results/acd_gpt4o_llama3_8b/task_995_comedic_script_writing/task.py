class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Two friends are stuck in an elevator.",
                "characters": "Friend 1, Friend 2"
            },
            "2": {
                "scenario": "A customer tries to return a used item to a store.",
                "characters": "Customer, Store Clerk"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a short comedic script based on the following scenario and characters:

Scenario: {t['scenario']}
Characters: {t['characters']}

Ensure that the script is at least 200 words long and includes at least three humorous elements, such as puns, witty remarks, or situational comedy. Submit your script as a plain text string in the following format:

[Character 1]: [Dialogue]
[Character 2]: [Dialogue]
[Character 1]: [Dialogue]
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The script should be at least 200 words long.",
            "The script should include at least three humorous elements, such as puns, witty remarks, or situational comedy.",
            "The script should follow the given scenario and characters."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
