class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "challenge": "Rising global sea levels are threatening coastal cities and displacing millions of people. Develop a comprehensive plan to address this issue, considering environmental, economic, and social factors."
            },
            "2": {
                "challenge": "A new pandemic has emerged, causing widespread health crises and economic disruption. Develop a comprehensive plan to manage the pandemic and mitigate its impact on global health and economies."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        challenge = t["challenge"]
        instructions = f"""Your task is to create a comprehensive plan to address the following global challenge:

Challenge: {challenge}

Your plan should include:
1. A detailed description of the challenge and its potential impacts.
2. A multi-faceted strategy to address the challenge, considering environmental, economic, and social factors.
3. Specific actions and policies that should be implemented.
4. Potential obstacles and how they can be overcome.
5. Metrics to measure the success of the plan.
6. A proposed timeline for the implementation of the plan.

Provide your response in plain text format, structured as follows:

Plan:
[Your comprehensive plan here]

Ensure that your plan is coherent, well-structured, and demonstrates an understanding of the interconnected nature of the challenge.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should include a detailed description of the challenge and its potential impacts.",
            "The plan should present a multi-faceted strategy to address the challenge, considering environmental, economic, and social factors.",
            "The plan should include specific actions and policies that should be implemented.",
            "The plan should identify potential obstacles and how they can be overcome.",
            "The plan should propose metrics to measure the success of the plan.",
            "The plan should propose a timeline for the implementation of the plan.",
            "The plan should be coherent and well-structured.",
            "The plan should demonstrate an understanding of the interconnected nature of the challenge."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
