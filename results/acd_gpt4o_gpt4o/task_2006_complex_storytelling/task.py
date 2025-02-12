class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"elements": ["a lost prince", "a magical forest", "a talking animal", "a hidden treasure"], "constraints": ["must include a moral lesson", "must have a twist ending"]},
            "2": {"elements": ["a time-traveling scientist", "a dystopian future", "a mysterious artifact", "a secret society"], "constraints": ["must include a love interest", "must resolve with a hopeful message"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a cohesive narrative based on the following elements and constraints:

Elements: {', '.join(t['elements'])}
Constraints: {', '.join(t['constraints'])}

Ensure your story is engaging, coherent, and integrates all the given elements while adhering to the constraints. The narrative should be between 300 and 500 words. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should be engaging and coherent.", "The narrative should integrate all the given elements.", "The narrative should adhere to all the given constraints.", "The response should be between 300 and 500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
