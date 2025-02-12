class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "composition_description": "A piece in C major, starting with a slow, melodic piano introduction, followed by a faster, rhythmic section featuring strings and percussion, and ending with a grand, orchestral finale.",
                "task_type": "interpret"
            },
            "2": {
                "composition": "A symphony in G minor with three movements: an allegro, a lento, and a vivace. The allegro features a prominent violin solo, the lento is characterized by a slow, haunting melody on the oboe, and the vivace is a lively, energetic finale with full orchestra.",
                "task_type": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            return f"""Interpret the following description of a musical composition and identify its key elements. Provide a detailed description of the composition's structure and characteristics. Your interpretation should be clear and logically organized.

Description:
{t['composition_description']}

Submit your interpretation as a plain text string in the following format:
'Key Elements: [Your interpretation here]'"""
        elif t["task_type"] == "generate":
            return f"""Generate a detailed description of the following musical composition. Ensure that the description captures all key elements and characteristics of the composition. Your description should be clear and detailed.

Composition:
{t['composition']}

Submit your description as a plain text string in the following format:
'Detailed Description: [Your description here]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            validation_criteria = ["The interpretation should accurately capture the structure and key elements of the described musical composition.", "The interpretation should be coherent and logically organized."]
        elif t["task_type"] == "generate":
            validation_criteria = ["The generated description should accurately capture the structure and key elements of the given musical composition.", "The description should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
