class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": """
def calculate_area(radius):
    PI = 3.14
    if radius < 0:
        return "Invalid radius"
    area = PI * radius ** 2
    return area

result = calculate_area(5)
print(f"Area: {result}")
""", "description": "Identify any potential bugs or suggest improvements for the provided code snippet."},
            "2": {"code": """
def find_max(numbers):
    if not numbers:
        return "Empty list"
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [1, 2, 3, 4, 5]
print(f"Max number: {find_max(numbers)}")
""", "description": "Identify any potential bugs or suggest improvements for the provided code snippet."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following code snippet and identify any potential bugs or suggest improvements. Provide a detailed explanation of your findings and suggestions in plain text format:

{t['code']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should identify any potential bugs.", "The response should suggest improvements if applicable.", "The explanation should be detailed and accurate.", "The response should be in plain text format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
