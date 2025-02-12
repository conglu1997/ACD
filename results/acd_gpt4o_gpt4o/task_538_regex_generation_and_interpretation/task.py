class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "a regex to match a date in the format YYYY-MM-DD, where the year is between 1900 and 2099"},
            "2": {"regex": "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'description' in t:
            instructions = f"""Your task is to create a regular expression (regex) based on the following description:

Description: {t['description']}

Ensure that your regex is accurate and matches the given description. Provide your regex in plain text format. Your response should be structured as follows:

Regex: [Your regex]"""
        else:
            instructions = f"""Your task is to interpret the following regular expression (regex) and describe the pattern it matches:

Regex: {t['regex']}

Ensure that your description is clear, accurate, and covers all aspects of the regex pattern. Provide your description in plain text format. Your response should be structured as follows:

Description: [Your description]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'description' in t:
            criteria = ["The regex should correctly match the described pattern."]
        else:
            criteria = ["The description should accurately interpret the regex pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
