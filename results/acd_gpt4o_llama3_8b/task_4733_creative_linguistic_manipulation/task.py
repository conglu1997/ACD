class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Create a palindrome using the word 'level'."},
            "2": {"task": "Generate an anagram for the phrase 'listen to the silent'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'palindrome' in t['task'].lower():
            return f"""Your task is to create a palindrome using the word 'level'. A palindrome is a word, phrase, or sequence that reads the same backward as forward. Ensure that the word 'level' is part of your palindrome.

Submit your response as a plain text string in the following format:
Response: [Your palindrome]"""
        elif 'anagram' in t['task'].lower():
            return f"""Your task is to generate an anagram for the phrase 'listen to the silent'. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

Submit your response as a plain text string in the following format:
Response: [Your anagram]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'palindrome' in t['task'].lower():
            criteria = [
                "The response should be a valid palindrome.",
                "The response should include the word 'level' used appropriately within the palindrome.",
                "The palindrome should be meaningful and coherent."
            ]
        elif 'anagram' in t['task'].lower():
            criteria = [
                "The response should be a valid anagram.",
                "The response should use all letters from the phrase 'listen to the silent'.",
                "The anagram should be meaningful and coherent."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
