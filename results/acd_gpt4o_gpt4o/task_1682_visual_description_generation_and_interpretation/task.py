class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"object": "a vintage wooden chair with intricate carvings on the backrest, four legs, and a cushioned seat with floral patterns"},
            "2": {"description": "A small garden with a variety of flowers in bloom, a stone path winding through it, a wooden bench under a large oak tree, and a small fountain in the corner."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'object' in t:
            instructions = f"""Your task is to generate a detailed visual description of the following object:

Object: {t['object']}

Ensure that your description is thorough, clear, and accurately conveys the visual aspects of the object. Provide your description in plain text format. Your response should be structured as follows:

Description: [Your description]"""
        else:
            instructions = f"""Your task is to interpret the following description and visualize the scene or object described:

Description: {t['description']}

Ensure that your visualization is accurate, detailed, and covers all aspects of the description. Provide your visualization in plain text format. Your response should be structured as follows:

Visualization: [Your visualization]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'object' in t:
            criteria = ["The description should accurately convey the visual aspects of the object, including specific details like carvings, legs, and cushioned seat with floral patterns."]
        else:
            criteria = ["The visualization should accurately interpret the description, capturing all mentioned elements such as the variety of flowers, stone path, wooden bench, large oak tree, and small fountain."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
