class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a sequence of escape room puzzles where the players must solve a series of challenges to find a hidden key."
            },
            "2": {
                "prompt": "Create a sequence of escape room puzzles where the players must deactivate a bomb by solving a series of interconnected puzzles."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "hidden key" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Create a sequence of escape room puzzles where the players must solve a series of challenges to find a hidden key. Your sequence should include at least 3 distinct puzzles, each with a clear solution that logically leads to the next puzzle. Ensure that the puzzles are engaging, coherent, and solvable. Provide a detailed description of each puzzle and its solution.

Submit your response as a plain text string in the following format:

1. Puzzle Description: [Description of the first puzzle]
   Solution: [Solution to the first puzzle]
2. Puzzle Description: [Description of the second puzzle]
   Solution: [Solution to the second puzzle]
3. Puzzle Description: [Description of the third puzzle]
   Solution: [Solution to the third puzzle]"""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Create a sequence of escape room puzzles where the players must deactivate a bomb by solving a series of interconnected puzzles. Your sequence should include at least 3 distinct puzzles, each with a clear solution that logically leads to the next puzzle. Ensure that the puzzles are engaging, coherent, and solvable. Provide a detailed description of each puzzle and its solution.

Submit your response as a plain text string in the following format:

1. Puzzle Description: [Description of the first puzzle]
   Solution: [Solution to the first puzzle]
2. Puzzle Description: [Description of the second puzzle]
   Solution: [Solution to the second puzzle]
3. Puzzle Description: [Description of the third puzzle]
   Solution: [Solution to the third puzzle]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The sequence should include at least 3 distinct puzzles.", "Each puzzle should have a clear solution that logically leads to the next puzzle.", "The puzzles should be engaging, coherent, and solvable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
