class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'puzzle': 'You meet two inhabitants: A and B. A says, "We are both knaves." B says nothing. Determine the identities of A and B.'},
            '2': {'puzzle': 'You meet three inhabitants: A, B, and C. A says, "I am a knight." B says, "A is a knave." C says, "A is a knight." Determine the identities of A, B, and C.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logic puzzle involving knights (who always tell the truth) and knaves (who always lie). Use logical deduction to determine the identities of the inhabitants based on their statements.

Puzzle: {t['puzzle']}

Provide your solution in plain text format, clearly stating the identity of each inhabitant as either a knight or a knave. Use the following format:
A: [knight/knave]
B: [knight/knave]
C: [knight/knave] (if applicable)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The solution should correctly identify the identity of each inhabitant as either a knight or a knave.',
            'The solution should be logically consistent with the given statements and the identities should not contradict each other.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
