class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"outputs": ["abc -> def", "ghi -> jkl", "mno -> pqr"]},
            "2": {"outputs": ["123 -> 246", "456 -> 912", "789 -> 1578"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to reverse engineer the given system based on the provided outputs. Identify the underlying rule or structure that transforms the input into the output. Provide a clear and detailed explanation of the rule, demonstrating how it applies to each given example.

Examples:
{t['outputs']}

Provide your explanation in plain text format. Your explanation should include the general rule and a step-by-step application of the rule to each example."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should clearly identify the rule or structure that transforms the input into the output.", "The rule should be consistently applicable to all provided examples.", "The explanation should include a step-by-step application of the rule to each example."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
