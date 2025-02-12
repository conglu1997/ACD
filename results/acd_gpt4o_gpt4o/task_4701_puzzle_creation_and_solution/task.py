class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Create a unique logic puzzle. The puzzle should be original, not a common or well-known puzzle, and should require logical reasoning to solve. Provide the solution to your created puzzle. Then, solve the following puzzle: 'In a group of 100 people, 85 speak English, 75 speak French, and 60 speak both. How many people speak only one language?'"
            },
            "2": {
                "description": "Create a unique word puzzle. The puzzle should involve wordplay or linguistic creativity and should be original. Provide the solution to your created puzzle. Then, solve the following puzzle: 'What 7-letter word becomes longer when the third letter is removed?'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task involves two parts. First, you need to create a unique puzzle of the specified type and provide its solution. The puzzle should not be a common or well-known one. Second, solve the given puzzle. Ensure your responses are in plain text format. Here is the detailed task:\n\n{description}\n\nResponse format:\n1. Created Puzzle: [Your puzzle here]\n2. Solution to Created Puzzle: [Your solution here]\n3. Solution to Given Puzzle: [Your solution to the given puzzle here]""".format(description=t['description'])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The created puzzle should be unique and coherent.",
            "The solution to the created puzzle should be correct and logical.",
            "The solution to the given puzzle should be correct." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
