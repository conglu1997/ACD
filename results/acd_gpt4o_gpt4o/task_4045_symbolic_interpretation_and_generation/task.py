class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symbols": "🌟📚🎨"},
            "2": {"symbols": "🚀🛸👽"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task involves two parts: interpreting symbols and generating narratives.

Task 1: Interpret the given symbols or emojis and provide a coherent description that captures their essence. Provide your response in plain text format.
Symbols: {symbols}

Task 2: Create a short narrative based on the given symbols or emojis. Ensure that your narrative is engaging and logically incorporates all the symbols. Provide your response in plain text format.
Symbols: {symbols}""".format(symbols=t["symbols"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should be coherent and accurately capture the essence of the symbols.", "The narrative should be engaging and logically incorporate all the symbols."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
