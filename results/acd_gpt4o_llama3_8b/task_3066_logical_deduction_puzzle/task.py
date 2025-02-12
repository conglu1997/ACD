class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "In a family of five members - A, B, C, D, and E - some statements are given: 1. A is the father of C. 2. B is the mother of C. 3. C is the sister of D. 4. E is the brother of A. 5. D is not a male. Who is the uncle of D?",
                "solution": "E"
            },
            "2": {
                "puzzle": "Three friends - Adam, Ben, and Charlie - are sitting in a row. Adam is not next to Ben. Ben is not next to Charlie. Charlie is on the left end. Adam is not on the right end. Who is sitting in the middle?",
                "solution": "Ben"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t['puzzle']
        return f"""Solve the following logical deduction puzzle by inferring the correct answer based on the given constraints and logical rules. Provide your answer as a single word or name.

Puzzle: {puzzle}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should be a single word or name.", f"The response should be: {t['solution']}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
