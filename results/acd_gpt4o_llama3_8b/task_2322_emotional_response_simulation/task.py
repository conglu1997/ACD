class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Alex just received a promotion at work after months of hard work and dedication."
            },
            "2": {
                "scenario": "Jamie found out that their best friend is moving to another country for a new job opportunity."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following scenario, generate a plausible emotional response for the character involved. Then, provide a short narrative explaining why the character feels this way. Ensure that the response is contextually appropriate and reflects a deep understanding of human emotions.

Scenario: {t['scenario']}

Submit your response in the following format:

Emotional Response: [Character's emotional reaction]
Narrative: [Explanation for the emotional reaction]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The emotional response is plausible and contextually appropriate.",
            "The narrative provides a clear and logical explanation for the emotional reaction."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
