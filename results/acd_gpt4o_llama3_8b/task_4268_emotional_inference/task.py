class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "John walked into the room and saw his friends all gathered around a table, whispering and glancing at him occasionally. He noticed a wrapped gift on the table."
            },
            "2": {
                "scenario": "Emily received a message from her boss late at night, asking her to come in early the next day for an urgent meeting. She had noticed her boss seemed anxious during their last conversation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following social scenario and infer the emotional states and intentions of the characters involved. Provide a detailed explanation supporting your inferences.

Scenario: {t['scenario']}

Your response should include:
1. The inferred emotional state of each character.
2. The inferred intentions of each character.
3. A detailed explanation supporting your inferences based on the given scenario.

Submit your response as a plain text string in the following format:

Emotional States:
- [Character]: [Inferred emotional state]

Intentions:
- [Character]: [Inferred intention]

Explanation: [Your detailed explanation]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include plausible emotional states for each character.",
            "The response should include plausible intentions for each character.",
            "The explanation should be detailed and logically supported by the given scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
