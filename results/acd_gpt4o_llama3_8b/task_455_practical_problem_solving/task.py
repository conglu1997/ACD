class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "How can we reduce plastic waste in urban areas?"
            },
            "2": {
                "problem": "How can public transportation be made more accessible for people with disabilities?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Devise a practical solution to the following real-world problem. Your solution should be creative, feasible, and actionable. Provide a detailed explanation of your proposed solution, including the steps needed to implement it and any potential challenges that might arise. Ensure your explanation is clear, well-structured, and addresses feasibility.

Problem: {t['problem']}

Submit your response as a plain text string in the following format:
Solution: [Your solution]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The solution should be practical, creative, and feasible.", "The explanation should be detailed, well-structured, and address potential challenges."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
