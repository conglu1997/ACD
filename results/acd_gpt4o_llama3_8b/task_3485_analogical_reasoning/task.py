class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pairs": ["sun:day", "moon:"]
            },
            "2": {
                "pairs": ["teacher:classroom", "doctor:hospital"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the relationship between the given pairs of concepts and apply the same relationship to complete the new pair. Submit your response as a plain text string in the following format:

Response: [Your response]

Example:
Pairs: 'pen:write', 'brush:paint'
Response: 'brush:paint'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response must correctly identify and apply the relationship between the given pairs."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
