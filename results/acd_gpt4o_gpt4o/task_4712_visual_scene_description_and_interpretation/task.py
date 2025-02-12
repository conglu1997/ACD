class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scene": "A busy marketplace with various stalls, people shopping, and a child holding a balloon."},
            "2": {"scene": "A serene beach at sunset with waves gently crashing, a couple walking hand in hand, and a sailboat in the distance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe and interpret the following visual scene based on the textual description provided:

Scene: {t['scene']}

Provide your response in plain text format, including the following elements:
1. A detailed description of the scene, mentioning key elements and their relationships.
2. An interpretation of the possible emotions, actions, or themes depicted in the scene.

Format your response as follows:

Description: [Your detailed description]
Interpretation: [Your interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a detailed and accurate description of the scene.",
            "The response should include an insightful interpretation of the emotions, actions, or themes depicted in the scene.",
            "The description should mention key elements and their relationships in the scene.",
            "The interpretation should be coherent and relevant to the scene described."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
