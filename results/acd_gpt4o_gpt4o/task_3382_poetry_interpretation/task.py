class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "The woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep."},
            "2": {"poem": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given poem. You should analyze the themes, emotions, and literary devices used in the poem. Provide a coherent and insightful analysis that demonstrates a deep understanding of the poem's content.

Poem:
{t['poem']}

Provide your interpretation in plain text format. Ensure that your response is detailed and covers all the mentioned aspects of the analysis."

Response Format:
Interpretation: [Your detailed interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should accurately reflect the themes of the poem.",
            "The analysis should identify and explain the emotions conveyed in the poem.",
            "The literary devices used in the poem should be correctly identified and analyzed.",
            "The interpretation should be coherent, insightful, and well-written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
