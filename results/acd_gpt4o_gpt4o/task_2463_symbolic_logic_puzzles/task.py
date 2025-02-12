class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'puzzle': 'If P implies Q, Q implies R, and R is false, what can we conclude about P?'
            },
            '2': {
                'puzzle': 'Given the premises: \n(1) A or B,\n(2) Not A,\nwhat can we conclude about B?'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t['puzzle']
        instructions = f"Solve the following logical puzzle:\n\n{puzzle}\n\nYour response should include:\n1. A step-by-step explanation of your reasoning.\n2. The final conclusion based on the given premises.\n\nProvide your response in plain text format."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and logical step-by-step explanation of reasoning.",
            "The response should correctly conclude based on the given premises.",
            "The response should be comprehensive and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
