class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate", "concept": "prime numbers"},
            "2": {"type": "solve", "riddle": "I am a two-digit number. I am the product of two primes and the sum of my digits is 10. What number am I?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'generate':
            return f"Your task is to create a riddle based on the following mathematical concept: {t['concept']}. Ensure that the riddle is clear, engaging, and solvable. The riddle should be between 20 to 50 words in length. Avoid giving direct hints or solutions within the riddle. Provide your riddle in plain text format."
        elif t['type'] == 'solve':
            return f"Your task is to solve the following riddle: {t['riddle']}. Provide your answer in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'generate':
            criteria = ["The riddle should be clear and based on the given mathematical concept.", "The riddle should be engaging and solvable.", "The riddle should be between 20 to 50 words in length.", "The riddle should not give away direct hints or solutions."]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        elif t['type'] == 'solve':
            correct_answer = "25"
            return 1.0 if submission.strip() == correct_answer else 0.0
