class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "You are given a singly linked list with the following elements: 1 -> 3 -> 5 -> 7. Your task is to insert the element 4 between the elements 3 and 5. Describe the resulting linked list."},
            "2": {"description": "You are given a binary search tree with the following elements inserted in order: 10, 5, 15, 3, 7, 12, 18. Your task is to delete the element 15 and describe the resulting tree structure."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to perform the specified operation on the given data structure and describe the resulting structure in detail. Ensure that your description is clear, accurate, and includes all relevant details about the structure after the operation.

{description}

Provide your description in plain text format, using complete sentences and paragraphs."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the resulting data structure after the specified operation.",
            "The description should be clear and detailed.",
            "The description should include all relevant details about the structure." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
