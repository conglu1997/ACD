class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "You are stranded on an island with limited resources. You have a metal spoon, a piece of cloth, and a plastic bottle. Devise a plan to create a signal to attract rescuers."
            },
            "2": {
                "problem": "You need to cross a river with a group of people, but you only have a small boat that can carry two people at a time. Devise a plan to get everyone across the river safely, considering that some people cannot swim."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to generate an innovative solution to the given problem. "
            "Demonstrate your ability to think creatively and use lateral thinking to devise a practical and effective solution. "
            "Ensure your response is clear, detailed, and feasible. Provide your response in plain text format."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be innovative and demonstrate lateral thinking.",
            "The plan should be clear, detailed, and feasible.",
            "The response should address all aspects of the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
