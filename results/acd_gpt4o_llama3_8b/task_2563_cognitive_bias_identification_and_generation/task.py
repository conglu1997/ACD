class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A person believes that their favorite sports team will win the championship this year despite the team's poor performance in recent seasons. They selectively remember only the team's past successes and ignore the losses.", "task": "Identify the cognitive bias in the scenario and explain why it fits that bias."},
            "2": {"bias": "confirmation bias", "task": "Generate an example of confirmation bias in a workplace setting."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "scenario" in t:
            return f"""Identify the cognitive bias in the following scenario and explain your reasoning:

Scenario: {t['scenario']}

Submit your response in the following format:
Cognitive Bias: [Name of the cognitive bias]
Explanation: [Your detailed explanation for why this bias fits the scenario. Be specific and thorough in your reasoning.]"""
        elif "bias" in t:
            return f"""Generate an example of the following cognitive bias in a specified setting:

Bias: {t['bias']}

Setting: Workplace

Submit your response in the following format:
Example: [Your generated example that clearly illustrates the specified cognitive bias in the given setting.]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "scenario" in t:
            criteria = [
                "The identified cognitive bias should be correct.",
                "The explanation should logically connect the scenario to the identified bias with specific and thorough reasoning."
            ]
        else:
            criteria = [
                "The generated example should clearly illustrate the specified cognitive bias.",
                "The example should be appropriate for the given setting and should be specific enough to demonstrate understanding of the bias."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
