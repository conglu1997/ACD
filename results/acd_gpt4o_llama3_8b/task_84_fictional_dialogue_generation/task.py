class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Two friends are discussing their plans for the weekend. One wants to go hiking, while the other prefers to stay home and read a book."
            },
            "2": {
                "scenario": "A detective is interrogating a suspect in a robbery case. The suspect claims innocence but provides conflicting details."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a fictional dialogue based on the given scenario: {t["scenario"]}. Ensure the dialogue is coherent, contextually appropriate, and engaging. The characters should have distinct voices and the conversation should flow naturally. Here is an example format:

Character 1: Hey, what are your plans for the weekend?
Character 2: I'm thinking of going hiking. How about you?
Character 1: I'm not really into hiking. I might just stay home and read a book.
Character 2: That sounds relaxing. Maybe I'll join you for some reading after the hike.

Ensure the dialogue is well-structured, maintains character consistency, and is relevant to the given scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue should be coherent and contextually appropriate.",
            "The characters should have distinct voices.",
            "The conversation should be engaging and flow naturally.",
            "The dialogue should be relevant to the given scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
