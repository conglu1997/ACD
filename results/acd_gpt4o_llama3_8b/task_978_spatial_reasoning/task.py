class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Imagine you are standing in a room with the following items: A chair is to the left of a table. A vase is on the table. A painting is on the wall directly opposite the table. A lamp is on the floor to the right of the table. There is a bookshelf behind the chair. Describe the position of the painting relative to the bookshelf.",
                "answer": "The painting is directly opposite the bookshelf."
            },
            "2": {
                "description": "You are in a park. There is a bench facing a pond. To the left of the bench is a tree. There is a fountain behind the bench. A statue is to the right of the pond. Describe the position of the statue relative to the tree.",
                "answer": "The statue is to the right of the tree."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following spatial description and make an inference based on it:

Description: {t['description']}

Provide your answer as a plain text string in the format: 'The [object] is [spatial relationship] the [reference object].' Ensure your response is clear and directly addresses the spatial relationship described."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should correctly describe the position of the items as inferred from the description: {t['answer']}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
