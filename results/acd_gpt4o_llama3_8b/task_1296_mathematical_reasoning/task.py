class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A car travels from City A to City B at an average speed of 55 miles per hour. On its way back from City B to City A, the car travels at an average speed of 45 miles per hour. The distance between the two cities is 220 miles. What is the average speed for the entire trip?"
            },
            "2": {
                "proof": "Prove that the square of any odd integer is always an odd integer."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'problem' in t:
            return f"""Solve the following word problem. Provide a clear and detailed solution, including any necessary calculations and explanations. Submit your solution as a plain text string.\n\nProblem: {t['problem']}\n\nYour solution should include:\n1. Calculation of the time taken for each leg of the journey.\n2. Calculation of the total distance traveled.\n3. Calculation of the average speed for the entire trip."""
        elif 'proof' in t:
            return f"""Generate a mathematical proof for the following statement. Use standard mathematical notation and ensure the proof is logically valid. Present the proof step-by-step, clearly showing each inference. Submit your proof as a plain text string.\n\nStatement: {t['proof']}\n\nExample format:\n1. Assume n is an odd integer.\n2. Represent n as 2k+1 where k is an integer.\n3. Square n to get (2k+1)^2.\n4. Simplify to get 4k^2 + 4k + 1.\n5. Conclude that the result is an odd integer since it is of the form 2m+1 where m is an integer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'problem' in t:
            validation_criteria = [
                "The solution should be correct and include all necessary calculations and explanations.",
                "The solution should correctly calculate the average speed for the entire trip."
            ]
        else:
            validation_criteria = [
                "The proof should be logically valid and use standard mathematical notation.",
                "The proof should show each step and inference clearly.",
                "The proof should conclude that the square of an odd integer is always an odd integer."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
