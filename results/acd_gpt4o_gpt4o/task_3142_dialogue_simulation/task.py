class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The impact of artificial intelligence on job markets"
            },
            "2": {
                "topic": "The benefits and drawbacks of remote working"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a coherent, contextually appropriate dialogue between two individuals on the given topic. Ensure that the dialogue is natural, maintains context, and flows logically from one turn to the next. Each participant should have a distinct voice and perspective on the topic. The dialogue should consist of at least six turns (three for each participant).

Topic: {t['topic']}

Provide your dialogue in the following format:

Person A: [First turn]
Person B: [Second turn]
Person A: [Third turn]
Person B: [Fourth turn]
Person A: [Fifth turn]
Person B: [Sixth turn]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be coherent and contextually appropriate.",
            "The dialogue should maintain logical flow and context across turns.",
            "Each participant should have a distinct voice and perspective.",
            "The dialogue should consist of at least six turns (three for each participant)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
