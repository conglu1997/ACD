class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'prompt': 'Describe a city floating in the sky, with buildings made of glass and clouds that change colors with the time of day.'},
            '2': {'prompt': 'Describe a forest where the trees are made of crystal, the ground is covered in soft moss that glows in the dark, and mythical creatures roam freely.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed and vivid description of the following scene. Ensure that your description is imaginative, coherent, and includes sensory details to bring the scene to life. Here is the prompt:

{t['prompt']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ['The description should be detailed and vivid.', 'The description should be coherent and imaginative.', 'The description should include sensory details.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
