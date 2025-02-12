class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Five friends are sitting in a row. Each friend likes a different fruit and wears a different colored shirt. Figure out who likes which fruit and what color shirt they are wearing based on the following clues: 1. John is wearing a blue shirt. 2. The person who likes apples is sitting immediately to the right of the person wearing the blue shirt. 3. Sarah likes bananas and is sitting in the middle. 4. The person wearing the red shirt is at one of the ends. 5. The person who likes oranges is sitting immediately to the left of the person wearing the green shirt. 6. Mike is sitting to the far left."
            },
            "2": {
                "puzzle": "Four people need to cross a bridge at night. They have one flashlight and at most two people can cross at a time. The bridge is too dangerous to cross without a flashlight. Person A can cross the bridge in 1 minute, Person B in 2 minutes, Person C in 5 minutes, and Person D in 10 minutes. When two people cross the bridge together, they must move at the slower person's pace. What is the minimum time required for all four people to cross the bridge?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logical puzzle. Carefully read the clues and constraints provided, and deduce the correct answer.\n\nPuzzle: {t['puzzle']}\n\nProvide your solution in plain text format as follows:\n\nSolution: [Your solution]\n\nExplanation: [Explain how you arrived at your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution must correctly identify the answer based on the given clues and constraints.", "The solution must be logically coherent and accurately derived from the provided information."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
