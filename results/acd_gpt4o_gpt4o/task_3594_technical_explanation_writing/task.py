class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Explain how a blockchain works and its potential applications in various industries."
            },
            "2": {
                "concept": "Explain the process of machine learning, including key steps such as data collection, training, validation, and deployment."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Your task is to explain the following technical concept in a clear and understandable way: {t['concept']}\n"
            "Ensure that your explanation is comprehensive, well-structured, and accessible to a general audience.\n"
            "Use simple language and avoid technical jargon wherever possible.\n"
            "Provide your response in plain text format with the following structure:\n"
            "1. Introduction\n"
            "2. Detailed Explanation\n"
            "3. Conclusion"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
