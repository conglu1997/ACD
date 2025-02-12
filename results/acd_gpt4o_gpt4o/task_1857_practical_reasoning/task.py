class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are planning a small outdoor picnic with friends. The weather forecast predicts a 40% chance of rain. You have the option to book a sheltered picnic spot for an additional cost or risk the open spot. Consider the following constraints: Cost of booking sheltered spot, Likelihood of rain, Impact on picnic plans. What would you do? Explain your reasoning."
            },
            "2": {
                "scenario": "You need to buy a gift for a friend’s birthday. You know they love reading, cooking, and outdoor activities. You have a budget of $50. Consider the following constraints: Budget, Friend’s interests, Practicality of the gift. What gift would you choose and why? Explain your reasoning."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Consider the following scenario: {t['scenario']}\n"
            "Take into account the given constraints: {', '.join(t['constraints'])}.\n"
            "Provide your decision and explain your reasoning in plain text format.\n"
            "Your response should be structured as follows:\n"
            "Decision: [Your decision]\n"
            "Reasoning: [Your detailed reasoning]"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
