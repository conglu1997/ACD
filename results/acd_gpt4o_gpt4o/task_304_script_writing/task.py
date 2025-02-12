class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Friendship", "constraints": "Include at least two characters, a conflict, and a resolution. The script should be suitable for a 5-minute performance."},
            "2": {"theme": "Mystery", "constraints": "Include at least three characters, a mystery element, and a twist ending. The script should be suitable for a 10-minute performance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a short script for a play or skit based on the given theme and constraints.

Theme: {t['theme']}

Constraints: {t['constraints']}

Ensure that the script includes appropriate dialogue, stage directions, and maintains coherence throughout. The script should be engaging and fit within the specified performance time.

Provide the script in the following format:

Characters:
- [Character 1]: [Description]
- [Character 2]: [Description]
...

[Scene description]

[Character 1]: [Dialogue]
[Character 2]: [Dialogue]
...

[Stage directions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The script should adhere to the given theme and constraints.",
            "The dialogue and stage directions should maintain coherence.",
            "The script should be engaging and suitable for the specified performance time." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
