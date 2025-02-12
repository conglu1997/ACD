class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a sonnet about the passage of time."},
            "2": {"prompt": "Analyze the following haiku and discuss its themes and imagery: 'An old silent pond... A frog jumps into the pond— Splash! Silence again.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["prompt"].startswith("Write a sonnet"):
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the sonnet adheres to one of the traditional formats:
1. Shakespearean (ababcdcdefefgg)
2. Petrarchan (abbaabbacdcdcd or abbaabbacdecde)
3. Spenserian (ababbcbccdcdee)

The sonnet should be 14 lines long and written in iambic pentameter. It should effectively explore the theme of the passage of time.

Submit your response as a plain text string."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Provide a detailed analysis of the haiku, discussing its themes, imagery, and the emotions it evokes. Your analysis should include:
1. An explanation of the imagery used
2. The themes conveyed by the haiku
3. The emotions the haiku evokes

Ensure your analysis is coherent and insightful.

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["prompt"].startswith("Write a sonnet"):
            criteria = ["The sonnet should adhere to one of the traditional formats (Shakespearean, Petrarchan, Spenserian).", "The sonnet should be 14 lines long and written in iambic pentameter.", "The sonnet should effectively explore the theme of the passage of time."]
        else:
            criteria = ["The analysis should discuss the themes and imagery of the haiku.", "The analysis should be coherent and insightful.", "The analysis should evoke the emotions conveyed by the haiku."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
