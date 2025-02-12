class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The American Revolution",
                "alternate_outcome": "The British won the war"
            },
            "2": {
                "event": "The fall of the Berlin Wall",
                "alternate_outcome": "The Berlin Wall remained standing"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reimagine the following historical event with the specified alternate outcome and detail the potential impacts of this new outcome.

Event: {t['event']}
Alternate Outcome: {t['alternate_outcome']}

Your response should be creative, well-reasoned, and demonstrate a deep understanding of historical context. Submit your response as a plain text string in the following format:

Reimagined Event: [Your reimagined event here]
Potential Impacts: [Detail the potential impacts of this new outcome here]

Example response format:
Reimagined Event: The British won the American Revolution.
Potential Impacts: If the British had won the American Revolution, the United States might have remained a collection of British colonies. This could have led to a delay in the spread of democratic ideals and possibly influenced other independence movements around the world. Additionally, the economic, cultural, and political landscape of North America would be vastly different, potentially affecting global events such as World War I and World War II."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The reimagined event should be logically coherent and creative.",
            "The potential impacts should be well-reasoned and demonstrate a deep understanding of historical context.",
            "The response should be detailed and logically consistent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
