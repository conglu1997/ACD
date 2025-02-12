class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "What comes next in the sequence: 2, 4, 8, 16, ?"
            },
            "2": {
                "puzzle": "You have a 3-liter jug and a 5-liter jug. How can you measure exactly 4 liters of water using these jugs? Provide the steps clearly and concisely."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following puzzle:

{t['puzzle']}

For the first puzzle, provide the next number in the sequence as a single number. For the second puzzle, describe the steps clearly and concisely. For example, if you need to measure 2 liters, you can fill the 3-liter jug and pour it into the 5-liter jug until the 5-liter jug is full, leaving you with 1 liter in the 3-liter jug. Empty the 5-liter jug, pour the remaining 1 liter into the 5-liter jug, and fill the 3-liter jug again. Pour from the 3-liter jug into the 5-liter jug until you have 2 liters in the 3-liter jug."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should correctly solve the given puzzle.",
            "For the second puzzle, the steps should be described clearly and concisely."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
