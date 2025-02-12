class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Five friends have their gardens next to one another, where each garden has a different flower. From the clues, determine who has which flower.\n\nClues:\n1. The person with the rose garden is somewhere to the left of the person with the tulip garden.\n2. The person with the daisy garden is at one end.\n3. The person with the lily garden is next to the person with the tulip garden.\n4. The person with the daisy garden is next to the person with the sunflower garden.\n5. The person with the lily garden is in the middle."
            },
            "2": {
                "puzzle": "Three people (Alice, Bob, and Carol) are sitting in a row, each wearing a hat that is either red or blue. Each person can see the hats of the other two but not their own. They are asked consecutively if they know the color of their own hat.\n\nClues:\n1. Alice says she does not know.\n2. Bob says he does not know.\n3. Carol says she knows.\n\nDetermine the colors of the hats of Alice, Bob, and Carol."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following logic puzzle based on the given clues. Provide your solution in a clear and concise manner.\n\nPuzzle:\n{t['puzzle']}\n\nFormat your response as follows: For Task 1, list the gardens and their corresponding flowers in order. For Task 2, list the colors of the hats for Alice, Bob, and Carol in that order."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["puzzle"].startswith("Five friends have their gardens"): 
            criteria = [
                "The solution should list the gardens and their corresponding flowers in the correct order.",
                "The solution should be based on the given clues.",
                "The solution should be logically consistent."
            ]
        elif t["puzzle"].startswith("Three people (Alice, Bob, and Carol)"):
            criteria = [
                "The solution should list the colors of the hats for Alice, Bob, and Carol in the correct order.",
                "The solution should be based on the given clues.",
                "The solution should be logically consistent."
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
