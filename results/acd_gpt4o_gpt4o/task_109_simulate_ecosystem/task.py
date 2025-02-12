class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ecosystem": "A forest ecosystem with deer, wolves, and vegetation.",
                "change": "Introduce a significant decrease in the wolf population."
            },
            "2": {
                "ecosystem": "A marine ecosystem with fish, sharks, and plankton.",
                "change": "Introduce a large increase in the plankton population."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to simulate the given ecosystem and predict the outcome based on the specified change. "
            "Describe the interactions between species and how the change will affect the ecosystem over time. "
            "Provide your response in plain text format, including a detailed explanation of the predicted outcome. "
            "Your response should be structured as follows: \n\n"
            "1. Description of the initial ecosystem \n"
            "2. Description of the specified change \n"
            "3. Predicted short-term effects \n"
            "4. Predicted long-term effects \n"
            "5. Explanation of the reasoning behind the predictions"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the initial ecosystem.",
            "The response should accurately describe the specified change.",
            "The predicted short-term and long-term effects should be logically consistent with the change and interactions between species.",
            "The explanation should demonstrate an understanding of the dynamic nature of ecosystems and provide sound reasoning for the predictions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
