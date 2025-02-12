class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Match a valid email address. The email should start with an alphanumeric character, followed by alphanumeric characters, dots, hyphens, or underscores. It should have an @ symbol, followed by a domain name that includes at least one dot and ends with a 2-6 letter top-level domain."},
            "2": {"regex": "^([a-zA-Z0-9_\.-]+)@([a-zA-Z0-9_\.-]+)\.([a-zA-Z\.]{2,6})$"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'criteria' in t:
            return f"""Generate a regular expression that fulfills the following criteria:

{t['criteria']}

Submit your response as a plain text string in the following format: Regex: [Your regular expression]"""
        elif 'regex' in t:
            return f"""Interpret the following regular expression and explain what it matches:

{t['regex']}

Submit your interpretation as a plain text string in the following format: Interpretation: [Your interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'criteria' in t:
            criteria = ["The regular expression should correctly match the specified criteria."]
        elif 'regex' in t:
            criteria = ["The interpretation should correctly explain what the regular expression matches."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
