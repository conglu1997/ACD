class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "John crossed his arms and avoided eye contact during the meeting."
            },
            "2": {
                "description": "Emily was smiling, but her eyes were tearing up."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to interpret the following description of body language and facial expressions to infer the underlying emotions or intentions.

Description:
{description}

Your response should include:
1. The inferred emotion(s) or intention(s).
2. A brief explanation of how the body language and facial expressions lead to your inference.

Provide your response in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately infer the underlying emotions or intentions based on the description.",
            "The response should be contextually appropriate and demonstrate an understanding of non-verbal cues.",
            "The response should include an explanation of how the body language and facial expressions lead to the inference."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
