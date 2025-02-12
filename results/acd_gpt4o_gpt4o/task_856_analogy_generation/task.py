class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pair": ["bird", "nest"]},
            "2": {"pair": ["teacher", "classroom"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "pair" in t:
            pair = t["pair"]
            return f"Your task is to generate an analogy based on the following pair of related concepts: {pair[0]} and {pair[1]}. Ensure your analogy is clear and demonstrates a similar relationship between two new concepts. Provide your analogy in plain text format in the following way: 'A is to B as C is to D'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analogy should demonstrate a similar relationship between the new pair of concepts as the given pair.",
            "The analogy should be clear and logical."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
