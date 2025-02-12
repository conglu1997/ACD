class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A friend just lost their job and is feeling very down. They text you saying, 'I don't know what to do anymore. I feel like such a failure. I can't see any way out of this situation and everything seems hopeless.'"
            },
            "2": {
                "scenario": "Your sibling is anxious about an upcoming exam and says, 'I'm so nervous about this test. What if I fail? I've been studying so hard but I just can't shake this anxiety.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the emotional state of the person in the following scenario and generate an empathetic response:

Scenario: {t['scenario']}

Your response should acknowledge their feelings and provide comfort or support. Ensure that your response is empathetic, appropriate, and relevant to the given scenario. The response should be between 50 to 150 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should acknowledge the emotional state of the person.", "The response should be empathetic.", "The response should be appropriate and relevant to the given scenario.", "The response should be between 50 to 150 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
