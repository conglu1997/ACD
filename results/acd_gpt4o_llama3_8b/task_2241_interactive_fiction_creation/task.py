class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A young prince discovers a hidden passage in the castle leading to an ancient library.", "continuation": ""},
            "2": {"prompt": "A group of explorers find a mysterious island that is not on any map.", "continuation": ""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a continuation of the following story prompt. Ensure the continuation is engaging, coherent, and maintains the narrative style of the prompt.

Story Prompt: {t["prompt"]}

Submit your continuation as a plain text string in the following format:

Continuation:
[Your story continuation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The continuation should be engaging.",
            "The continuation should be coherent.",
            "The continuation should maintain the narrative style of the prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
