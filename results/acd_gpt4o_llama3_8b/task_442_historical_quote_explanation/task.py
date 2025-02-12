class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"quote": "Give me liberty, or give me death!"},
            "2": {"quote": "The only thing we have to fear is fear itself."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following historical quote:

{t["quote"]}

Your explanation should include the following points:
1. The context of the quote.
2. Who said it.
3. The significance at the time it was said.
4. Its lasting impact or relevance.

Submit your response as a plain text string in the following format:

Quote: [The quote]
Context: [Your explanation of the context]
Speaker: [The person who said it]
Significance: [The significance at the time]
Impact: [The lasting impact or relevance]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should include the context of the quote.", "The explanation should identify who said the quote.", "The explanation should discuss the significance of the quote at the time it was said.", "The explanation should cover the lasting impact or relevance of the quote."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
