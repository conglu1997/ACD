class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"elements": ["a beach with people", "a sunset", "a lighthouse", "seagulls flying"], "constraints": ["mention the colors vividly", "include at least one sound effect"]},
            "2": {"elements": ["a bustling city street", "a street musician", "a food truck", "people walking dogs"], "constraints": ["describe at least three smells", "mention different types of clothing people are wearing"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide a detailed textual description of a scene based on the following visual elements:

Elements: {', '.join(t['elements'])}

Constraints: {', '.join(t['constraints'])}

Ensure your description is vivid, coherent, and adheres to the given constraints. Format your response in plain text as follows:

Description: [Your detailed description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The description should include the elements: {', '.join(t['elements'])}.",
                    "The description should adhere to the given constraints.",
                    "The description should be vivid and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
