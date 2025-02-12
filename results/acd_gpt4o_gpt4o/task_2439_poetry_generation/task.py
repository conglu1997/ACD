class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "rhyme_scheme": "ABAB",
                "meter": "iambic pentameter",
                "theme": "nature",
                "poetic_device": "alliteration"
            },
            "2": {
                "rhyme_scheme": "AABB",
                "meter": "trochaic tetrameter",
                "theme": "love",
                "poetic_device": "metaphor"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a poem based on the following constraints:

Rhyme Scheme: {t['rhyme_scheme']}
Meter: {t['meter']}
Theme: {t['theme']}
Poetic Device: {t['poetic_device']}

Ensure that your poem adheres to the specified rhyme scheme and meter. The poem should also incorporate the given theme and make effective use of the specified poetic device. Provide your poem in plain text format.

Your response should include:
1. The poem itself
2. A brief explanation of how your poem meets the given constraints.

Format your response as follows:
Poem: [Your poem here]
Explanation: [Your explanation here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the specified rhyme scheme.",
            "The poem should follow the given meter.",
            "The poem should incorporate the theme effectively.",
            "The poem should make use of the specified poetic device."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
