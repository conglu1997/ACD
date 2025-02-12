class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"question": "What is the traditional dress of Japan, often worn during festivals and ceremonies, called? Provide your answer in one word."},
            "2": {"question": "Which country is renowned for the dance form 'Flamenco', which has its roots in the Andalusian region? Provide your answer in one word."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Answer the following cultural trivia question:

{t["question"]}

Provide your answer as a short, factual statement in one word."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be a factual statement.",
            "The response should correctly answer the trivia question.",
            "The response should be in one word."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
