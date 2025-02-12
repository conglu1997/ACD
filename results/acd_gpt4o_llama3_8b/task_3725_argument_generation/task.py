class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The use of surveillance cameras in public spaces."
            },
            "2": {
                "topic": "The implementation of universal basic income."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate coherent and logically consistent arguments for and against the following controversial topic. Ensure that each argument is clear, well-structured, and addresses the key points of the topic. Provide at least three distinct and non-repetitive points for each side (for and against), and support each point with evidence or examples.\n\nTopic:\n{t['topic']}\n\nFormat your response as follows:\nFor:\n1. [Point 1 with evidence/example]\n2. [Point 2 with evidence/example]\n3. [Point 3 with evidence/example]\n\nAgainst:\n1. [Point 1 with evidence/example]\n2. [Point 2 with evidence/example]\n3. [Point 3 with evidence/example]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The arguments for and against the topic should be coherent and logically consistent.",
            "Each side should contain at least three distinct and non-repetitive points.",
            "Each point should be supported by evidence or examples.",
            "The points should be well-structured and address key aspects of the topic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
