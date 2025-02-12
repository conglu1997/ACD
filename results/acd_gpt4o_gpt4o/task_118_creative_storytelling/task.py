class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "A journey through a magical forest", "constraints": ["must include a talking animal", "must involve a hidden treasure"]},
            "2": {"theme": "An unlikely friendship", "constraints": ["must include a robot", "must involve a mystery"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a short story based on the given theme and constraints.

Theme: {t['theme']}
Constraints: {', '.join(t['constraints'])}

Ensure that your story is engaging, coherent, and adheres to the given theme and constraints. Provide your story in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should adhere to the given theme.", "The story should meet the specified constraints.", "The story should be engaging and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
