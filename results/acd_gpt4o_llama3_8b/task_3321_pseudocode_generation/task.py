class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Write pseudocode to find the greatest common divisor (GCD) of two integers using the Euclidean algorithm."
            },
            "2": {
                "problem": "Write pseudocode to sort an array of integers using the QuickSort algorithm."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write pseudocode to solve the following problem: 

Problem:
{t['problem']}

Ensure that your pseudocode includes clear steps and uses appropriate syntax for pseudocode. The pseudocode should be written as follows:
1. [Step 1]
2. [Step 2]
...
Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The pseudocode should correctly solve the specified problem.", "The pseudocode should be clear and follow logical steps.", "The pseudocode should use appropriate syntax for pseudocode."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
