class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "statement": "Prove that the sum of the first n natural numbers is given by the formula S = n(n + 1) / 2."
            },
            "2": {
                "statement": "Prove that the product of any two even numbers is always even."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        statement = t["statement"]
        instructions = f"""Your task is to generate a formal mathematical proof for the following statement:

{statement}

Your proof should be clear, logically structured, and use appropriate mathematical notation and terminology. Please provide your proof in plain text format.

The proof should follow these steps:
1. State the proposition clearly.
2. Provide any definitions or known theorems that will be used.
3. Develop the proof with step-by-step logical reasoning, ensuring each step is justified.
4. Conclude the proof by summarizing the findings and restating the proven statement."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proof must be logically coherent and mathematically correct.",
            "The proof must follow the step-by-step structure outlined in the instructions.",
            "The final conclusion must accurately restate the proven statement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
