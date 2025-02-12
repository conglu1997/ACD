class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "animals", "structure": "knock-knock"},
            "2": {"theme": "technology", "structure": "one-liner"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['structure'] == 'knock-knock':
            return f"""Your task is to create a 'knock-knock' joke based on the theme '{t['theme']}'.

A 'knock-knock' joke follows this structure:

Knock, knock.
Who's there?
[Setup]
[Setup] who?
[Punchline]

Ensure your joke is creative, coherent, and fits the given theme. Format your response in plain text as follows:

Knock, knock.
Who's there?
[Setup]
[Setup] who?
[Punchline]"""
        elif t['structure'] == 'one-liner':
            return f"""Your task is to create a one-liner joke based on the theme '{t['theme']}'.

A one-liner joke is a concise and witty remark or observation, usually delivered in a single sentence.

Ensure your joke is creative, coherent, and fits the given theme. Format your response in plain text as follows:

[Joke]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['structure'] == 'knock-knock':
            criteria = [
                "The joke should be a 'knock-knock' joke.",
                "The joke should follow the 'knock-knock' structure.",
                "The joke should be based on the theme of animals.",
                "The joke should be creative and coherent."
            ]
        elif t['structure'] == 'one-liner':
            criteria = [
                "The joke should be a one-liner.",
                "The joke should be based on the theme of technology.",
                "The joke should be creative and coherent."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
