class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the ambassador of Country A, and you need to respond to a neighboring country's concerns about a recent border incident. Ensure your response is diplomatic, acknowledges their concerns, and proposes a constructive way forward."},
            "2": {"scenario": "As a representative of an international organization, you need to address a controversial statement made by a member country without escalating tensions. Your response should be balanced, neutral, and promote dialogue."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to craft a diplomatically sensitive response to the given scenario. Ensure that your response is appropriate, tactful, and culturally sensitive. Use language that promotes understanding and cooperation. Format your response as follows:

1. Diplomatic Response: [Your response]""".format(t["scenario"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be appropriate, tactful, and culturally sensitive. It should acknowledge concerns and propose constructive solutions without escalating tensions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
