class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "You have 8 balls, one of which is heavier than the others. You have a balance scale that you can use only two times. Determine which ball is the heavier one.",
                "constraints": "You must use the balance scale exactly two times."
            },
            "2": {
                "puzzle": "There are three houses in a row, each painted a different color: red, blue, and green. Each house is owned by a different person: Alice, Bob, and Carol. Use the following clues to determine who owns each house and what color it is painted: 1. Alice owns the house next to the green one. 2. Bob does not own the red house. 3. Carol owns the house next to the blue one.",
                "constraints": "All clues must be used to determine the ownership and color of each house."            
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given puzzle and constraints:

Puzzle: {t['puzzle']}

Constraints: {t['constraints']}

Provide a detailed solution that explains each step of your reasoning process. Ensure that your solution is logical, coherent, and follows the given constraints.

Submit your response as a plain text string in the following format:

Solution: [Your detailed solution here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The solution must correctly identify the heavier ball or the ownership and color of each house.", "The solution must follow the given constraints and use logical reasoning.", "The solution must be detailed and explain each step of the reasoning process."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
