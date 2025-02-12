class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a manager at a small retail store. Recently, you've noticed a decline in sales and customer satisfaction. You have a limited budget of $500 and 3 part-time employees. Provide a detailed plan to improve both sales and customer satisfaction. Include specific actions and how you will measure success.", "criteria": "The plan should be practical, feasible, include specific actions, and provide methods for measuring success."},
            "2": {"scenario": "You are a software engineer tasked with reducing the loading time of a web application. The application uses a large number of images and external scripts. Provide a detailed solution to optimize the loading time. Consider multiple optimization techniques and explain how each technique will contribute to reducing the loading time.", "criteria": "The solution should be technically sound, practical, consider multiple optimization techniques, and explain the contribution of each technique to reducing the loading time."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following real-world problem by providing actionable advice or a solution based on the given scenario:

Scenario: {t['scenario']}

Format your response as follows:

1. Action Plan: [Your detailed action plan or solution]
2. Measurement of Success: [Methods for measuring success or the impact of your solution]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [t['criteria']]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
