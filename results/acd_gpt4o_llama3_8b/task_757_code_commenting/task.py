class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "comment", "code": "def add(a, b):\n    return a + b"},
            "2": {"type": "code", "comment": "# This function checks if a number is prime\ndef is_prime(n):\n    if n <= 1: return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0: return False\n    return True"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "comment":
            return f"""Given the following code snippet, generate meaningful comments that explain what the code does. Ensure that the comments are clear, concise, and informative. The comments should explain the purpose of each line or block of code, and not just restate what the code is doing.

Code snippet:
{t['code']}

Submit your response as a plain text string in the following format:
# [Your comment]
[Code]"""
        elif t["type"] == "code":
            return f"""Given the following comments, generate a code snippet that matches the description. Ensure that the code is correct, logically structured, and follows standard coding conventions. The code should perform the functionality described in the comments.

Comments:
{t['comment']}

Submit your response as a plain text string in the following format:
[Code]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["type"] == "comment":
            criteria.append("The comments should explain the purpose of each line or block of code.")
            criteria.append("The comments should be clear, concise, and informative.")
        elif t["type"] == "code":
            criteria.append("The code should be correct and logically structured.")
            criteria.append("The code should follow standard coding conventions.")
            criteria.append("The code should perform the functionality described in the comments.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
