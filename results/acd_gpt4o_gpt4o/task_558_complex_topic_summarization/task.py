class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Quantum Computing", "levels": ["detailed", "concise"]},
            "2": {"topic": "Climate Change", "levels": ["detailed", "concise"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to summarize the following complex topic at different levels of detail:

Topic: {t["topic"]}

Summarize the topic in the following ways:
1. A detailed summary (approximately 300 words, within the range of 250-350 words)
2. A concise summary (approximately 50 words, within the range of 40-60 words)

Provide your summaries in plain text format, clearly indicating which is the detailed summary and which is the concise summary. Format your response as follows:

Detailed Summary: [Your detailed summary]
Concise Summary: [Your concise summary]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The detailed summary should be within the range of 250-350 words.",
            "The concise summary should be within the range of 40-60 words.",
            "Both summaries should accurately capture the key points of the topic.",
            "The summaries should be clear, coherent, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
