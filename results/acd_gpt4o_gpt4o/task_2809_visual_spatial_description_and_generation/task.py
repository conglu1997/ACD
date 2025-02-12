class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'task_type': 'interpret', 'description': 'A rectangular room with a large window on the north wall. There is a bed against the west wall, a desk and a chair by the window, and a bookshelf against the east wall.', 'question': 'Describe the layout of the room using spatial terms.'},
            '2': {'task_type': 'generate', 'description': 'Generate a layout for a small garden with a circular fountain in the center, a wooden bench to the left of the fountain, flowerbeds around the perimeter, and a stone path leading from the entrance to the fountain.', 'criteria': 'Ensure the layout description is clear and follows the specified elements.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            instructions = f"""Your task is to interpret the following visual-spatial description and provide a detailed layout of the scene using spatial terms:

Description: {t['description']}

Question: {t['question']}

Provide your answer in plain text format as a clear and detailed layout of the room. For example: 'The bed is positioned against the west wall, facing east. The desk and chair are by the window on the north wall, and the bookshelf is against the east wall.'"""
        else:
            instructions = f"""Your task is to generate a visual-spatial layout based on the following description:

{t['description']}

Ensure the layout description is clear and follows the specified elements. Provide your submission in plain text format as a detailed layout. For example: 'The circular fountain is in the center of the garden. A wooden bench is located to the left of the fountain. Flowerbeds are around the perimeter, and a stone path leads from the entrance to the fountain.'"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ['The response should correctly describe the layout of the room using spatial terms.']
        else:
            criteria = ['The generated layout should follow the specified elements.', 'The description should be clear and detailed.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
