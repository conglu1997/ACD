class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["All humans are mortal.", "Socrates is a human.", "All mortals eventually die."], "question": "Will Socrates eventually die?"},
            "2": {"premises": ["If it rains, the ground will be wet.", "If the ground is wet, the grass will grow.", "It is raining."], "question": "Will the grass grow?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to analyze the given premises and deduce a logical conclusion. Here are the details:

Premises: {0}
Question: {1}

Ensure that your response is logically sound and directly answers the question based on the provided premises. Provide your response in plain text format as 'Answer: [your conclusion]'.""".format(t["premises"], t["question"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should directly answer the question based on the provided premises.",
            "The response should be logically sound and valid."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
