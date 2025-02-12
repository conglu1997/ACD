class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate a humorous short story that involves a misunderstanding between two characters in a workplace setting."},
            "2": {"prompt": "Generate a joke that uses a pun based on the concept of time."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["prompt"].startswith("Generate a humorous short story"):
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the short story adheres to the following requirements:
1. The story should be humorous and involve a clear misunderstanding between two characters in a workplace setting.
2. The humor should be appropriate and understandable without requiring extensive cultural knowledge.
3. The story should be engaging and coherent, with a clear beginning, middle, and end.

Submit your response as a plain text string.
"""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the joke adheres to the following requirements:
1. The joke should be based on a pun involving the concept of time.
2. The pun should be clever and elicit a humorous response.
3. The joke should be concise and deliver the punchline effectively.

Submit your response as a plain text string.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["prompt"].startswith("Generate a humorous short story"):
            criteria = ["The story should be humorous and involve a clear misunderstanding between two characters in a workplace setting.", "The humor should be appropriate and understandable without requiring extensive cultural knowledge.", "The story should be engaging and coherent, with a clear beginning, middle, and end."]
        else:
            criteria = ["The joke should be based on a pun involving the concept of time.", "The pun should be clever and elicit a humorous response.", "The joke should be concise and deliver the punchline effectively."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
