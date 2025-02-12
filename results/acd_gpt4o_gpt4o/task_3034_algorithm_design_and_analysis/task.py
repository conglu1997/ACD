class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Design an algorithm to find the greatest common divisor (GCD) of two integers using the Euclidean method. Provide a step-by-step explanation of the algorithm."},
            "2": {"prompt": "Analyze the time complexity of the following algorithm for finding the maximum element in an unsorted list:\n\ndef find_max(arr):\n    max_element = arr[0]\n    for element in arr[1:]:\n        if element > max_element:\n            max_element = element\n    return max_element\nProvide a detailed analysis of the time complexity."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to perform the following algorithm-related task:\n\nPrompt: {t['prompt']}\n\nFor Task 1: Design an algorithm to solve the given problem and explain it step-by-step. Ensure your explanation is clear, logical, and covers each step of the algorithm in detail. Provide your response in plain text format.\nFor Task 2: Analyze the time complexity of the given algorithm. Provide a detailed analysis and explain the reasoning behind your conclusions. Provide your response in plain text format.\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm design should be clear, logical, and correctly solve the problem.",
            "The analysis should accurately determine the time complexity and provide a clear explanation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
