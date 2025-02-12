class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a poem about the changing seasons.",
                "title": "Seasons Poem"
            },
            "2": {
                "prompt": "Write a poem that explores the theme of solitude.",
                "title": "Solitude Poem"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        title = t["title"]
        instructions = f"""Your task is to compose a poem based on the following prompt.

Title: {title}
Prompt: {prompt}

Your response should include:
1. A poem that aligns with the given prompt.
2. The poem should demonstrate creativity, emotional depth, and linguistic artistry.

Provide your response in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should align with the given prompt.",
            "The poem should demonstrate creativity, emotional depth, and linguistic artistry."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
