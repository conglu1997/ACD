class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Create a hypothetical invention that helps reduce air pollution in urban areas. Describe the invention, its components, how it works, and its potential impact on the environment."
            },
            "2": {
                "criteria": "Design a hypothetical invention that can improve the quality of life for elderly people. Describe the invention, its components, how it works, and its potential benefits."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following criteria, create a hypothetical invention and provide a detailed description of it. Your description should include the invention's components, how it works, and its potential impact or benefits.

Criteria: {t['criteria']}

Submit your description as a plain text string with the following format:

Invention Description:
[Your description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include all specified components.",
            "The invention's functionality and impact should be described clearly and logically.",
            "The overall description should be coherent, innovative, and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0