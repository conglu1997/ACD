class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art": "\n   ____\n  /  o  \ \n | o   o |\n  \__^__/"},
            "2": {"art": "\n  /\_/\ \n ( o.o )\n  > ^ <"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following piece of ASCII art and provide a detailed description of what it represents. Your description should be clear, accurate, and provide enough detail to convey the essence of the image. Submit your description as a plain text string. Here is the ASCII art:\n{t['art']}\nYour response should be at least 50 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately represent the ASCII art.", "The description should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
