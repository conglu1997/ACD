class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Write a Python function that takes a list of integers and returns a list of those integers sorted in ascending order."},
            "2": {"code": "def inefficient_function(arr):\n    result = []\n    for i in range(len(arr)):\n        min_idx = i\n        for j in range(i+1, len(arr)):\n            if arr[min_idx] > arr[j]:\n                min_idx = j\n        arr[i], arr[min_idx] = arr[min_idx], arr[i]\n    return arr", "description": "Optimize the provided Python function for better performance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "problem" in t:
            return f"Your task is to write a Python function based on the following problem:\n\n{t['problem']}\n\nEnsure that your function is correct, efficient, and follows best coding practices. Provide your function in plain text format."
        elif "code" in t:
            return f"Your task is to optimize the following Python function for better performance:\n\n{t['code']}\n\n{t['description']}\n\nEnsure that your optimized function is correct, efficient, and follows best coding practices. Provide your optimized function in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "problem" in t:
            criteria = [
                "The function should take a list of integers and return a list of those integers sorted in ascending order.",
                "The function should be correct and efficient.",
                "The function should follow best coding practices."]
        elif "code" in t:
            criteria = [
                "The optimized function should perform the same task as the original function.",
                "The optimized function should be more efficient than the original function.",
                "The optimized function should follow best coding practices."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0