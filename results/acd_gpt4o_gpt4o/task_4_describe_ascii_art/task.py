class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art": """
  *
 ***
*****
 ***
  *
""", "description": "A diamond shape made out of stars."},
            "2": {"art": """
  #
 ###
#####
 ###
  #
""", "description": "A diamond shape made out of hashes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the following ASCII art pattern in detail. Your description should accurately convey the shape and the characters used:

{t['art']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately describe the shape.", "The description should mention the characters used in the pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
