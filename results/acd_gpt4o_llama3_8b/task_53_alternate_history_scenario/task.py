class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The American Revolution",
                "point_of_divergence": "What if the British had won the Battle of Yorktown?"
            },
            "2": {
                "event": "The Fall of the Berlin Wall",
                "point_of_divergence": "What if the Berlin Wall had never fallen and East Germany remained a separate state?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write an alternate history scenario based on the following historical event and point of divergence:

Historical Event: {t['event']}
Point of Divergence: {t['point_of_divergence']}

Describe how history might have unfolded differently from the point of divergence. Ensure your scenario is historically plausible, engaging, and includes key events, figures, and outcomes that would have been affected by this change. The narrative should follow a logical progression with a clear beginning, middle, and end. Here is an example structure:

1. Introduction: Briefly describe the historical context and the point of divergence.
2. Alternate Events: Detail the key events and changes that occur as a result of the point of divergence.
3. Conclusion: Summarize the long-term effects and outcomes of this alternate history.

The scenario should be at least 500 words long. Engage the reader by providing vivid descriptions and logical sequences of events. Ensure that the scenario is cohesive, historically accurate, and logically follows from the point of divergence. Submit your scenario in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The scenario should be at least 500 words long.",
            "The narrative should be historically plausible and include key events, figures, and outcomes that would have been affected by the point of divergence.",
            "The scenario should be coherent and well-structured, with a clear beginning, middle, and end.",
            "The alternate history should logically follow from the point of divergence.",
            "The narrative should be engaging and follow a logical progression.",
            "The scenario should be cohesive, historically accurate, and logically follow from the point of divergence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
