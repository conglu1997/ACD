class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Convert the following active sentences to passive voice: 'The cat chased the mouse.', 'The chef cooked a delicious meal.' Additionally, convert the following direct speech to reported speech: 'She said, \"I am reading a book.\"', 'John exclaimed, \"I won the lottery!\"'"},
            "2": {"description": "Convert the following passive sentences to active voice: 'The book was read by Mary.', 'The cake was baked by John.' Additionally, convert the following reported speech to direct speech: 'She said that she was reading a book.', 'John exclaimed that he had won the lottery.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following sentences as instructed. Provide your transformed sentences in plain text format:

{t['description']}

Format: [Transformed Sentence 1], [Transformed Sentence 2], [Transformed Sentence 3], [Transformed Sentence 4]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The transformed sentences should be syntactically correct and accurately reflect the intended transformation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
