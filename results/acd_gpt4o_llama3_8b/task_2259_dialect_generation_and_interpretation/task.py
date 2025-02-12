class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a dialogue in a given dialect.",
                "instructions": "Write a dialogue between two friends meeting after a long time. The dialogue should be written in the Southern American English dialect. Ensure that the dialogue captures the linguistic characteristics and cultural nuances of Southern American English. Submit your dialogue as a plain text string in the format:\nDialogue: [Your dialogue here]"
            },
            "2": {
                "description": "Interpret the same dialogue written in another dialect.",
                "instructions": "Interpret the following dialogue written in the Cockney dialect. Provide a translation and explanation of the dialogue, capturing the meaning and cultural context. Submit your interpretation as a plain text string in the format:\nInterpretation: [Your interpretation here]\n\nCockney Dialogue: 'Alright mate, ain't seen you in donkey's years! How's it been, then?' 'Blimey, it's been a right old while, innit? Been up to me eyeballs in work, but you know how it is.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['instructions']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['description'] == 'Generate a dialogue in a given dialect.':
            criteria = [
                "The dialogue must accurately reflect the linguistic characteristics of the specified dialect.",
                "The dialogue should be coherent and contextually appropriate.",
                "The dialogue should capture the cultural nuances of the dialect."]
        elif t['description'] == 'Interpret the same dialogue written in another dialect.':
            criteria = [
                "The interpretation must accurately reflect the meaning of the original dialogue.",
                "The translation should capture the cultural context of the original dialect.",
                "The interpretation should be logically consistent and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
