class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The fall of the Roman Empire",
                "contemporary_event": "The decline of the Soviet Union"
            },
            "2": {
                "historical_event": "The Industrial Revolution",
                "contemporary_event": "The Digital Revolution"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical and contemporary events, and discuss their similarities and differences:

Historical Event: {t['historical_event']}
Contemporary Event: {t['contemporary_event']}

Your analysis should cover the following points:
1. A brief description of each event.
2. Key similarities between the two events.
3. Key differences between the two events.
4. The impact of each event on society.

Ensure that your analysis is detailed, logically structured, and demonstrates a deep understanding of both events. Submit your response as a plain text string with numbered points for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should include a brief description of each event.",
            "The analysis should identify key similarities between the events.",
            "The analysis should identify key differences between the events.",
            "The analysis should discuss the impact of each event on society.",
            "The analysis should be detailed and logically structured.",
            "The analysis should demonstrate a deep understanding of both events."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
