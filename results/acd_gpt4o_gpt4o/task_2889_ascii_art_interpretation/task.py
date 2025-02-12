class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art": [
                "  ###  ",
                " #   # ",
                "#     #",
                "#  #  #",
                "#     #",
                " #   # ",
                "  ###  "
            ], "prompt": "Describe the above ASCII art in detail, identifying any recognizable patterns or objects."},
            "2": {"art": [
                "  +  ",
                " + + ",
                "+   +",
                " + + ",
                "  +  "
            ], "prompt": "Transform the above ASCII art into an alternative representation while maintaining the same structure and meaning."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        art = '\n'.join(t["art"])
        prompt = t["prompt"]
        instructions = f"""Your task is to interpret and respond to the given ASCII art:

{art}

{prompt}

Provide a detailed and thoughtful response. Ensure that your interpretation or transformation maintains the integrity of the original art and captures its essence. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe or interpret the ASCII art.",
            "The response should maintain the integrity and essence of the original art.",
            "The response should be detailed and thoughtfully crafted."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
