class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original": "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."},
            "2": {"original": "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous parody of the following original text. Maintain the style and form of the original work while infusing it with humor and exaggeration. Your parody should be coherent, contextually appropriate, and funny. Aim for a length similar to the original text.

Original Text: {t['original']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The parody should maintain the original style and form.",
            "The parody should be humorous and exaggerated.",
            "The parody should be coherent and contextually appropriate.",
            "The parody should capture the essence of the original text."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
