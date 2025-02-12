class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A friend is sharing their excitement about a recent promotion but also mentions feeling nervous about new responsibilities and missing their old team.",
                "tone": "supportive and enthusiastic"
            },
            "2": {
                "scenario": "A colleague is feeling stressed about an upcoming deadline and mentions missing a family event because of it; they also express frustration about the workload.",
                "tone": "empathetic and encouraging"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an appropriate response to the given social interaction scenario. Make sure to consider the context and tone provided:

Scenario: {t['scenario']}
Tone: {t['tone']}

Ensure your response is contextually relevant and matches the specified tone. Submit your response as a plain text string in the following format:

Response: [Your response]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be contextually relevant to the scenario.",
            "The response should match the specified tone.",
            "The response should be coherent and socially appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
