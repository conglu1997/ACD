class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "idiom": "Bite the bullet"
            },
            "2": {
                "idiom": "Burn the midnight oil"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        idiom = t["idiom"]
        instructions = f"""Your task is to interpret the following idiomatic expression and provide a coherent explanation or usage example.

Idiom: {idiom}

Provide your explanation or example in plain text format. Your response should be structured as follows:
1. Explanation of the idiom
2. A sentence using the idiom correctly"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a correct explanation of the idiom.", "The usage example should accurately reflect the meaning of the idiom in context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
