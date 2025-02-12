class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "palindrome", "criteria": "Create a palindrome that is at least 5 words long and makes sense as a sentence."},
            "2": {"type": "anagram", "criteria": "Generate an anagram for the phrase 'astronomer' that is also a valid English phrase."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        task_type = t["type"]
        criteria = t["criteria"]
        return f"""Complete the following task based on the given criteria:

Task Type: {task_type.capitalize()}
Criteria: {criteria}

Ensure that your response meets the criteria specified. Submit your response as a plain text string in the following format:

Response: [Your solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should meet the specified criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0