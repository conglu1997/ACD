class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Describe and generate the code for a bubble sort algorithm."
            },
            "2": {
                "prompt": "Describe and generate the code for a binary search algorithm."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['prompt']
        return f"""Generate a detailed explanation and code for the following algorithm: {prompt}. 
Your explanation should include:
1. A description of what the algorithm does.
2. A step-by-step explanation of how the algorithm works.
3. The time complexity of the algorithm.
4. The space complexity of the algorithm.

Provide the code implementation in Python. Ensure that your explanation is clear, detailed, and logically structured.
Submit your response as a plain text string in the following format:

Description: [Your description]
Steps: [Your step-by-step explanation]
Time Complexity: [Your time complexity analysis]
Space Complexity: [Your space complexity analysis]
Code: [Your Python code]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately describe the algorithm.",
            "The step-by-step explanation should be clear and logically structured.",
            "The time complexity analysis should be correct.",
            "The space complexity analysis should be correct.",
            "The code implementation should be correct and functional."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
