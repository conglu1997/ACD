class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Nature", "constraints": "The poem should be a sonnet (14 lines) with an ABABCDCDEFEFGG rhyme scheme."},
            "2": {"theme": "Love", "constraints": "The poem should consist of three quatrains followed by a couplet, each quatrain with an ABAB rhyme scheme and the couplet with an AA rhyme scheme."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a poem based on the following theme and constraints:

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure that the poem is coherent, adheres to the specified structure, and reflects the given theme. The poem should strictly follow the given rhyme scheme and structure. Submit your poem as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The poem should strictly follow the rhyme scheme and structure specified in the constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
