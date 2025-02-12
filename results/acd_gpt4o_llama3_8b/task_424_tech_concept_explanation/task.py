class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Explain the concept of recursion in computer programming. Include an example in your explanation."
            },
            "2": {
                "concept": "Explain the concept of Big O notation and its importance in algorithm analysis. Include an example in your explanation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following technical concept clearly and concisely. Your explanation should be original and detailed enough for someone with a basic understanding of computer science to grasp the concept. Ensure you include an example to illustrate the concept. Here is the concept:

{t["concept"]}

Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be clear and concise.",
            "The explanation should include an example illustrating the concept.",
            "The explanation should be original and detailed enough for someone with a basic understanding of computer science to understand."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
