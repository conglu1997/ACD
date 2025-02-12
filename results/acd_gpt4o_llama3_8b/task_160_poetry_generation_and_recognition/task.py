class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "theme": "nature", "constraints": "The poem should have at least two stanzas, each with four lines, and follow an ABAB rhyme scheme.", "example": "Under the canopy of green,\nWhere sunlight dances, unseen,\nWhispers of the forest's song,\nGuide the weary traveler along.", "synthetic_examples": ["Beneath the sky so blue,\nFields of flowers in every hue,\nNature's beauty all around,\nIn every sight and sound.", "In the heart of the wood,\nNature's secrets understood,\nWhispers of the ancient trees,\nCarried on the gentle breeze."]},
            "2": {"task_type": "recognition", "text": "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate:\nRough winds do shake the darling buds of May,\nAnd summer's lease hath all too short a date:", "question": "Identify the rhyme scheme and any metaphors used in the text. Submit your answer in the following format: 'Rhyme Scheme: [scheme], Metaphors: [list of metaphors]'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generation":
            examples = '\n'.join(t.get('synthetic_examples', []))
            return f"Generate a poem based on the following theme: {t['theme']}. {t['constraints']}\nExample: {t['example']}\nAdditional examples:\n{examples}"
        elif t["task_type"] == "recognition":
            return f"Read the following text and answer the question: {t['text']}\nQuestion: {t['question']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generation":
            criteria = ["The poem should follow the given theme and constraints, including the ABAB rhyme scheme and at least two stanzas with four lines each."]
        elif t["task_type"] == "recognition":
            criteria = ["The response should correctly identify the rhyme scheme and any metaphors used in the text."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
