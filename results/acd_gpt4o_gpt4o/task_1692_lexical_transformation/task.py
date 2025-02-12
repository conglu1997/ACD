class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The cat is sleeping on the mat.", "transformation": "Convert all verbs to their past tense forms."},
            "2": {"sentence": "She sings beautifully.", "transformation": "Convert all verbs to their gerund forms."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to transform the given sentence according to the specified rule while retaining its original meaning. Here is the sentence: '{t["sentence"]}'. Transformation rule: {t["transformation"]} Provide your answer as a transformed sentence in plain text format without additional text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly transform the sentence according to the specified rule.",
            "The transformed sentence should retain the original meaning."]
        sentence = t["sentence"]
        transformation = t["transformation"]
        if sentence == "The cat is sleeping on the mat." and transformation == "Convert all verbs to their past tense forms.":
            correct_answer = "The cat slept on the mat."
        elif sentence == "She sings beautifully." and transformation == "Convert all verbs to their gerund forms.":
            correct_answer = "She is singing beautifully."
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) and submission.strip() == correct_answer else 0.0
