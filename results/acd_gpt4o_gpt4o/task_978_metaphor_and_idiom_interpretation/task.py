class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"expression": "The ball is in your court."},
            "2": {"expression": "Burning the midnight oil."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        expression = t["expression"]
        instructions = f"""Your task is to interpret the following metaphor or idiomatic expression and respond appropriately to a given scenario:

Expression: {expression}

Scenario: Imagine you are explaining this expression to someone who is not familiar with it. Provide a clear and accurate interpretation of the expression and give an example of how it might be used in a conversation.

Your response should include:
1. A clear interpretation of the expression's meaning.
2. An example of how the expression can be used in a sentence.

Ensure your response is coherent, accurate, and demonstrates a clear understanding of the figurative language.

Format your response as follows:

Interpretation: [Your interpretation]
Example: [Your example sentence]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation of the expression should be clear and accurate.",
            "The example sentence should appropriately use the expression in context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
