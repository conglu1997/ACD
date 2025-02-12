class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"myth": "The Myth of Icarus"},
            "2": {"myth": "The Legend of Mulan"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a modern retelling of the following mythological story:

{t["myth"]}

Your retelling should include:
1. A brief summary of the original myth.
2. A modernized version of the story that is engaging for contemporary audiences.
3. A description of the main characters, setting, and plot elements involved in the modern version.

Ensure that your retelling maintains the core essence and themes of the original myth while making it relatable and interesting for today's readers. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a brief summary of the original myth.",
            "The response should include a modernized version of the story that is engaging for contemporary audiences.",
            "The retelling should maintain the core essence and themes of the original myth while being relatable and interesting for today's readers."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
