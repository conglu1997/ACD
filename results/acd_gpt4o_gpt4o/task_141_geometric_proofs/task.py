class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "Prove that the sum of the interior angles of a triangle is 180 degrees."},
            "2": {"statement": "Prove that the diagonals of a rectangle are equal in length."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide a step-by-step geometric proof for the following statement:

Statement: {t['statement']}

Ensure that your proof is clear, logically structured, and uses appropriate geometric theorems and postulates. Provide your proof in plain text format. Example proof structure:

1. Draw the geometric figure (in your mind or on paper).
2. Identify known elements and given information.
3. State the geometric theorem/postulate being used.
4. Apply the theorem/postulate to the given statement.
5. Draw logical conclusions based on the application.
6. Continue until the statement is proven."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The proof should be logically structured.", "The proof should use appropriate geometric theorems and postulates.", "The proof should correctly establish the given statement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
