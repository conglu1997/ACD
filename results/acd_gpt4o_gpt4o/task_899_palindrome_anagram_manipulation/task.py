class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "palindrome", "prompt": "Generate a palindrome using the letters in the word 'detartrated'."},
            "2": {"type": "anagram", "prompt": "Generate an anagram of the word 'conversation' that forms a meaningful word or phrase."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "palindrome":
            return f"""Your task is to generate a palindrome using the letters in the given word. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Ensure that the resulting word or phrase is a valid palindrome. Here is the word: {t["prompt"]}. Provide your palindrome in plain text."""
        else:
            return f"""Your task is to generate an anagram of the given word that forms a meaningful word or phrase. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. Ensure that the resulting anagram makes sense in English. Here is the word: {t["prompt"]}. Provide your anagram in plain text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "palindrome":
            criteria = ["The response should be a valid palindrome."]
        else:
            criteria = ["The response should be a valid anagram that forms a meaningful word or phrase."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
