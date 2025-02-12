class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "nature",
                "example": "Write a poem about the beauty of nature."
            },
            "2": {
                "theme": "love",
                "example": "Write a poem about the feeling of love."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a poem based on the following theme: '{t['theme']}'. Your poem should be between 10 to 20 lines. After writing the poem, explain the poetic devices you used, such as metaphors, similes, alliteration, etc., and how they contribute to the overall meaning and impact of the poem.

Submit your response in the following format:

Poem:
[Your poem here]

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The poem should be relevant to the given theme.",
            "The explanation should clearly identify and describe the poetic devices used.",
            "The poetic devices should contribute to the overall meaning and impact of the poem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
