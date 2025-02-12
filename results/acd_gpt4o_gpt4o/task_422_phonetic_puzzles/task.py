class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Which word, when pronounced, sounds like 'you' but is not 'you'?"},
            "2": {"puzzle": "Rearrange the sounds in the word 'stop' to form a new word that is a place for learning."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following phonetic puzzle: {t['puzzle']}. Provide your answer as a single word in plain text format. Ensure that the word is spelled correctly, fits the phonetic criteria described in the puzzle, and is relevant to the context provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["puzzle"] == "Which word, when pronounced, sounds like 'you' but is not 'you'?":
            criteria = ["The word should sound like 'you' but not be 'you'.", "The answer should be provided as a single word.", "The word should be spelled correctly.", "The word should be relevant to the context of the puzzle."]
        elif t["puzzle"] == "Rearrange the sounds in the word 'stop' to form a new word that is a place for learning.":
            criteria = ["The new word should be a place for learning.", "The word should be formed by rearranging the sounds of 'stop'.", "The answer should be provided as a single word.", "The word should be spelled correctly.", "The word should be relevant to the context of the puzzle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
