class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "interpret", "art": "🟦🟥⬛⬜🟨🟩🔺🔶"},
            "2": {"type": "generate", "prompt": "Create a description for an abstract art piece that uses a mix of geometric shapes, bold colors, and varying textures to convey a sense of chaos and complexity."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "interpret":
            return f"""Given the following abstract art piece represented by emojis, generate a coherent description that interprets the shapes, colors, and overall composition. Your description should be creative and convey a meaningful interpretation of the abstract art.

Abstract art piece:
{t['art']}

Submit your response as a plain text string."""
        elif t["type"] == "generate":
            return f"""Given the following prompt, generate a detailed description for an abstract art piece. Ensure that your description is vivid, creative, and captures the essence of the abstract art as described in the prompt.

Prompt:
{t['prompt']}

Submit your response as a plain text string."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["type"] == "interpret":
            criteria.append("The description should interpret the shapes, colors, and overall composition.")
            criteria.append("The description should be creative and convey a meaningful interpretation.")
        elif t["type"] == "generate":
            criteria.append("The description should be vivid, creative, and capture the essence of the abstract art as described in the prompt.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
