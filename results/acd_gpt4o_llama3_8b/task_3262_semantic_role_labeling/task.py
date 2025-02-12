class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sentence": "The chef, who recently moved to the city and started a new job, cooked a delicious meal for the guests in the new kitchen despite the power outage."
            },
            "2": {
                "sentence": "Despite the rain and unexpected delays, the company launched a new product in the market last week with great success, surprising all the analysts and stakeholders."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the predicate-argument structures in the following sentence. For each predicate, list its arguments and their roles (e.g., agent, theme, recipient, location, etc.).

Sentence: {t['sentence']}

Submit your response in the following format:

Predicate: [predicate]
Arguments:
- [role1]: [argument1]
- [role2]: [argument2]
- ..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should correctly identify the predicate in the sentence.",
            "The response should accurately list all arguments associated with the predicate.",
            "The response should correctly label the roles of each argument.",
            "The response should follow the specified format precisely."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
