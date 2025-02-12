class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate a joke that involves a wordplay or pun."},
            "2": {"prompt": "Analyze the following text and determine if it contains humor. If so, explain what makes it humorous: 'I told my wife she was drawing her eyebrows too high. She looked surprised.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        response_format = """Response format:
1. For joke generation:
Joke: [Your joke here]

2. For humor detection:
Contains Humor: [Yes/No]
Explanation: [Your explanation here]
"""
        return "Your task is to perform the following instruction: {}\n\n{}".format(t["prompt"], response_format)

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["prompt"].startswith("Generate"):
            criteria = ["The response should be a joke that makes use of wordplay or a pun."]
        elif t["prompt"].startswith("Analyze"):
            criteria = ["The response should correctly identify if the text contains humor and provide a coherent explanation of what makes it humorous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
