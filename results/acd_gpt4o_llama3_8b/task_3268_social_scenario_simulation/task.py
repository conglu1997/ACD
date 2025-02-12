class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are at a friend's dinner party. During the meal, your friend makes a self-deprecating joke about their cooking skills. Most of the guests laugh, but you notice one person who seems uncomfortable and another who tries to change the subject. Additionally, you are aware that your friend has recently been feeling insecure about their cooking. Interpret the scenario and generate an appropriate response that is both supportive and light-hearted, taking into account the uncomfortable guest, the person trying to change the subject, and your friend's insecurities."
            },
            "2": {
                "scenario": "You are in a professional meeting where a colleague presents an idea that has already been rejected in a previous meeting. Some team members seem visibly frustrated by the repetition, while others appear indifferent. Additionally, you know that the colleague presenting the idea is under pressure from upper management to push this idea forward. Interpret the scenario and generate an appropriate response that acknowledges the repetition respectfully while maintaining professionalism, addressing the team's frustration and indifference, and considering the colleague's pressure from management."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following social scenario and generate an appropriate response based on social norms and context:

Scenario: '{t['scenario']}'

Ensure that your response is contextually appropriate and aligns with expected social norms. Submit your response as a plain text string in the following format:

Response: [Your response]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response must be contextually appropriate.",
            "The response must align with expected social norms."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
