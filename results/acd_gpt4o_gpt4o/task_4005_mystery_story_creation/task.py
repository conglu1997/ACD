class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A detective receives an anonymous tip about a hidden treasure buried in an old mansion."},
            "2": {"prompt": "A group of friends discovers a hidden room in their new house that leads to a series of cryptic clues."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a mystery story based on the following prompt:

{t['prompt']}

Your story should include the following elements:
1. A build-up of suspense
2. At least one plot twist
3. A coherent resolution that ties up all loose ends

Ensure your story is engaging and logically consistent. Provide your story in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should include a build-up of suspense.", "The story should have at least one plot twist.", "The story should have a coherent resolution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
