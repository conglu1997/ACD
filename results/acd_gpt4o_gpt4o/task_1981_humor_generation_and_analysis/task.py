class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "technology",
                "type": "pun"
            },
            "2": {
                "theme": "animals",
                "type": "knock-knock"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        type_ = t["type"]
        instructions = f"""Your task is to generate a joke based on the given theme and type.

Theme: {theme}
Type: {type_}

Your response should include:
1. A joke that aligns with the given theme and type.
2. An explanation of why the joke is humorous, including any wordplay, cultural references, or context that contributes to the humor.

Provide your response in plain text format, structured as follows:

Joke: [Your joke]
Explanation: [Your explanation of why the joke is humorous]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The joke should align with the given theme and type.",
            "The explanation should appropriately describe why the joke is humorous.",
            "The response should be structured as 'Joke: [Your joke]' and 'Explanation: [Your explanation of why the joke is humorous]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
