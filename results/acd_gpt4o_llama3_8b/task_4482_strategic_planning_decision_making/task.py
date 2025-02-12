class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A company is facing declining sales in one of its key product lines.",
                "constraints": [
                    "The budget for marketing and product development is limited.",
                    "There is increasing competition in the market.",
                    "The company has a strong research and development team.",
                    "Customer preferences are shifting towards more eco-friendly products.",
                    "Supply chain disruptions are affecting product availability."],
                "unexpected_event": "A key competitor has just released a highly innovative product that is capturing significant market share."
            },
            "2": {
                "scenario": "A city is experiencing traffic congestion problems during peak hours.",
                "constraints": [
                    "The city's budget for infrastructure development is limited.",
                    "Public transportation usage is low.",
                    "There is a growing population in the city.",
                    "Air pollution levels are rising.",
                    "Residents are resistant to changes that affect their daily commute."],
                "unexpected_event": "A major public transportation strike has just been announced, severely limiting available transport options."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following scenario, create a strategic plan or make a decision that addresses the problem. Consider the given constraints and unexpected event, and provide a detailed explanation of your plan or decision.

Scenario: {t['scenario']}

Constraints:
""" + '\n'.join([f"- {constraint}" for constraint in t['constraints']]) + """

Unexpected Event: {t['unexpected_event']}

Your response should include:
1. A clear statement of the problem.
2. A detailed plan or decision that addresses the problem.
3. An explanation of how the plan or decision takes the constraints into account.
4. Any potential risks or challenges and how they can be mitigated.
5. An evaluation of the expected outcomes and how success will be measured.
6. A contingency plan addressing the unexpected event, including how it will be integrated into the overall strategy.

Submit your response as a plain text string. Ensure your response is well-structured, logically organized, and comprehensive."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response includes a clear statement of the problem.",
            "The response provides a detailed plan or decision that addresses the problem.",
            "The response explains how the plan or decision takes the constraints into account.",
            "The response identifies potential risks or challenges and how they can be mitigated.",
            "The response evaluates the expected outcomes and how success will be measured.",
            "The response includes a contingency plan addressing the unexpected event and integrates it into the overall strategy.",
            "The response is well-structured, logically organized, and comprehensive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
