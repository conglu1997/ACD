class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Create a visual maze with the following features: a starting point, an ending point, multiple paths, some dead ends, and at least one loop. The maze should be challenging and visually appealing. Provide a detailed description of the maze, including its layout, key features, and the path to the solution."
            },
            "2": {
                "criteria": "Create a visual puzzle that involves arranging shapes to fit into a 5x5 grid. The shapes should include triangles, squares, and circles, and must fit together without overlapping. Provide a detailed description of the puzzle, including the grid layout, the shapes to be used, and how the puzzle can be solved."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and describe a visual puzzle based on the following criteria:

Criteria: {t['criteria']}

Your description should include a detailed explanation of the puzzle's layout, key features, and how it meets the given criteria. Use clear and precise language to convey your design.

Submit your response in the following format:

- Description: [Your description here]
- Criteria Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The puzzle should include all specified features.",
            "The puzzle should be challenging and visually appealing.",
            "The description should be clear and precise, explaining the layout and key features of the puzzle.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
