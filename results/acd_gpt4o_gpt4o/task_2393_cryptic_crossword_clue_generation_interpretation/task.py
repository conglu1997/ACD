class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"word": "apple", "clue_type": "anagram"},
            "2": {"clue": "One may consume this fruit after a trip (5)", "answer": "peach"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "word" in t:
            return """Your task is to generate a cryptic crossword clue for the given word using the specified clue type.

Word: {0}
Clue Type: {1}

Ensure that your clue is creative, follows the rules of the specified clue type, and provides enough information to deduce the correct word. Your clue should be self-contained and solvable independently. Provide your clue in plain text format.""".format(t["word"], t["clue_type"])
        else:
            return """Your task is to interpret the given cryptic crossword clue and find the correct answer.

Clue: {0}

Ensure that your answer is a single word that fits the clue and the given length. Provide your answer in plain text format.""".format(t["clue"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "word" in t:
            criteria = [
                "The clue should be a valid cryptic crossword clue.",
                "The clue should follow the rules of the specified clue type.",
                "The clue should provide enough information to deduce the correct word.",
                "The clue should be self-contained and solvable independently."
            ]
        else:
            criteria = [f"The answer should be {t['answer']}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
