class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "character": "Sherlock Holmes",
                "context": "You are in 19th century London, solving a complex murder mystery. You encounter a suspect during your investigation. Sherlock's keen observation skills and logical reasoning should be evident in the dialogue."
            },
            "2": {
                "character": "Galadriel",
                "context": "You are in Middle-earth, during the Third Age. You meet a group of adventurers seeking your wisdom about a rising darkness in the land. Galadriel's wisdom, grace, and mystical nature should be reflected in the conversation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Assume the role of {t['character']} and engage in a conversation based on the following context: {t['context']}. Ensure your dialogue is consistent with the character's personality, background, and the given context. Submit your conversation as a dialogue exchange format, with each line prefixed by the character's name or 'You' if you are responding. Aim for a minimum of 10 dialogue exchanges."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be consistent with the character's personality.",
            "The dialogue should be relevant to the given context.",
            "The conversation should contain a minimum of 10 dialogue exchanges.",
            "The dialogue should reflect the storyline and setting appropriately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
