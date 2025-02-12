class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A friend is feeling down because they did not get a job they really wanted, despite preparing extensively and being confident about their chances."
            },
            "2": {
                "scenario": "Two colleagues are celebrating a successful project completion, where one of them had to overcome significant personal challenges to contribute effectively." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a dialogue based on the following scenario: {t['scenario']}.

Your response should include:
1. A dialogue between two characters where one character is expressing their emotions related to the scenario.
2. Appropriate responses from the other character that show empathy, understanding, and support.
3. Ensure the dialogue feels natural and contextually appropriate.

Submit your response as a plain text string in the following format:

Dialogue:
[Character 1]: [Their emotional expression]
[Character 2]: [Their empathetic response]
[Character 1]: [Their reaction]
[Character 2]: [Further support/encouragement]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue should reflect the emotional scenario presented.",
            "Character 2's responses should show empathy, understanding, and appropriate support.",
            "The dialogue should feel natural and contextually appropriate.",
            "The dialogue should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
