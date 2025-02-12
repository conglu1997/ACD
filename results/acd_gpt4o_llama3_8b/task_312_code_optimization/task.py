class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def inefficient_function(data):\n    result = []\n    for i in range(len(data)):\n        for j in range(i+1, len(data)):\n            if data[i] == data[j]:\n                result.append(data[i])\n    return result", "description": "Optimize the given function to improve its performance. Consider using more efficient data structures or algorithms."},
            "2": {"code": "def slow_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr", "description": "Optimize the sorting algorithm to improve its performance. Consider more efficient sorting algorithms."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Optimize the following code snippet for better performance:\n\n{t['code']}\n\n{t['description']}\n\nSubmit your optimized code as a plain text string. Ensure that your optimized code is logically correct and produces the same output as the original code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The optimized code should have significantly better performance than the original.", "The optimized code should be logically correct and produce the same output as the original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
