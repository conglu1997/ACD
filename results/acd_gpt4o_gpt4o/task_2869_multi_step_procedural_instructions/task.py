class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_description": "Assemble a basic bookshelf from pre-cut wooden pieces and screws. Include steps for identifying parts, tools needed, and safety precautions."},
            "2": {"task_description": "Bake a chocolate cake from scratch. Include steps for measuring ingredients, mixing, baking, and decorating the cake."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate detailed, step-by-step procedural instructions for the given task.

Task: {t['task_description']}

Instructions:
1. Break down the task into clear and logical steps.
2. Ensure each step is detailed and easy to follow.
3. Use appropriate technical terminology where necessary.
4. The instructions should be coherent and cover all necessary aspects of the task.
5. Consider potential issues and include troubleshooting tips if relevant.

Your response should be structured as follows:
Step 1: [First step of the process]
Step 2: [Second step of the process]
...
Step N: [Final step of the process]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The instructions should be clear and logically structured.", "Each step should be detailed and accurate.", "The overall process should be coherent and complete.", "The instructions should include all necessary tools, ingredients, and safety precautions.", "Troubleshooting tips should be included where relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
