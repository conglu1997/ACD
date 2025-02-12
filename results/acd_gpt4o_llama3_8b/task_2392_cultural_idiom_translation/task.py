class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_expression": "Break a leg!", "target_culture": "Chinese"},
            "2": {"source_expression": "It's raining cats and dogs.", "target_culture": "Spanish"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        source_expression = t["source_expression"]
        target_culture = t["target_culture"]
        return f"""Translate the following idiomatic expression into an equivalent expression in {target_culture} culture while retaining its intended meaning and contextual appropriateness:

Idiomatic Expression: '{source_expression}'

Ensure that your translation adheres to the cultural context and conveys the same meaning as the original expression.

Submit your translated expression as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translated expression should be idiomatic in the target culture.",
            "The translated expression should retain the intended meaning of the original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
