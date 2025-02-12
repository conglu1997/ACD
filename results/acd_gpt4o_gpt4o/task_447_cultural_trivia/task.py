class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"question": "What is the cultural and historical significance of the cherry blossom in Japanese culture, and how is it celebrated annually?"},
            "2": {"question": "Who wrote the play 'A Midsummer Night's Dream', and what are the central themes explored in this work?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to answer the following cultural trivia question in a clear and concise manner:
{t['question']}
Your response should be accurate and informative, providing any necessary context or background information. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
