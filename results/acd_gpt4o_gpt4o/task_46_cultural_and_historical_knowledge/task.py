class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "The fall of the Berlin Wall."},
            "2": {"topic": "The Mona Lisa painting by Leonardo da Vinci."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to provide detailed information about the following topic:

{t["topic"]}

Your response should include:
1. The historical or cultural significance of the topic.
2. Key facts about the topic.
3. Any notable figures or events associated with the topic.

Ensure your information is accurate, well-structured, and provides a comprehensive understanding of the topic. Format your response in plain text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the historical or cultural significance.",
            "The response should include key facts about the topic.",
            "The response should mention any notable figures or events associated with the topic.",
            "The information should be accurate and well-structured.",
            "The response should provide a comprehensive understanding of the topic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
