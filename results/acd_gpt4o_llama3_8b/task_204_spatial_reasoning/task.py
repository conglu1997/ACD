class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Imagine you are standing in a room with a table in the center. On the table, there are three objects: a book, a vase, and a lamp. The book is to the left of the vase, and the lamp is to the right of the vase. Describe the relative positions of the book and the lamp with respect to each other."
            },
            "2": {
                "description": "You are in a park. To your north, there is a playground. To your east, there is a pond. To your south, there are benches. To your west, there is a fountain. If you turn to face the fountain and then turn left, what will you be facing?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following spatial description and provide a solution that demonstrates your understanding of the spatial relationships involved. Here is the description:

{t["description"]}

Ensure your response is coherent, logically structured, and accurately reflects the spatial relationships described. Submit your response as a plain text string in the following format:

Response: [Your Answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
