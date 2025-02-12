class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Three people (Alice, Bob, and Charlie) are standing in a line. Each person can see the people in front of them but not behind. They are each wearing a hat that is either red or blue. They can only see the hats of the people in front of them. When asked, Alice says 'I don't know what color my hat is.' Then Bob says 'I don't know what color my hat is.' Finally, Charlie says 'I know the color of my hat.' What color is Charlie's hat?"},
            "2": {"criteria": "Generate a new logical puzzle involving three people with different professions (doctor, lawyer, and engineer) who are trying to determine who has which profession based on a set of clues. Ensure the puzzle has a single, clear solution."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'puzzle' in t:
            return f"""Solve the following logical puzzle and provide your answer. Explain your reasoning step by step. Submit your response as a plain text string in the following format:

Answer: [Your answer]
Reasoning: [Your step-by-step reasoning]

Puzzle: {t['puzzle']}"""
        else:
            return f"""Generate a new logical puzzle based on the given criteria. Ensure the puzzle involves three people with different professions (doctor, lawyer, and engineer) and includes a set of clues that lead to a single, clear solution. Provide the puzzle and the solution. Submit your response as a plain text string in the following format:

Puzzle: [Your generated puzzle]
Solution: [The solution to your puzzle]

Criteria: {t['criteria']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'puzzle' in t:
            criteria = ["The solution should correctly identify the color of Charlie's hat and provide a clear, logical explanation."]
        else:
            criteria = ["The generated puzzle should involve three people with different professions and include a set of clues leading to a single, clear solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
