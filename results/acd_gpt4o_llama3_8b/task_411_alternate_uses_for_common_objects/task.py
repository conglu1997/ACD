class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "object": "paperclip"
            },
            "2": {
                "object": "toothbrush"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate at least five alternate uses for the following common object: {t['object']}. Ensure that each use is practical and creative. Avoid very similar uses and try to think outside the box. Submit your list of uses as a plain text string in the following format:

1. [First use]
2. [Second use]
...
5. [Fifth use]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "Each use should be practical.",
            "Each use should be creative.",
            "Avoid very similar uses."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
