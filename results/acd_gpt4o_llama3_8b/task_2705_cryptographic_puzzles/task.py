class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "objective": "Solve the following cryptogram: 'GSRH RH Z HVXIVG'. The encrypted message uses a simple substitution cipher where each letter in the alphabet is replaced with its reverse counterpart (A <-> Z, B <-> Y, etc.).",
                "hint": "The solution is a common English phrase."
            },
            "2": {
                "objective": "Create a cryptogram using a Caesar cipher with a shift of 3. Encrypt the message 'HELLO WORLD'.",
                "hint": "Remember to only shift letters and keep the spaces intact."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        objective = t["objective"]
        hint = t["hint"]
        return f"""Complete the following task:\n\nObjective: {objective}\n\nHint: {hint}\n\nSubmit your response as a plain text string.\nFor solving the cryptogram, provide the decrypted message.\nFor creating the cryptogram, provide the encrypted message."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        expected_solution = ""
        if "Solve the following cryptogram" in t['objective']:
            criteria = ["The solution should be the correct decrypted phrase."]
            expected_solution = "THIS IS A SECRET"
        elif "Create a cryptogram" in t['objective']:
            criteria = ["The encrypted message should correctly follow the Caesar cipher with a shift of 3."]
            expected_solution = "KHOOR ZRUOG"
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) and submission.strip() == expected_solution else 0.0
