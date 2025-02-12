class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "Ancient Rome during the reign of Julius Caesar.", "constraints": "Include a scene involving a political intrigue in the Roman Senate, with at least three historical figures present and a significant plot twist."},
            "2": {"context": "Medieval Europe during the Black Death.", "constraints": "Focus on the life of a healer trying to help the afflicted, incorporating historically accurate methods of treatment and the societal response to the plague."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a short piece of historical fiction based on the following context and constraints:

Historical Context: {t['context']}

Constraints: {t['constraints']}

Your story should be historically accurate, engaging, and fit within the provided context and constraints. Provide your response in plain text format.

Format your response as follows:

Story: <your historical fiction piece>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be historically accurate.",
            "The story should be engaging and coherent.",
            "The story should fit within the provided context and constraints.",
            "The story should demonstrate creativity.",
            "The language should be appropriate for the historical setting."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
