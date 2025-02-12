class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"product": "A new eco-friendly water bottle that keeps drinks cold for 24 hours."},
            "2": {"slogan": "Just Do It."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "product" in t:
            return f"""Create a catchy advertising slogan for the following product:

Product: {t["product"]}

Your slogan should be memorable, concise, and convey the key benefits of the product. Submit your slogan as a plain text string in the format:

Slogan: [Your slogan]"""
        else:
            return f"""Analyze the effectiveness of the following advertising slogan:

Slogan: {t["slogan"]}

Your analysis should cover the following points:
1. The target audience of the slogan.
2. The key message conveyed by the slogan.
3. The emotional appeal or persuasive techniques used.
4. The overall effectiveness of the slogan.

Submit your response as a plain text string in the format:

Analysis: [Your detailed analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "product" in t:
            criteria = ["The slogan should be catchy and memorable.", "The slogan should convey the key benefits of the product.", "The slogan should be concise."]
        else:
            criteria = ["The analysis should identify the target audience.", "The analysis should explain the key message of the slogan.", "The analysis should discuss the emotional appeal or persuasive techniques used.", "The analysis should evaluate the overall effectiveness of the slogan."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
