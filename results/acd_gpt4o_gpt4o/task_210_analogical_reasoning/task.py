class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pair1": ["fire", "heat"], "pair2": ["sun", "?"]},
            "2": {"pair1": ["teacher", "teach"], "pair2": ["doctor", "?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pair1 = t["pair1"]
        pair2 = t["pair2"]
        instructions = f"""Your task is to identify the relationship between the first pair of concepts and apply this relationship to complete the second pair of concepts.

First Pair: {pair1[0]} is to {pair1[1]} as {pair2[0]} is to _____.

Provide your answer in plain text format. Ensure that the relationship is similar in both pairs."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly identify the relationship between the first pair of concepts.",
            "The submission should apply this relationship accurately to complete the second pair of concepts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
