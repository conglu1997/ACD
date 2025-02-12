import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        principles = [
            "conservation of energy",
            "natural selection",
            "plate tectonics",
            "quantum superposition",
            "thermodynamics"
        ]
        puzzle_types = [
            "riddle",
            "word puzzle",
            "logic puzzle",
            "visual puzzle",
            "mathematical puzzle"
        ]
        return {
            "1": {"principle": random.choice(principles), "puzzle_type": random.choice(puzzle_types)},
            "2": {"principle": random.choice(principles), "puzzle_type": random.choice(puzzle_types)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a {t['puzzle_type']} that demonstrates the scientific principle of {t['principle']}. Your response should include:

1. The puzzle itself (100-150 words)
2. The solution to the puzzle (50-100 words)
3. An explanation of how the puzzle demonstrates the scientific principle (100-150 words)

Ensure that your puzzle is original, engaging, and accurately reflects the chosen scientific principle. The puzzle should be challenging but solvable with the information provided.

Format your response as follows:

Puzzle:
[Your puzzle here]

Solution:
[Your solution here]

Explanation:
[Your explanation here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle accurately demonstrates the given scientific principle.",
            "The puzzle is original, engaging, and appropriate for the specified puzzle type.",
            "The solution is correct and clearly explained.",
            "The explanation effectively links the puzzle to the scientific principle.",
            "The response adheres to the specified word counts and format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
