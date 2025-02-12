class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "technology"},
            "2": {"topic": "animals"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a joke based on the following topic. After generating the joke, provide an explanation of why it is funny and how it relates to the topic.

Topic: {t['topic']}

Your response should include:
1. A humorous and original joke related to the given topic.
2. A clear explanation of why the joke is funny.
3. An explanation of how the joke relates to the given topic.

Ensure your joke is inventive and your explanation is comprehensive. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a humorous and original joke related to the given topic.",
            "The explanation of why the joke is funny should be clear and concise.",
            "The explanation should clearly relate the joke to the given topic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
