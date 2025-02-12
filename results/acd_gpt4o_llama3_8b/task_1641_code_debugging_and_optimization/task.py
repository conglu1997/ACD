class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def calculate_sum(numbers):\n    total = 0\n    for number in numbers:\n        total += number\n    total += 1 # Off-by-one error\n    return total\n\nprint(calculate_sum([1, 2, 3, 4, 5]))\nprint(calculate_sum([10, -2, 3.5, 8]))\nprint(calculate_sum([]))", "task_type": "debugging"},
            "2": {"code": "def sort_numbers(arr):\n    # Implementing bubble sort\n    for i in range(len(arr)):\n        for j in range(len(arr) - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n    return arr\n\nprint(sort_numbers([64, 34, 25, 12, 22, 11, 90]))", "task_type": "optimization"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "debugging":
            return f"""Complete the following task based on the given code:\n\nCode:\n{t['code']}\n\nTask: Identify and fix any bugs in the code. Ensure that the corrected code functions as intended. Submit your corrected code as a plain text string in the following format:\n\nCorrected Code:\n[Your corrected code here]"""
        elif t["task_type"] == "optimization":
            return f"""Complete the following task based on the given code:\n\nCode:\n{t['code']}\n\nTask: Optimize the given code for better performance. Provide an explanation for the changes made and why they improve performance. Submit your optimized code and explanation as a plain text string in the following format:\n\nOptimized Code:\n[Your optimized code here]\n\nExplanation:\n[Your explanation here]"""
        else:
            raise ValueError("Invalid task type")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "debugging":
            criteria = ["The submitted code should be free of syntax and logical errors.", "The corrected code should produce the expected output when executed."]
        elif t["task_type"] == "optimization":
            criteria = ["The submitted code should be optimized for better performance.", "The explanation should clearly describe the changes made and why they improve performance."]
        else:
            raise ValueError("Invalid task type")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0