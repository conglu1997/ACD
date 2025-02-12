class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Discuss the impact of social media on mental health."},
            "2": {"topic": "Debate the pros and cons of remote work."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        return f"""Engage in a multi-turn conversation on the following topic: {topic}\nEnsure that your responses are coherent, relevant, and demonstrate an understanding of the context across all turns. Submit your conversation as a plain text string in the following format:\n\nTurn 1: [Your response]\nTurn 2: [Your response]\nTurn 3: [Your response]\n(and so on for a total of 5 turns)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The conversation should be coherent across all turns.", "Each response should be relevant to the topic and previous turns.", "Context should be retained and built upon in each turn."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
