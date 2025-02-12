class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story set in a post-apocalyptic world where humanity is rebuilding."},
            "2": {"prompt": "Write a short story about a young wizard discovering their powers in a magical academy."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "post-apocalyptic" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Write a short story set in a post-apocalyptic world where humanity is rebuilding. Your story should include:
1. A vivid description of the setting and the remnants of the old world.
2. The challenges faced by the characters in this new world.
3. The progress and hope for the future as humanity rebuilds.

Ensure your story is engaging, well-structured, and imaginative. Submit your response as a plain text string in the following format:

Story: [Your Story Here]"""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Write a short story about a young wizard discovering their powers in a magical academy. Your story should include:
1. A vivid description of the magical academy and its environment.
2. The experiences and challenges the young wizard faces while discovering their powers.
3. The growth and development of the young wizard's abilities and character.

Ensure your story is engaging, well-structured, and imaginative. Submit your response as a plain text string in the following format:

Story: [Your Story Here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "post-apocalyptic" in t["prompt"]:
            criteria = ["The story should include a vivid description of the setting, the challenges faced by the characters, and the progress and hope for the future.", "The story should be engaging, well-structured, and imaginative."]
        else:
            criteria = ["The story should include a vivid description of the magical academy, the experiences and challenges of the young wizard, and the growth and development of the character.", "The story should be engaging, well-structured, and imaginative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
