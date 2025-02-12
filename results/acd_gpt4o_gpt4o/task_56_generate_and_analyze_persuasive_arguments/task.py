class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Why recycling should be mandatory.", "type": "generate"},
            "2": {"argument": "Increasing funding for public transportation will reduce traffic congestion and pollution, making our cities more livable.", "type": "analyze"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate":
            return f"""Your task is to generate a persuasive argument for the following topic: {t["topic"]}. Make sure your argument is compelling, logically structured, and uses persuasive techniques effectively. Provide your argument in a paragraph."""
        else:
            return f"""Your task is to analyze the following argument: '{t["argument"]}'. Identify and explain the persuasive techniques used in this argument. Provide your analysis in 2-3 sentences."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate":
            criteria = ["The argument should be compelling, logically structured, and use persuasive techniques effectively."]
        else:
            criteria = ["The analysis should accurately identify and explain the persuasive techniques used in the argument."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
