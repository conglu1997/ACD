import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        themes = [
            {
                "theme": "Space Exploration",
                "concepts": ["exponential growth", "logarithms", "orbital mechanics"]
            },
            {
                "theme": "Climate Change",
                "concepts": ["rate of change", "statistical analysis", "probability"]
            }
        ]
        return {
            "1": random.choice(themes),
            "2": random.choice(themes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a mathematical puzzle based on the theme '{t['theme']}'. Your puzzle should incorporate at least two of the following mathematical concepts: {', '.join(t['concepts'])}.

Your response should include:
1. A clear problem statement (2-3 sentences)
2. The solution to the puzzle (2-3 sentences)
3. An explanation of how the mathematical concepts are applied in the puzzle (2-3 sentences)

Ensure that your puzzle is challenging but solvable, and that it relates meaningfully to the given theme."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The puzzle must be based on the theme '{t['theme']}'.",
            f"The puzzle must incorporate at least two of the following concepts: {', '.join(t['concepts'])}.",
            "The submission must include a clear problem statement, solution, and explanation.",
            "The puzzle must be mathematically sound and solvable.",
            "The explanation must correctly describe how the mathematical concepts are applied in the puzzle."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
