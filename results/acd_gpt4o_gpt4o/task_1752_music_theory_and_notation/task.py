class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "notation": "C4 E4 G4",
                "problem": "Identify the chord represented by the given musical notes in scientific pitch notation.",
                "expected_output": "C major"
            },
            "2": {
                "notation": "A3 C4 E4",
                "problem": "Identify the intervals between the given musical notes in scientific pitch notation.",
                "expected_output": "minor third, major third"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to understand the given musical notation and solve the specified problem.

Given Notation: {t['notation']}
Problem: {t['problem']}

Provide your solution in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution correctly identifies or converts the given musical notation.",
            "The response should be accurate and relevant to the problem specified."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
