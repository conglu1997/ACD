class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generation", "description": "Generate a sentence that is a palindrome. Ensure that the sentence reads the same backward and forward, ignoring spaces, punctuation, and capitalization."},
            "2": {"type": "interpretation", "palindrome": "A man, a plan, a canal, Panama!", "description": "Interpret the given palindrome and explain why it is considered a palindrome. Ignore spaces, punctuation, and capitalization in your explanation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generation":
            return f"Your task is to generate a sentence that is a palindrome. Ensure that the sentence reads the same backward and forward, ignoring spaces, punctuation, and capitalization. Provide your response in plain text format."
        elif t["type"] == "interpretation":
            palindrome = t["palindrome"]
            return f"Your task is to interpret the given palindrome and explain why it is considered a palindrome. The palindrome is: \n\n{palindrome}\n\nIgnore spaces, punctuation, and capitalization in your explanation. Provide your response in plain text format."
        else:
            raise ValueError("Unknown task type.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generation":
            criteria = [
                "The generated sentence should read the same backward and forward, ignoring spaces, punctuation, and capitalization.",
                "The sentence should be meaningful and grammatically correct."]
        elif t["type"] == "interpretation":
            criteria = [
                "The explanation should accurately describe why the given sequence is a palindrome.",
                "The explanation should ignore spaces, punctuation, and capitalization."]
        else:
            raise ValueError("Unknown task type.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
