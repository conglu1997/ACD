class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)"},
            "2": {"system": "A vending machine that accepts coins, allows selection of items, and dispenses the selected item if the correct amount is entered."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "code" in t:
            instructions = f"""Your task is to reverse engineer the following code snippet and explain its functionality in detail. Describe what the code does, how it works, and any potential edge cases or limitations.

Code snippet:
{t['code']}

Provide your response in the following format:
1. Functionality: [Explanation of what the code does]
2. How it works: [Explanation of how the code works]
3. Edge cases or limitations: [Discussion of any potential edge cases or limitations]"""
        else:
            instructions = f"""Your task is to reverse engineer the following described system and explain its functionality in detail. Describe how the system works, its components, and any potential edge cases or limitations.

System description:
{t['system']}

Provide your response in the following format:
1. Functionality: [Explanation of what the system does]
2. How it works: [Explanation of how the system works]
3. Components: [Description of the system's components]
4. Edge cases or limitations: [Discussion of any potential edge cases or limitations]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "code" in t:
            criteria = [
                "The explanation should accurately describe the functionality of the code.",
                "The explanation should cover how the code works, including any edge cases or limitations."]
        else:
            criteria = [
                "The explanation should accurately describe the functionality of the system.",
                "The explanation should cover how the system works, its components, and any edge cases or limitations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
