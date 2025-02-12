class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "There is a table in the center of the room. A chair is placed to the north of the table, a lamp to the east, a bookshelf to the south, and a plant to the west.", "description": "A table is in the center of the room with a chair to the north, a lamp to the east, a bookshelf to the south, and a plant to the west."},
            "2": {"scenario": "A park has a fountain in the middle. To the north of the fountain, there is a bench. To the south, there is a playground. To the east, there is a statue, and to the west, there are trees.", "description": "A park with a fountain in the center has a bench to the north, a playground to the south, a statue to the east, and trees to the west."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following scenario, describe the spatial arrangement of objects:

Scenario: {t['scenario']}

Provide your response in the following format: '[Object] is to the [direction] of [central object].'
For example: 'The chair is to the north of the table.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
