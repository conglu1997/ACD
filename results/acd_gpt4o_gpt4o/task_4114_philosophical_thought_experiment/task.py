class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "personal identity"},
            "2": {"theme": "ethics and morality"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        instructions = f"""Your task is to create and explain a philosophical thought experiment based on the following theme: {theme}.

Your thought experiment should include:
1. A detailed description of the scenario.
2. The key questions or dilemmas it raises.
3. An explanation of the potential implications and significance of the thought experiment.

Ensure your explanation is clear, well-structured, and demonstrates deep conceptual thinking. Your response should be at least 300 words in length. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a detailed description of the scenario.", "The key questions or dilemmas should be clearly stated.", "The potential implications and significance should be explained.", "The response should be at least 300 words in length."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
