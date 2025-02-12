class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"words": ["apple", "puzzle", "engineer"], "example_clue": "A fruit that keeps the doctor away (5 letters)"},
            "2": {"words": ["ocean", "mystery", "painter"], "example_clue": "A large body of salt water (5 letters)"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        words = ", ".join(t["words"])
        example_clue = t["example_clue"]
        instructions = f"""Your task is to perform two activities related to crossword puzzles.

1. Generate creative and solvable crossword clues for the following words:
Words: {words}

Example Clue: {example_clue}

Please provide your clues in the following format:
- Word: [Given word]
- Clue: [Your clue]

2. Solve the following crossword clue and provide the answer:
Example Clue: {example_clue}

Ensure that your generated clues are creative, clear, and logically lead to the given words. Provide the answer to the example clue in plain text format as follows:
- Answer: [Your answer]

Your response should include both the generated clues and the answer to the example clue."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated clues should be creative, clear, and logically lead to the given words.",
            "The answer to the example clue should be accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
