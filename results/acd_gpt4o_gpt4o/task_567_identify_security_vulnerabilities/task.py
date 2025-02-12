class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def authenticate(user, password):\n    if user == 'admin' and password == 'password':\n        return True\n    return False\n# Note: This is a hardcoded password vulnerability."},
            "2": {"code": "def get_user_data(user_id):\n    query = f'SELECT * FROM users WHERE id = {user_id}'\n    return execute_query(query)\n# Note: This is an SQL injection vulnerability."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and explain any security vulnerabilities in the following piece of code. Provide a detailed explanation of each vulnerability, including why it is a problem and how it could potentially be exploited. Additionally, suggest ways to fix each identified vulnerability.

Code:
{t['code']}

Ensure your response is comprehensive, accurate, and insightful. Your response should include:
1. Identification of each security vulnerability.
2. Explanation of why each vulnerability is a problem and how it could be exploited.
3. Suggestions for how to fix each identified vulnerability.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include identification of security vulnerabilities.",
            "The explanation should include why each vulnerability is a problem and how it could be exploited.",
            "The response should suggest ways to fix each identified vulnerability."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
