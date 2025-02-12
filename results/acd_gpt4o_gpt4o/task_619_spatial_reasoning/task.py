class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Imagine a room with the following objects: a table in the center, a chair to the north of the table, a lamp to the east of the table, and a bookshelf to the west of the table. Describe the position of the chair relative to the lamp and the bookshelf. Provide your response in plain text format."
            },
            "2": {
                "description": "Visualize a park with a fountain in the middle. There is a tree to the south of the fountain, a bench to the north, a playground to the east, and a flower bed to the west. Explain how you would walk from the tree to the playground, passing by the fountain and the bench. Provide your response in plain text format."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to interpret the following spatial description and provide a clear and accurate response based on the spatial relationships described. Ensure your response is in plain text format, and clearly addresses the specific questions or tasks posed. Here is the description:\n\n{description}\n\nSubmit your response in plain text format.""".format(description=t['description'])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately interpret the spatial relationships described.",
            "The response should be clear and logically consistent.",
            "The response should correctly address the specific questions or tasks posed in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
