class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"word_type": "noun", "required_letters": "a,e,i"},
            "2": {"word_type": "verb", "required_letters": "o,u,y"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a new {t['word_type']} that includes the following letters: {t['required_letters']}. Provide a definition for this new word (between 20-50 words) and use it in a sentence (between 10-20 words) to demonstrate its meaning. Ensure that the word is original, and the sentence clearly shows its usage in context. Your response should be in the following format:

Word: [Your new word]
Definition: [Your definition]
Sentence: [Your sentence]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The new word must include the required letters.",
            "The definition should be between 20-50 words.",
            "The sentence should demonstrate proper usage of the word in context and be between 10-20 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
