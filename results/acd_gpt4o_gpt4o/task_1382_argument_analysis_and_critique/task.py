class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "premises": [
                    "All humans are mortal.",
                    "Socrates is a human."
                ],
                "conclusion": "Socrates is mortal.",
                "flaws": []
            },
            "2": {
                "premises": [
                    "If it is raining, the ground will be wet.",
                    "The ground is wet."
                ],
                "conclusion": "It is raining.",
                "flaws": [
                    "Affirming the consequent"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        premises = t["premises"]
        conclusion = t["conclusion"]
        instructions = f"""Your task is to analyze the following argument based on the given premises and conclusion. Identify any logical flaws in the argument and suggest improvements.

Premises:
"""
        for premise in premises:
            instructions += f"- {premise}\n"
        instructions += f"\nConclusion:\n- {conclusion}\n\nProvide your response with the following format:\n1. Identify and explain any logical flaws in the argument.\n2. Suggest improvements to make the argument logically valid."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify any logical flaws in the argument.",
            "The response should suggest reasonable improvements to make the argument logically valid.",
            "The response should be logically coherent and well-structured.",
            "The response should provide clear explanations for each identified flaw."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
