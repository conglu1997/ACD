class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a backstory for a character named Elara, a young warrior from a distant land, who has a mysterious past and a special ability to communicate with animals."
            },
            "2": {
                "prompt": "Create a backstory for a character named Dr. Marcus, a brilliant scientist who was once a renowned researcher but is now living in seclusion due to a tragic accident that changed his life."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed backstory for the following character based on the given prompt. Ensure that the backstory is coherent, consistent, and provides a rich narrative. The backstory should include details about the character's early life, significant events, personal motivations, and any unique traits or abilities. Aim for a length of 200-300 words.

Prompt: {t['prompt']}

Provide your backstory in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The backstory should be coherent and consistent.", "The backstory should include details about early life, significant events, personal motivations, and unique traits or abilities."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
